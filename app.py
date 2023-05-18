from flask import Flask, render_template

app = Flask(__name__)

#homepage
@app.route("/") 
def hello_world():
  return render_template('home.html')

#starforce calculator

#yelp analysis

#index fund analysis

#for testing
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)