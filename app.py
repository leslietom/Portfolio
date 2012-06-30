##This comes from YouTube tutorial.

import flask, flask.views
from model.portfolio_model import DataController

        ##phases = p.get_allproject_ids(project_id = id_filter)
        ##Leslie: to get this to work like how i did in View class. -- get project_id. Filter function for phases in project_id.
        #phases = p.get_project(project_id)

#Leslie trying to add a project class - so she can run a new URL rule.
class Project(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        
        project_id_filter = flask.request.args.get('project_id', None)
        
        project_phases = p.get_project_phases(project_id=project_id_filter)
        
        return flask.render_template('project.html',
                                     phases=project_phases)


#This comes from class DataController methods.
class AllProjects(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        allprojects = p.get_all_projects()
        return flask.render_template('allprojects.html',
                                     prjs=allprojects,
                                     years=p.get_years(),
                                     #Leslie added a_year to access year?
                                     a_year=p.get_a_year(),
                                     orgs=p.get_orgs(),
                                     num_ppl=p.get_num_ppl(),
                                     tools=p.get_tools(),
                                     places=p.get_places(),
                                     image_urls=p.get_image_urls())

class RootFilter(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        
        #This is Flask's get request.
        org_filter = flask.request.args.get('org', None)
        year_filter = flask.request.args.get('year', None)
        people_filter = flask.request.args.get('num_people', None)
        place_filter = flask.request.args.get('place', None)
        tool_filter = flask.request.args.get('tool', None)
        image_urls_filter = flask.request.args.get('image_url', None)
        
        projects = p.get_construction_projects(org=org_filter, year=year_filter, num_people=people_filter, place=place_filter, tool=tool_filter, image_url=image_urls_filter)
        
        #Sarah helped to set up return flask.render_template 6/25/12
        return flask.render_template('index.html',
                                     prjs=projects,
                                     orgs=p.get_orgs(),
                                     years=p.get_years(),
                                     people=p.get_num_ppl(),
                                     places=p.get_places(),
                                     tools=p.get_tools(),
                                     image_urls=p.get_image_urls(),
                                     selected_org=org_filter,
                                     selected_year=year_filter,
                                     selected_num_people=people_filter,
                                     selected_place=place_filter,
                                     selected_tool=tool_filter)

portfolio_app = flask.Flask(__name__)

portfolio_app.add_url_rule('/', view_func=RootFilter.as_view('main'), methods=['GET'])
portfolio_app.add_url_rule('/project', view_func=Project.as_view('project'), methods=['GET'])

#This is how you create more web pages / templates.
portfolio_app.add_url_rule('/allprojects', view_func=AllProjects.as_view('allprojects'), methods=['GET'])

portfolio_app.debug = True
portfolio_app.run(host="localhost", port=5000)
