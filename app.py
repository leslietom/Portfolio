##This comes from YouTube tutorial.

import flask, flask.views
from model.portfolio_model import DataController
app = flask.Flask(__name__)

#Why can't you take this out? LT.
class bySchool(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

class AllProjects(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        allprojects = p.get_all_projects()
        return flask.render_template('allprojects.html',
                                     prjs=allprojects,
                                     years=p.get_years(),
                                     orgs=p.get_orgs(),
                                     num_ppl=p.get_num_ppl(),
                                     tools=p.get_tools(),
                                     places=p.get_places())

class View(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        org_filter = flask.request.args.get('org', None)
        year_filter = flask.request.args.get('year', None)
        people_filter = flask.request.args.get('num_people', None)
        place_filter = flask.request.args.get('place', None)
        
        projects = p.get_projects(org=org_filter, year=year_filter, num_people=people_filter, place=place_filter)
            
            
        #Sarah helped to set up return flask.render_template 6/25/12
        return flask.render_template('index.html',
                                     prjs=projects,
                                     years=p.get_years(),
                                     orgs=p.get_orgs(),
                                     people=p.get_num_ppl(),
                                     tools=p.get_tools(),
                                     places=p.get_places(),
                                     selected_org=org_filter,
                                     selected_year=year_filter,
                                     selected_num_people=people_filter,
                                     selected_place=place_filter)
        

#This is how you create more web pages / templates.    
app.add_url_rule('/allprojects', view_func=AllProjects.as_view('allprojects'), methods=['GET'])
app.add_url_rule('/bySchool', view_func=bySchool.as_view('bySchool'), methods=['GET'])
app.add_url_rule('/', view_func=View.as_view('index'), methods=['GET'])

app.debug = True
app.run()
