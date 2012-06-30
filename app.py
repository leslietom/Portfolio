##This comes from YouTube tutorial.

import flask, flask.views
from model.portfolio_model import DataController

app = flask.Flask(__name__)

        ##phases = p.get_allproject_ids(project_id = id_filter)
        ##Leslie: to get this to work like how i did in View class. -- get project_id. Filter function for phases in project_id.
        #phases = p.get_project(project_id)

#Leslie trying to add a project class - so she can run a new URL rule.
class project(flask.views.MethodView):
    def get(self):
        p = DataController()
        p.read_file()
        project = p.get_all_projects()
        return flask.render_template('project.html', prjs=project, prgs=p.get_orgs(), image_urls=p.get_image_urls())


#This comes from class DataController methods.
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
                                     places=p.get_places(),
                                     image_urls=p.get_image_urls())

class View(flask.views.MethodView):
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
        
        projects = p.get_projects(org=org_filter, year=year_filter, num_people=people_filter, place=place_filter, tool=tool_filter, image_url=image_urls_filter)
        
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
        
#Trying to add another project web page.
app.add_url_rule('/project', view_func=project.as_view('project'), methods=['GET'])
app.add_url_rule('/bySchool', view_func=project.as_view('bySchool'), methods=['GET'])

#This is how you create more web pages / templates.    
app.add_url_rule('/allprojects', view_func=AllProjects.as_view('allprojects'), methods=['GET'])
app.add_url_rule('/', view_func=View.as_view('index'), methods=['GET'])


app.debug = True
app.run()
