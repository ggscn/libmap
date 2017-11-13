from google.cloud import bigquery

#https://blog.gdeltproject.org/google-bigquery-3-5m-books-sample-queries/

def get_credentials():
    service_account_path = '../instance/libmap.json'
    return bigquery.Client.from_service_account_json(
        service_account_path)
    

def query(table_address,start_date,end_date,title):

    with open('query.txt', 'r') as query_file:
        query = query_file.read()

    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = True

    client = get_credentials()
    query = query.format(table_address,start_date,end_date,title)
    query_job = client.query(query, job_config=job_config)
    print(query)

    return query_job.result()  # Waits for job to complete.
