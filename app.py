from flask import Flask, request, render_template
from InvertedIndex import InvertedIndex
from Database import Database
import csv


app = Flask(__name__)
db = Database()
inverted_Index = InvertedIndex(db)

def __init__(self, db):
    self.db = db    
    
@app.route('/')
def index():    
    query = request.args.get("query", None)
    if query:
        app.logger.info("Query {} received".format(query))
        results = retrieve(query)
        return render_template('results.html', query=query, results=results)
    else:
        load()
        return render_template('index.html')

def load():
    print("Index")
    with open('Project_data.csv',encoding="utf=8") as f:        
        reader = csv.reader(f, delimiter=",")
        next(reader)            
        for i, row in enumerate(reader):
            document = {
            'id': i,
            'text':  " ".join([row[0], row[1], row[2], row[5]]),
            'name':  row[2],
            'address':  " ".join([row[3], row[1], row[0]]),
            'operation':   row[4]
            }
            # print(document)
            inverted_Index.index_document(document,i) 

def retrieve(query):
    document=[]
    app.logger.debug("Ran NLP on query.")
    result = inverted_Index.lookup_query(query)
    print(result)
    for row in enumerate(result):
        print(row[1][0])
        document.append(db.get(row[1][0]))
        print(str(document))
    return document