#!/usr/bin/env python

__author__ = 'Leslie Tom'
__email__ = 'leslie.tom@gmail.com'
__python_version__ = '3.2.3'

from datetime import datetime

class Project:
    def __init__(self, line):
        '''
        Instantiates all the variables from the lines read in from the csv file.
        '''
        cells= line.split(',')
        #calling organization_category "Project"
        self.organization_category = cells[0] 
        self.project_title = cells[1]
        self.project_description = cells[2]
        self.start_date = self.parse_date(cells[3]) ##need to change into a date object -- and is there a way to parse through and have project print for each year?
        self.end_date = self.parse_date(cells[4]) ##need to change into a date object
        self.tools = self.clean_string_colon(cells, 5)
        self.num_of_people_experienced = cells[6]
        self.places = cells[7]
        self.phase_name = cells[8].strip()
        self.fullproject_title = cells[9]
        self.image_urls = cells[10]
        self.organization_names = cells[11]
        self.about = cells[12]
        self.project_id = cells[13]
    
    #Leslie experimented with this def. This takes out the ":" -- but does not split apart the cells. (split() does not work) - 2 arguements needed
    def clean_string_colon(self, cells, index):
        try:
            return cells[index].strip().replace(':', '')
        except:
            return ''
    
    #Sarah helped me make a start_year to plug into get_project method
    def start_year(self):
        return self.start_date.strftime('%Y')
        
    def end_year(self):
        return self.end_date.strftime('Y')
        
    #Sarah helped me make parse date and Output year methods.
    def parse_date(self, date_string):
        '''
        Changes start_date and end_date to date objects
        '''
        mydate = datetime.strptime(date_string, '%m/%d/%Y') #11/13/2011
        return mydate
    
    def output_year(self, mydate):
        return mydate.strftime('%Y')
        

class DataController:
    def __init__(self):
        self.projects = []
    
    #Sarah helped me find the file directory path and worked on cleaning up my csv data from using Excel and spliting on ';'
    def read_file(self, file_name='/Users/leslietom/Dropbox/iSchool Berkeley/i206summer/i206_Final Project/website/static/data/2012portfolio_leslie1.csv'):
        '''
        Reads a file and populates self.projects with a list of Project objects
        '''
        f = open(file_name)
        for line in f.readlines()[1:]:
            print(line)
            self.projects.append(Project(line))
        f.close()

    #Worked with Sarah 6/27/12 to help get all projects.
    def get_all_projects(self):
        '''
        Returns a list of all projects.
        '''
        return self.projects
    
    #Leslie tried to just get the 'construction' phase to show for the main page. Still in progress - to be tied into index.
    def get_project_phases(self, phase):
        '''
        Returns a list of projects where the phase name matches. This also tells which resource initially shows.
        '''
        projects = []
        for project in self.projects:
            #print(project.phase_name)
            if project.phase_name == phase:
                projects.append(project)
        return projects

    #Sarah helped to start - a method that passes everything. 6/27/12
    def get_projects(self, org=None, phase=None, year=None, num_people=None, place=None, tool=None, image_url=None):
        '''
        Returns a list of all projects. This also tells which resource initially shows.
        '''
        projects = []
        for project in self.projects:
            #comment out hard coded phase name.  To be put in when more projects populate csv list. 
            #if (project.phase_name == phase and
            if ((org is None or project.organization_category == org) and
                (year is None or project.start_year() == year) and
                (num_people is None or project.num_of_people_experienced == num_people) and
                (place is None or project.places == place) and
                (tool is None or project.tools == tool) and
                (image_url is None or project.image_urls == image_url)):
                projects.append(project)
        return projects
    
    #Leslie tried to just get the 'construction' phase to show for the main page. Still in progress - to be tied into index.
    def get_final_projects(self, org=None, phase='Construction', year=None, num_people=None, place=None, tool=None, image_url=None):
        '''
        Returns a list of projects where the phase name matches. 
        '''
        projects = []
        for project in self.projects:
            #comment out hard coded phase name.  To be put in when more projects populate csv list. 
            if (project.phase_name == phase and
                (org is None or project.organization_category == org) and
                (year is None or project.start_year() == year) and
                (num_people is None or project.num_of_people_experienced == num_people) and
                (place is None or project.places == place) and
                (tool is None or project.tools == tool) and
                (image_url is None or project.image_urls == image_urls)):
                projects.append(project)
        return projects
    
    #Using this method to return all project id's to group projects.
    def get_allproject_ids(self, project_id=None):
        '''
        Returns a list of project ids. 
        '''
        projects = []
        for project in self.projects:
            if project.project_id == project_id:
                projects.append(project)
        return projects
        
    #This method may return blank output on base.HTML page because did not tie end dates into HTML.
    def get_years(self):
        '''
        Returns a unique list of all start and end dates.
        '''
        #create a set to get all unique values.
        years = set()
        for project in self.projects:
            years.add(project.output_year(project.start_date))
            years.add(project.output_year(project.end_date))
        #turn set into a list
        years = list(years)
        #have the most recent years printed out first.
        years.sort(reverse=True) 
        return years
        
    def get_orgs(self):
        '''
        Returns a list of projects where the get organizations matches.  This is called projects in HTML.
        '''
        organizations = set()
        for project in self.projects:
            organizations.add(project.organization_category) #for set
        organizations = list(organizations)
        organizations.sort()
        return organizations
    
    def get_num_ppl(self):
        '''
        Returns a list of projects where the number of people experienced matches.
        '''
        people = set()
        for project in self.projects:
            people.add(project.num_of_people_experienced) 
        people = list(people)
        people.sort()
        return people
    
    def get_places(self):
        '''
        Returns a list of project locations / places.
        '''
        places = set()
        for project in self.projects:
            places.add(project.places) 
        places = list(places)
        places.sort()
        return places
    
    def get_tools(self):
        '''
        Returns a list of tools used.
        '''
        tools = set()
        for project in self.projects:
            tools.add(project.tools) #for set
        tools = list(tools)
        tools.sort()
        return tools
            
    def get_image_urls(self):
        '''
        Returns a list of urls images from Flickr
        '''
        image_urls = set()
        for project in self.projects:
            image_urls.add(project.image_urls)
            image_urls = list(image_urls)
            image_urls.sort()
            return image_urls
