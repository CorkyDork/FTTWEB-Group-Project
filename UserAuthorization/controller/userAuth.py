import requests
import json
from django.contrib import auth

from fttweb import dbconfigs
from FttWebApp.controller import contextGenerator
from FttWebApp.controller import dbQuery



def HandleApiIsSignIn(request):
	userEmail = request.POST.get('email')
	userPass = request.POST.get('pass')
	
	toasts = [] # Store notifications to display at frontend here

	# Try to sign in in firebase by their api
	try:
		userData = dbconfigs.authe.sign_in_with_email_and_password(userEmail,userPass)

	# Handle wrong api response types
	except requests.HTTPError as e:
		errorJson = e.args[1]
		error = json.loads(errorJson)['error']['message']

		if error == "INVALID_PASSWORD" or error == "EMAIL_NOT_FOUND":
			toast = contextGenerator.generateContextOfToastData(
				error, 
				"Signin failed", 
				"Wrong credentials", 
				"isError", 
				10000
			)

		elif error == "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":
			toast = contextGenerator.generateContextOfToastData(
				error, 
				"Signin failed", 
				"Too many login attempts, account frozen, please try again later", 
				"isError",
				10000
			)

		else:
			toast = contextGenerator.generateContextOfToastData(
				"UNKNOWN_ERROR", 
				"Signin failed", 
				"Some error occured, try again latter", 
				"isError",
				10000
			)
		
		toasts.append(toast) # Append generated notice data to notices list

		return {"toasts": toasts}

	# Set new session
	session_id = userData['idToken']
	request.session['uid'] = str(session_id)

	# All good - we return auth data to handle it properly in views
	dataReply = {
		"authData": contextGenerator.generateContextOfUserAuthData(userData)
	}
	return dataReply


def HandleApiIsSignUp(request):
	firstName = request.POST.get('name')
	lastName = request.POST.get('surname')
	userEmail = request.POST.get('email')
	userPass = request.POST.get('pass')
	finInstitutionName = request.POST.get('finInstitution')

	toasts = [] # Store notifications to display at frontend here
	
	# Try to register in firebase by their api
	try:
		userData = dbconfigs.authe.create_user_with_email_and_password(userEmail,userPass)

	# Handle wrong api response types
	except requests.HTTPError as e:
		errorJson = e.args[1]
		error = json.loads(errorJson)['error']['message']

		if error == "EMAIL_EXISTS":
			toast = contextGenerator.generateContextOfToastData(
				error, 
				"Signup failed", 
				"Email already registered, please signin instead",
				"isError",
				10000
			)

		elif error == "WEAK_PASSWORD : Password should be at least 6 characters":
			toast = contextGenerator.generateContextOfToastData(
				error, 
				"Signup failed", 
				"Weak password, must be atleast 6 characters",
				"isError",
				10000
			)

		else:
			toast =  contextGenerator.generateContextOfToastData(
				"UNKNOWN_ERROR", 
				"Signup failed", 
				"Some error occured, try again latter",
				"isError",
				10000
			)

		toasts.append(toast) # Append generated notice data to notices list

		return {"toasts": toasts}


	# Store extra user data to firestore db "brokers>local id"
	finInstitutionRef = dbconfigs.FSDb.collection("financial_institutions").document(finInstitutionName)
	finInstitutionDocRef = finInstitutionRef.get()

	if finInstitutionDocRef.exists:
		requiredData = {
			'localId': userData['localId'],
			'firstName': firstName,
			'lastName': lastName,
			'financialInstitute': finInstitutionName
		}
		dbQuery.setOrUpdateFieldsDuringUserSignUp(requiredData)

	else:
		print('WARNING: financial institution selected by user not in db')

		requiredData = {
			'localId': userData['localId'],
			'firstName': firstName,
			'lastName': lastName,
			'financialInstitute': "NULL"
		}
		dbQuery.setOrUpdateFieldsDuringUserSignUp(requiredData)

	# Set new session
	session_id = userData['idToken']
	request.session['uid'] = str(session_id)

	#authe.send_email_verification(user['idToken']) #TODO enable to send emails	

	# All good - we return auth data to handle it properly in views
	dataReply = {
		"authData": contextGenerator.generateContextOfUserAuthData(userData)
	}
	return dataReply



def HandleApiIsPasswordReset(request):
	email = request.POST.get('email')
	
	toasts = [] # Store notifications to display at frontend here

	# Try to password reset via firebase api
	try:
		dbconfigs.authe.send_password_reset_email(email)

	# Handle wrong api response types
	except requests.HTTPError as e:
		errorJson = e.args[1]
		error = json.loads(errorJson)['error']['message']

		if error == "EMAIL_NOT_FOUND":
			toast = contextGenerator.generateContextOfToastData(
				error, 
				"Reset failed", 
				"Given email does not belong to any account",
				"isError",
				10000
			)

		else:
			toast = contextGenerator.generateContextOfToastData(
				"UNKNOWN_ERROR", 
				"Reset failed", 
				"Some error occured, try again latter",
				"isError",
				10000
			)

		toasts.append(toast) # Append generated notice data to notices list

		return {"toasts": toasts}

	# All good - we return toast data to display success in fronend
	toast = contextGenerator.generateContextOfToastData(
		"SUCCESS", 
		"Reset Requested", 
		"Please check your email for further instructions",
		"isSuccess",
		10000
	)

	toasts.append(toast) # Append generated notice data to notices list

	return {"toasts": toasts}



def HandleApiIsFirebaseSocialSignin(request):
	email = request.POST.get("email")
	idToken = request.POST.get("token")

	toasts = [] # Store notifications to display at frontend here

	# Try to get user data by session token obtained from firebase api on front end
	try:
		userData = dbconfigs.authe.get_account_info(idToken) # Get user data by token from firebase in frontend

	# Handle wrong api response types
	except requests.HTTPError as e: # Session error
		error_json = e.args[1]
		errorCode = json.loads(error_json)['error']['message']

		if errorCode == "INVALID_ID_TOKEN":
			toast = contextGenerator.generateContextOfToastData(
				"SESSION_INVALID", 
				"Signin failed", 
				"Session attempt was refused",
				"isError",
				10000
			)

		else:
			toast = contextGenerator.generateContextOfToastData(
				"UNKNOWN_ERROR", 
				"Sign in failed", 
				"Some error occured, try again latter",
				"isError",
				10000
			)

		toasts.append(toast) # Append generated notice data to notices list

		return {"toasts": toasts}
 

	# Store extra user data to firestore db "brokers>local id"
	nameParts = userData['users'][0]['displayName'].split()

	requiredData = {
		'localId': userData['users'][0]['localId'],
		'firstName': nameParts[0],
		'lastName': nameParts[1],
		'financialInstitute': "NULL"
	}

	dbQuery.setOrUpdateFieldsDuringUserSignUp(requiredData)


	# User data obtained - proceed with login
	if "users" in userData:
		users = userData["users"]

		if len(users) > 0:
			userOne = users[0]

			if email == userOne["email"]: 
				request.session['uid'] = str(idToken) # Set session to sing in user

				# All good - we return auth data to handle it properly in views
				dataReply = {
					"authData": contextGenerator.generateContextOfUserAuthData(userData)
				}
				return dataReply

			else:
				toast = contextGenerator.generateContextOfToastData(
					"USER_EMAIL_MISMATCH", 
					"Sign in failed", 
					"Some error occured, try again latter",
					"isError",
					10000
				)

				toasts.append(toast) # Append generated notice data to notices list

				return {"toasts": toasts}
	else:
		toast = contextGenerator.generateContextOfToastData(
			"UNKNOWN_ERROR", 
			"Sign in failed", 
			"Some error occured, try again latter"
			"isError",
			10000
		)

		toasts.append(toast) # Append generated notice data to notices list

		return {"toasts": toasts}



# Collects data from firebase users db by providing session id, to which firebase replies with user data or error.
def getUserAuthDataFromDbByTokenFromSession(request):
	toasts = [] # Store notifications to display at frontend here

	if 'uid' in request.session: # Session exists
		idToken = request.session['uid']

		try:
			userData = dbconfigs.authe.get_account_info(idToken)
		
		# Handle wrong api response types
		except requests.HTTPError as e: # Session error
			error_json = e.args[1]
			errorCode = json.loads(error_json)['error']['message']

			if errorCode == "INVALID_ID_TOKEN":
				toast = contextGenerator.generateContextOfToastData(
					"SESSION_EXPIERED", 
					"Session expiered", 
					"Please sign in again",
					"isError",
					10000
				)

				auth.logout(request)

			else:
				toast = contextGenerator.generateContextOfToastData(
					"UNKNOWN_ERROR", 
					"Session error", 
					"Some error occured, you were signed out",
					"isError",
					10000
				)

				auth.logout(request)

			toasts.append(toast) # Append generated notice data to notices list

			return {"toasts": toasts}

		# All good - we return auth data to handle it properly in views
		dataReply = {
			"authData": contextGenerator.generateContextOfUserAuthData(userData)
		}
		return dataReply

	else: # No session exists
		return {"toasts": toasts}
		# print("BOSSSS IN")
		# toast = contextGenerator.generateContextOfToastData(
		# 			"UNKNOWN_ERROR", 
		# 			"Session error", 
		# 			"Some error occured, you were signed out",
		# 			"isSuccess",
		# 			10000
		# 		)

		# toasts.append(toast) # Append generated notice data to notices list

		# toast = contextGenerator.generateContextOfToastData(
		# 			"UNKNOWN_ERROR", 
		# 			"Session error", 
		# 			"Some error occured, you were signed out",
		# 			"isError",
		# 			10000
		# 		)

		# toasts.append(toast) # Append generated notice data to notices list

		# toast = contextGenerator.generateContextOfToastData(
		# 			"UNKNOWN_ERROR", 
		# 			"Session error", 
		# 			"Some error occured, you were signed out",
		# 			"",
		# 			10000
		# 		)

		# toasts.append(toast) # Append generated notice data to notices list
		# return {"toasts": toasts}