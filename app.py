##This comes from YouTube tutorial.

import flask, flask.views
from model.portfolio_model import DataController
app = flask.Flask(__name__)

class bySchool(flask.views.MethodView):
    def get(self):
        return flask.render_template('bySchool.html')

class AllProjects(flask.views.MethodView):
    def get(self):
        return flask.render_template('allprojects.html')

class View(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        #Sarah helped to set up return flask.render_template 6/25/12
        phases = p.get_project_phases('Construction')
        return flask.render_template('index.html',
                                     prjs=p.get_project_phases('Construction'),
                                     years=p.get_years(),
                                     orgs=p.get_orgs('AIA'),
                                     num_ppl=p.get_num_ppl(20),
                                     tools=p.get_tools())
        
    
app.add_url_rule('/allprojects', view_func=AllProjects.as_view('allprojects'), methods=['GET'])
app.add_url_rule('/bySchool', view_func=bySchool.as_view('bySchool'), methods=['GET'])
app.add_url_rule('/', view_func=View.as_view('index'), methods=['GET'])

app.debug = True
app.run()
