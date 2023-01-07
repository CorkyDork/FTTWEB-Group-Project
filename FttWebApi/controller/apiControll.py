from fttweb import dbconfigs



def HandleApiIsGetClientTransactions(request):
    clientId = request.POST.get('clientId')

	# Document of broker client for who to get transactions
    clientDocRef = dbconfigs.FSDb.collection('users').document(clientId)
    clientDoc = clientDocRef.get()

    if clientDoc.exists:
        print("CLIENT IS: ")
        print(clientDoc.get('first_name'))

        clientCryptoOrders = clientDoc.collection("orders_crypto")
        clientStockOrders = clientDoc.collection("orders_stocks")

        {
            "order0": [
                {
                "game": "Solitaire",
                "score": 100
                }
            ]
        }


    return True