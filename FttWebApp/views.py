from django.shortcuts import render
from django.shortcuts import redirect

from fttweb import dbconfigs
from UserAuthorization.controller import userAuth
from FttWebApp.controller import contextGenerator



# Render functions
def viewIsHome(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)

	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		return redirect("/myclients")

	else: # User not unthenditicated
		finInstitutionsData = contextGenerator.generateContextOfFinancialInstitutionDataFromDb()
		context.update({'finInstitutionsData': finInstitutionsData}) # Append extra data to context

		return render(request,"pages/home.html", context)



def viewIsMyDetails(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)
	
	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		return render(request,"pages/mydetails.html", context)

	else: # User not unthenditicated
		return redirect("/")



def viewIsMyClients(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)
	
	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	print(" xxxxxxxxxxxxxxxxxxxxxxx")
	print(context)

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		brokerClientsDetails = contextGenerator.generateContextOfBrokersClientsDataFromDb(statusData["authData"]['localId']) # Get broker client details
		context.update({'brokerClientsDetails': brokerClientsDetails}) # Append extra data to context
		
		return render(request,"pages/myclients.html", context)

	else: # User not unthenditicated
		return redirect("/")


 
def viewIsContactUs(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)

	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		return render(request,"pages/contact.html", context)

	else: # User not unthenditicated
		finInstitutionsData = contextGenerator.generateContextOfFinancialInstitutionDataFromDb()
		context.update({'finInstitutionsData': finInstitutionsData}) # Append extra data to context

		return render(request,"pages/contact.html", context)



def viewIsPredictions(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)

	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		return render(request,"pages/predictions.html", context)

	else: # User not unthenditicated
		return redirect("/")



def viewIsReports(request):
	statusData = userAuth.getUserAuthDataFromDbByTokenFromSession(request)

	# Prepair data context
	toasts = statusData.get('toasts')
	authData = statusData.get('authData')
	context = {
		'toasts': toasts if toasts and len(toasts) > 0 else False,
		'authData': authData if authData and len(authData) > 0 else False
	}

	if context["authData"]: # User is authenditicated
		brokerDetails = contextGenerator.generateContextOfBrokerExtraDetailsFromDb(statusData["authData"]['localId']) # Get broker extra details
		context.update({'brokerDetails': brokerDetails}) # Append extra data to context

		return render(request,"pages/reports.html", context)

	else: # User not unthenditicated
		return redirect("/")