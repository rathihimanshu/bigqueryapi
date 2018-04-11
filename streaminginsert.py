from google.cloud import bigquery

def main():
	bqclient=bigquery.Client.from_service_account_json("/root/play/keyfile.json")
#	Streaming(bqclient)

#def Streaming(bqclient):
	dataset_ref=bqclient.dataset('streaming')
	table_ref=dataset_ref.table('stream')
	table=bqclient.get_table(table_ref)

	data = [
		(u'himanshu', 27),
		(u'anjali', 30),
	]
	errors=bqclient.create_rows(table,data)
if __name__=="__main__":
	main()
