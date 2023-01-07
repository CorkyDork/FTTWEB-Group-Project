from decimal import Decimal
from fttweb import dbconfigs



# Generate context data functions
def generateContextOfError(code, msg):
	context = {
		"isError": True,
		"showInToast" : False,
		"code": code,
		"msg": msg,
	}
	return context


def generateContextOfToastData(code, title, msg, type, duration):
	context = {
		"title" : title,
		"code": code,
		"msg": msg,
		"type": type,
		"showDuration": duration,
	} 
	return context


def generateContextOfUserAuthData(userAuthData):
	if "users" in userAuthData:
		authData = {
			"localId": userAuthData["users"][0]["localId"] if "localId" in userAuthData["users"][0] else False,
			"isAuth": True,
			"email": userAuthData["users"][0]["email"] if "email" in userAuthData["users"][0] else "NULL",
			"isEmailVerified": userAuthData["users"][0]["emailVerified"] if "emailVerified" in userAuthData["users"][0] else False,
			"photoUrl": userAuthData["users"][0]["photoUrl"] if "photoUrl" in userAuthData["users"][0] else False
		}
	else:
		authData = {
			"localId": userAuthData["localId"] if "localId" in userAuthData  else "NULL",
			"isAuth": True,
			"email": userAuthData["email"] if "email" in userAuthData  else "NULL",
			"isEmailVerified": userAuthData["emailVerified"] if "emailVerified" in userAuthData  else "NULL",
			"photoUrl": userAuthData["photoUrl"] if "photoUrl" in userAuthData  else "NULL"
		}

	return authData


def generateContextOfFinancialInstitutionDataFromDb():
	finInstCollRef = dbconfigs.FSDb.collection("financial_institutions")
	finInstDocs = finInstCollRef.stream()

	finInstitution = {}

	for doc in finInstDocs:
		finInstitution.update(
			{
				doc.id: {
					"percentage": round(Decimal(doc.get('percentage')*100), 2)
				}
			}
		)
 
	return finInstitution


def generateContextOfBrokerExtraDetailsFromDb(brokerLocalId):
	brokerDetailsDocRef = dbconfigs.FSDb.collection("brokers").document(brokerLocalId).get()

	# Grab name of financial institution of current broker
	financialInstitutionName = brokerDetailsDocRef.get('financial_institute')

	# Get financial institution percentage value from financial institution collection
	financialInstitutionDetailsDocRef = dbconfigs.FSDb.collection("financial_institutions").document(financialInstitutionName).get()
	financialInstitutionPercentage = financialInstitutionDetailsDocRef.get('percentage')

	brokerDetails = {
		"firstName": brokerDetailsDocRef.get('first_name'),
		"lastName": brokerDetailsDocRef.get('last_name'),
		"financialInstitution": financialInstitutionName,
		"financialInstitutionPercentage": round(Decimal(financialInstitutionPercentage*100), 2) if financialInstitutionPercentage else "None",
	}
 
	return brokerDetails



def generateContextOfBrokersClientsDataFromDb(brokerLocalId):
	# All users collection reference
	clientsCollRef = dbconfigs.FSDb.collection("users")

	# Documents in the collection of users which signed up under our broker
	brokerClients = clientsCollRef.where('broker_localid', '==', brokerLocalId)

	# Get all registered users object from firebase authenditication
	users = dbconfigs.auth.list_users().iterate_all()

	brokerClientsDetails = {}

	# Go over list of clients of this broker
	for doc in brokerClients.stream():
		for user in [u for u in users if u.uid == doc.id]: # Get this clients email from firebase authenditication user object
			userEmail = user.email

		brokerClientsDetails.update({
			doc.id: {
				"firstName": doc.get('first_name'),
				"lastName": doc.get('last_name'),
				"email": userEmail
			}}
		)
 
	return brokerClientsDetails