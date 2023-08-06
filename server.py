from flask import Flask, Response,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    n1=int(data["first"])
    n2=int(data["second"])
    result=n1+n2
    return {"result":result},200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json
    n1=int(data["first"])
    n2=int(data["second"])
    result=n1-n2
    return {"result":result},200
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
