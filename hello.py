# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)
#
# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name
#
# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))
#
# if __name__ == '__main__':
#    app.run(debug = True)
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
