from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
	Listdataset(bqclient)

def Listdataset(bqclient):
	for dataset in bqclient.list_datasets():
		print("-----")
		print("Name of the dataset is::{}".format(dataset.dataset_id))
		print("-----")


if __name__=="__main__":
	main()
