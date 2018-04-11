from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
	Listprojects(bqclient)

def Listprojects(bqclient):
	for project in bqclient.list_projects():
		print("Name of the project is--{}".format(project.project_id))	

if __name__=="__main__":
	main()
