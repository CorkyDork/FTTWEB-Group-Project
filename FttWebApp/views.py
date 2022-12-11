import json
from django.shortcuts import render
import requests
from fttweb import dbconfigs



def pageHome(request):

	userAuthData = getUserAuthDataFromDbBySession(request)

	if not isinstance(userAuthData, bool): #some session exists

		if "users" in userAuthData: #we got json string - user is authorized
			email = json.loads(userAuthData)['users'][0]['email']
			return render(request,"home.html", {"email":email}) #push all required data to page

		elif isinstance(userAuthData, str): #we got string - session expiered
			return render(request,"home.html", {"email":"SESSION EXPIERED"})

	else: #we got boolean - user not authorized
		return render(request,"home.html")

 
def pageContactUs(request):
	return render(request,"contact.html")


def pageAboutUs(request):
	return render(request,"about.html")


def pageBrokerDetails(request):
	return render(request,"brokerdetails.html")


def pageftpPredict(request):
	return render(request,"ftppredict.html")


def pageReport(request):
	return render(request,"report.html")


def pageViewClients(request):
	return render(request,"viewclients.html")


def getUserAuthDataFromDbBySession(request):
	if 'uid' in request.session: #we have session

		idToken = request.session['uid']

		try:
			userData = dbconfigs.authe.get_account_info(idToken)

			# TODO remove when done developing
			print("User data is: ")
			print(userData)

		except requests.HTTPError as e: #session expiered - we return error message
			error_json = e.args[1]
			error = json.loads(error_json)['error']['message']

			if error == "INVALID_ID_TOKEN":
				msg = "Session expiered, please signin again"
			else:
				msg ="Some error occured, please try again"

			return msg

		#all good - we return user firebase auth data in json
		return json.dumps(userData)

	else: #no session exists
		return False