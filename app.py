##This comes from YouTube tutorial.

import flask, flask.views
from model.portfolio_model import DataController
app = flask.Flask(__name__)

#class View(flask.views.MethodView):
#    def get(self):
#        return 'Hello There!'

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
        
    
app.add_url_rule('/', view_func=View.as_view('Main'), methods=['GET'])

app.debug = True
app.run()