from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
	Deletedataset(bqclient)


def Deletedataset(bqclient):
	datasetref=bqclient.dataset("newdataset2")

	bqclient.delete_dataset(datasetref)




if __name__=="__main__":
	main()
