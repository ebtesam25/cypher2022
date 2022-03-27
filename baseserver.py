from flask import Flask, request, abort, Response
from flask import redirect

from flask_cors import CORS
from flask import render_template
import json

import cockroachdbhelper as cdh
from hashlib import sha256




app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("immigrace.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>"""










@app.route("/handleCockroachRequest", methods=['GET', 'POST'])
def hcr():
    
    conn = cdh.connector()
    cdh.initialize(conn)
    
    
    
    
    print ("*******************************")
    
    print ("request JSON is:")

    res = request.get_json()
    print (res)
    print ("##################################")
    print( res['queryResult']['queryText'])
    
    if 'queryResult' in res:
        if 'queryText' in res['queryResult']:
            types = []
            
            if 'scholarship' in res['queryResult']['queryText']:
                types.append('scholarship')
                results = cdh.getresources(conn, types)
                results.append("I can tell you more about them if you're interested!")
                
                status = {}
                fms = []
                text1 = {}
                text2 = {}
                text2['text'] = results
                text1['text'] = text2
                fms.append(text1)
                
                status["fulfillmentMessages"] = fms
                # status["server"] = "up"
                # status["results"] = results 

                statusjson = json.dumps(status)

                print(statusjson)

                js = "<html> <body>OK THIS WoRKS</body></html>"

                resp = Response(statusjson, status=200, mimetype='application/json')
                ##resp.headers['Link'] = 'http://google.com'

                return resp
                
            
            if 'legal' in res['queryResult']['queryText']:
                types.append('legal')
                results = cdh.getresources(conn, types)
                results.append("I can tell you more about them if you're interested!")
                
                status = {}
                fms = []
                text1 = {}
                text2 = {}
                text2['text'] = results
                text1['text'] = text2
                fms.append(text1)
                
                status["fulfillmentMessages"] = fms
                # status["server"] = "up"
                # status["results"] = results 

                statusjson = json.dumps(status)

                print(statusjson)

                js = "<html> <body>OK THIS WoRKS</body></html>"

                resp = Response(statusjson, status=200, mimetype='application/json')
                ##resp.headers['Link'] = 'http://google.com'

                return resp
                
            
            if 'financial' in res['queryResult']['queryText']:
                types.append('financial')
                results = cdh.getresources(conn, types)
                results.append("I can tell you more about them if you're interested!")
                
                status = {}
                fms = []
                text1 = {}
                text2 = {}
                text2['text'] = results
                text1['text'] = text2
                fms.append(text1)
                
                status["fulfillmentMessages"] = fms
                # status["server"] = "up"
                # status["results"] = results 

                statusjson = json.dumps(status)

                print(statusjson)

                js = "<html> <body>OK THIS WoRKS</body></html>"

                resp = Response(statusjson, status=200, mimetype='application/json')
                ##resp.headers['Link'] = 'http://google.com'

                return resp
                    
            types.append('all')
            results = cdh.getresources(conn, types)
            results.append("I can tell you more about them if you're interested!")
            
            status = {}
            fms = []
            text1 = {}
            text2 = {}
            text2['text'] = results
            text1['text'] = text2
            fms.append(text1)
            
            status["fulfillmentMessages"] = fms
            # status["server"] = "up"
            # status["results"] = results 

            statusjson = json.dumps(status)

            print(statusjson)

            js = "<html> <body>OK THIS WoRKS</body></html>"

            resp = Response(statusjson, status=200, mimetype='application/json')
            ##resp.headers['Link'] = 'http://google.com'

            return resp
    
    print ("*******************************")

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()


    status = {}
    status["server"] = "up"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp







@app.route("/dummyJson", methods=['GET', 'POST'])
def dummyJson():
    
    print ("*******************************")
    
    print ("request JSON is:")

    res = request.get_json()
    print (res)
    
    print ("*******************************")

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()


    status = {}
    status["server"] = "up"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp


if __name__ == '__main__':
    # app.run()
    # app.run(debug=True, host = '45.79.199.42', port = 8090)
    app.run(debug=True, host = 'localhost', port = 8099)  ##change hostname here
