import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from FttWebApi.controller import apiControll


@csrf_exempt
def ApiIsGetClientTransactions(request):
	clientTransactions = apiControll.HandleApiIsGetClientTransactions(request)
	return HttpResponse(json.dumps(clientTransactions))