from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential


search_endpoint: str = "https://octopian-semanticsearch.search.windows.net"
search_api_key: str = "DTmPLjSVcBHOTXK2VBXgGb7GpxQWSYvyxBnLsXlGfiAzSeDEajoK"


def createSearchClient(index_name):
    search_client = SearchClient(endpoint=search_endpoint,
        index_name=index_name,
        credential=AzureKeyCredential(search_api_key))
    return search_client
    
def getResult(index_name ,prompt):
    results =  createSearchClient(index_name).search(query_type='semantic', semantic_configuration_name='my-semantic-config',
        search_text=f'{prompt}', 
        query_caption='extractive')
    return results