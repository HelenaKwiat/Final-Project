from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/graph',methods = ['POST', 'GET'])
def graph():
   if request.method == 'POST':
        team = request.form['submitbutton']
        ###do stuff
        context = {team}
        return render_template('graph.html', context)



if __name__ == '__main__':
   app.run(debug = True)
