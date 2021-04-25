import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
   result = 25
   return render_template('index.html',result = result)

@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      exp = request.form["experience"]
      test =request.form["testscore"]
      interview =request.form["interviewscore"]
      final_features =[np.array([int(exp),int(test),int(interview)])]
      result = model.predict(final_features)
      output = round(result[0],2)
      return render_template("index.html",result = output)

if __name__ == '__main__':
   app.run(debug = True)

