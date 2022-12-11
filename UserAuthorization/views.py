import json
from fttweb import dbconfigs
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import auth
from fttweb import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests


 
def pageSignIn(request):
	return render(request,"signin.html")


@csrf_exempt
def postSignIn(request):
	userEmail = request.POST.get('email')
	userPass = request.POST.get('pass')
 
	try:
		user = dbconfigs.authe.sign_in_with_email_and_password(userEmail,userPass)

	except requests.HTTPError as e:
		errorJson = e.args[1]
		print(errorJson)
		error = json.loads(errorJson)['error']['message']

		if error == "EMAIL_EXISTS":
			msg = "Email already exists"
		elif error == "INVALID_PASSWORD" or error == "EMAIL_NOT_FOUND":
			msg = "Wrong credentials"
		elif error == "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":
			msg = "Too many login attempts, account frozen, please try again later"
		else:
			msg = "Some error occured, please try again"

		return HttpResponse(json.dumps({"code": "signin_error","msg": msg}))


	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	
	return HttpResponse(json.dumps({"code": "signin_success"}))


@csrf_exempt
def postSignUp(request):
	userEmail = request.POST.get('email')
	userPass = request.POST.get('pass')
	userName = request.POST.get('username')

	try:
		user = dbconfigs.authe.create_user_with_email_and_password(userEmail,userPass)
		
	except requests.HTTPError as e:
		errorJson = e.args[1]
		print(errorJson)
		error = json.loads(errorJson)['error']['message']

		if error == "EMAIL_EXISTS":
			msg = "Email already registered, please signin"
		elif error == "WEAK_PASSWORD : Password should be at least 6 characters":
			msg = "Weak password, must be atleast 6 characters"
		else:
			msg = "Some error occured, please try again"

		return HttpResponse(json.dumps({"code": "signup_error","msg": msg}))

	
	userData = dbconfigs.authe.get_account_info(user['idToken'])
	print(userData)
	#authe.send_email_verification(user['idToken']) #TODO enable to send emails	
	
	uId = user['localId']
	data = {"username":userName}
	dbconfigs.database.child("users").child(uId).child("details").set(data)
	
	return HttpResponse(json.dumps({"code": "signup_success"}))


@csrf_exempt
def postPasswordReset(request):
	email = request.POST.get('email')

	try:
		dbconfigs.authe.send_password_reset_email(email)

	except requests.HTTPError as e:
		errorJson = e.args[1]
		print(errorJson)
		error = json.loads(errorJson)['error']['message']

		if error == "EMAIL_NOT_FOUND":
			msg = "Given email does not belong to any account"
		else:
			msg = "Some error occured, please try again"

		return HttpResponse(json.dumps({"code": "reset_error","msg": msg}))
	
	return HttpResponse(json.dumps({"code": "reset_success"}))


def pageLogout(request):
	auth.logout(request)
	return render(request,"home.html")


@csrf_exempt
def postFirebaseSocialSignin(request):

	username = request.POST.get("username")
	email = request.POST.get("email")
	provider = request.POST.get("provider")
	token = request.POST.get("token")
	
	firbase_response = loadDatafromFirebaseApi(token)
	userData = dbconfigs.authe.get_account_info(token)

	firbase_dict = json.loads(firbase_response)
	
	if "users" in firbase_dict:
		user=firbase_dict["users"]
		if len(user)>0:
			user_one=user[0]
			
			if email == user_one["email"]:
				provider1 = user_one["providerUserInfo"][0]["providerId"]

				if user_one["emailVerified"]==1 or user_one["emailVerified"]==True or user_one["emailVerified"]=="True" or provider1=="facebook.com":
					data = proceedToLogin(request,email,username,token,provider)
					return HttpResponse(data)

				else:
					return HttpResponse("Please verify your email")

			else:
				return HttpResponse("Unknown user email")
	else:
		return HttpResponse("Bad request")


def loadDatafromFirebaseApi(token):

	ENDPOINT = 'https://identitytoolkit.googleapis.com/v1/accounts:lookup'

	# set the request parameters
	params = {
		'idToken': token,
    	'key': 'AIzaSyAkfFcXXg4_8T2yNSoyZMYt3mEOG_SwZak', # take from project settings
	}

	response = requests.post(ENDPOINT, params=params)

	# check the response status
	if response.status_code == 200:
		user_accounts = response.json()
	
	return response.text


def proceedToLogin(request, email, username, token, provider):
	users = User.objects.filter(username = username).exists()

	request.session['uid'] = str(token)
	
	if users == True:
		user_one = User.objects.get(username = username)
		user_one.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request, user_one)
		return "login_success"
	else:
		user = User.objects.create_user(username = username, email = email, password = settings.SECRET_KEY)
		user_one = User.objects.get(username = username)
		user_one.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request, user_one)
		return "login_success"