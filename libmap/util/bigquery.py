import os
from google.oauth2 import service_account
from google.cloud import bigquery

#https://blog.gdeltproject.org/google-bigquery-3-5m-books-sample-queries/

class BigQuery:
    def __init__(self, project_name=None, credentials=None):
        if credentials is None:
            self.bq_client = bigquery.Client()


    @classmethod
    def get_query_str(cls, query_name):
        query_str_path = '{}/{}/{}.sql'.format(
            os.path.dirname(os.path.abspath(__file__)),
            'queries',
            query_name
        )

        query_str_path = query_str_path.replace('util/','')
        with open(query_str_path, 'r') as f:
            query_str = f.read()
        return query_str


    def query(self, query_str):
        query_result = self.bq_client.query(
            query_str).result()
        
        cols = [x.name for x in query_result.schema]
        rows = [{c: r[i] for i, c in enumerate(cols)} for r in query_result]
        return rows

