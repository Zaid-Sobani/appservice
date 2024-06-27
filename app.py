from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from searchClient import getResult

app = Flask(__name__)
CORS(app)

api_key = 'KfuyYJl13wrx5u8lfAaMWb1snOXdZ3fofwRVAdgAzLWwQ1snOXdZ3'

@app.route('/api/nakl', methods=['POST'])
def getNakeldata():
    if request.headers.get('api-key') == api_key:
        try:
            prompt = request.json.get('prompt')
            context = request.json.get('context')
            
            results =  getResult('nakl', prompt)
        
            results_array = []
            for result in results:
                if result['@search.reranker_score'] != None and result['@search.reranker_score'] >= 1.2:
                    record = {'Id' : result['Id'], 'ServiceID' : result['ServiceID'],
                            'ServiceSubCategoryName': result['ServiceSubCategoryName'], 'ServiceName' : result['ServiceName'], 
                            'ServiceSubCategoryID' : result['ServiceSubCategoryID'],
                            'ServiceDescription' : result['ServiceDescription'], 'ServiceWeight' : result['ServiceWeight'],'ServicePrice' : result['ServicePrice'],'ServiceCost' : result['ServiceCost'],'ServiceQuantity' : result['ServiceQuantity'],'ItemID' : result['ItemID'],'ItemName' : result['ItemName'],'ItemDescription' : result['ItemDescription'],'ItemWeight' : result['ItemWeight'],'ItemImagePath' : result['ItemImagePath'],'ItemBalance' : result['ItemBalance'],'ItemCost' : result['ItemCost'],'ItemPrice' : result['ItemPrice'],'ItemQuantity' : result['ItemQuantity'],'ItemVariations' : result['ItemVariations'],'ItemOptions' : result['ItemOptions'],'vector' : result['vector']}
                    record_after_replacing_null = {k : (v if v is not None else '') for k,v in record.items()}
                    results_array.append(record_after_replacing_null)
                    
            results_string = json.dumps(results_array[:10])
            rt = {'context': context, 'response':results_string}
            return rt
        
        except Exception as ex:
            return {'response' : ex}
        
    else:
        return {'error' : 'Invalid API key'}, 401

        
if __name__ == '__main__':
    app.run(debug=True)