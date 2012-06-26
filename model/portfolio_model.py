#!/usr/bin/env python

__author__ = 'Leslie Tom'
__email__ = 'leslie.tom@gmail.com'
__python_version__ = '3.2.3'

from datetime import datetime

class Project:
    def __init__(self, line):
        #print(line)
        cells= line.split(',')
        #calling organization_category "Project"
        self.organization_category = cells[0] 
        self.project_title = cells[1]
        self.project_description = cells[2]
        self.start_date = cells[3] ##need to change into a date object -- and is there a way to parse through and have project print for each year?
        self.end_date = cells[4] ##need to change into a date object
        self.tools = cells[5]
        self.num_of_people_experienced = cells[6]
        self.places = cells[7]
        self.phase_name = cells[8].strip()
        
    def clean_string(self, cells, index):
        try:
            return cells[index].strip().replace('"', '')
        except:
            return ''

class DataController:
    def __init__(self):
        self.projects = []
    
    def read_file(self, file_name='/Users/leslietom/Dropbox/iSchool Berkeley/i206summer/i206_Final Project/website/static/data/2012portfolio_leslie2.csv'):
        '''
        Reads a file and populates self.projects with a list of Project objects
        '''
        f = open(file_name)
        for line in f.readlines()[1:]:
            self.projects.append(Project(line))
            
    def get_project_phases(self, phase):
        projects = []
        for project in self.projects:
            #print(project.phase_name)
            if project.phase_name == phase:
                projects.append(project)
        return projects
    
    def get_years(self):
        return [2004, 2006, 2008]
        
    def get_orgs(self):
        return ['Org 1', 'Org 2', 'Org 3']
    
    def get_num_ppl(self):
        return [2, 6, 4, 7].sort()
    
    def get_tools(self):
        return ['Photoshop', 'Word']
            
    def print_phases(self, projects):
        '''
        Prints out a list of project phases only
        '''
        for project in projects:
            print(project.project_title)
                

p = DataController()
p.read_file()
