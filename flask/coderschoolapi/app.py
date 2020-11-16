from flask import Flask, jsonify, render_template, request, json
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import re

es = Elasticsearch(hosts=["https://cd5eb0031138.ngrok.io"])
app = Flask(__name__)

@app.route('/', methods= ['GET'])
def get():
    return "/query?q=yourtext"

def get_prod(txt):
    query_body = {
    "query": {
        "match": {
            "name": {
                "prefix_length": 1,
                "query": txt,
                "fuzziness": 4
            }
        }
        },
    "size" : 100
    }
    ans = es.search(index="products", body=query_body)['hits']['hits']
    return ans
# print(get_prod('may'))
@app.route('/query', methods=['GET'])
def get_product():
    txt = request.args.get('q','')
    if(len(txt)):
        ans = get_prod(txt)
        # print(txt)
        products = []
        pro2 = []
        for i, pro in enumerate(ans):
            name = json.dumps(pro['_source']["name"],ensure_ascii= False)
            price = pro['_source']['price']["sellPrice"]
            products.append((name,price))
            pro2.append(pro['_source'])
        # return json.dumps(pro2,ensure_ascii= False)
        return render_template('tasks.html', products = products)
    else:
        return "no txt"
if __name__ == '__main__':
   app.run(debug = True)
