#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "Hello World!"
###Leslie needs to route this to the index.html page.
#
#
#if __name__ == "__main__":
#    app.debug = True
#    app.run()
#
##This comes from YouTube tutorial.
import flask, flask.views
app = flask.Flask(__name__)

#class View(flask.views.MethodView):
#    def get(self):
#        return 'Hello There!'

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
app.add_url_rule('/', view_func=View.as_view('Main'), methods=['GET'])

app.debug = True
app.run()