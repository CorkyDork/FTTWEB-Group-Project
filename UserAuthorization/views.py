import json
from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from UserAuthorization.controller import userAuth




@csrf_exempt
def ApiIsSignIn(request):
	statusData = userAuth.HandleApiIsSignIn(request)

	# Prepair data context
	context = {
		'toasts': statusData['toasts'] if "toasts" in statusData else False,
		'authData': statusData['authData'] if "authData" in statusData else False
	}

	return HttpResponse(json.dumps(context)) # Front end handle everything -> it will redirects and show toast


@csrf_exempt
def ApiIsSignUp(request):
	statusData = userAuth.HandleApiIsSignUp(request)

	# Prepair data context
	context = {
		'toasts': statusData['toasts'] if "toasts" in statusData else False,
		'authData': statusData['authData'] if "authData" in statusData else False
	}

	return HttpResponse(json.dumps(context))


@csrf_exempt
def ApiIsPasswordReset(request):
	statusData = userAuth.HandleApiIsPasswordReset(request)
	
	# Prepair data context
	context = {
		'toasts': statusData['toasts'] if "toasts" in statusData else False,
		'authData': statusData['authData'] if "authData" in statusData else False
	}

	return HttpResponse(json.dumps(context))


def ApiIsLogout(request):
	auth.logout(request)
	return redirect("/")


@csrf_exempt
def ApiIsFirebaseSocialSignin(request):
	statusData = userAuth.HandleApiIsFirebaseSocialSignin(request)
	
	# Prepair data context
	context = {
		'toasts': statusData['toasts'] if "toasts" in statusData else False,
		'authData': statusData['authData'] if "authData" in statusData else False
	}

	return HttpResponse(json.dumps(context))