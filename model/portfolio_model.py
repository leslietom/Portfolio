#!/usr/bin/env python

__author__ = 'Leslie Tom'
__email__ = 'leslie.tom@gmail.com'
__python_version__ = '3.2.3'

from datetime import datetime

class Project:
    def __init__(self, line):
        cells= line.split(',')
        #calling organization_category "Project"
        self.organization_category = cells[0] 
        self.project_title = cells[1]
        self.project_description = cells[2]
        self.start_date = self.parse_date(cells[3]) ##need to change into a date object -- and is there a way to parse through and have project print for each year?
        self.end_date = self.parse_date(cells[4]) ##need to change into a date object
        self.tools = cells[5]
        self.num_of_people_experienced = cells[6]
        self.places = cells[7]
        self.phase_name = cells[8].strip()
        
    def clean_string(self, cells, index):
        try:
            return cells[index].strip().replace('"', '')
        except:
            return ''
        
    def start_year(self):
        return self.start_date.strftime('%Y')
        
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
    def read_file(self, file_name='/Users/leslietom/Dropbox/iSchool Berkeley/i206summer/i206_Final Project/website/static/data/2012portfolio_leslie2.csv'):
        '''
        Reads a file and populates self.projects with a list of Project objects
        '''
        f = open(file_name)
        for line in f.readlines()[1:]:
            print(line)
            self.projects.append(Project(line))
        f.close()

    def get_all_projects(self):
        '''
        Returns a list of projects where the phase name matches. This also tells which resource initially shows.
        '''
        return self.projects
    
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

    def get_projects(self, org=None, phase='Construction', year=None, num_people=None):
        '''
        Returns a list of projects where the phase name matches. This also tells which resource initially shows.
        '''
        projects = []
        for project in self.projects:
            #print(project.phase_name)
            #if (project.phase_name == phase and
            if ((org is None or project.organization_category == org) and
                (year is None or project.start_year() == year) and
                (num_people is None or project.num_of_people_experienced == num_people)):
                projects.append(project)
        return projects
        
    def get_years(self):
        years = set()
        for project in self.projects:
            years.add(project.output_year(project.start_date))
            years.add(project.output_year(project.end_date))#for set
        years = list(years)
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
    
    def get_tools(self):
        return ['Photoshop', 'Word']
            
    def print_titles(self, projects):
        '''
        Prints out a list of project titles
        '''
        for project in projects:
            print(project.project_title)
                

#p = DataController()
#p.read_file()
#print(p.projects)
