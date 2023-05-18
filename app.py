from flask import Flask

app = Flask(__name__)

@app.route("/") #refers to homepage
def hello_world():
  return "initial"


#for testing
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)