from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
	Createdataset(bqclient)

def Createdataset(bqclient):
	datasetname = "streaming"
	dataset_ref = bqclient.dataset(datasetname)
	
	datasetname2=bigquery.Dataset(dataset_ref)
	demodataset=bqclient.create_dataset(datasetname2)

if __name__=="__main__":
	main()
