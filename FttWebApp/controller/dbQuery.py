from fttweb import dbconfigs



def setOrUpdateFieldsDuringUserSignUp(data):
    brokerRef = dbconfigs.FSDb.collection("brokers").document(data['localId'])

    # Check if the document exists
    docSnapshot = brokerRef.get()
    if docSnapshot.exists:

        userExtraData = {
			'first_name': data['firstName'],
            'last_name': data['lastName'],
		}

        if 'financialInstitute' in data:
            userExtraData.update({'financial_institute': data['financialInstitute']})

        # Update only given fields in the document if it exists
        brokerRef.update(userExtraData)

    else:
        # Create the document if it doesnt exist
        userExtraData = {
			'first_name': data['firstName'],
            'last_name': data['lastName'],
		}

        if 'financialInstitute' in data:
            userExtraData.update({'financial_institute': data['financialInstitute']})

        # Update only given fields in the document if it exists
        brokerRef.set(userExtraData)
