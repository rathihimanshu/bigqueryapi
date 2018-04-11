from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
	Createtable(bqclient)

def Createtable(bqclient):
	dataset_ref=bqclient.dataset('streaming')
	schema = [
		bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
		bigquery.SchemaField('age','INTEGER', mode='REQUIRED'),
	]
	table_ref=dataset_ref.table('streamnew')
	table=bigquery.Table(table_ref, schema=schema)
	table=bqclient.create_table(table)

if __name__=="__main__":
	main()
