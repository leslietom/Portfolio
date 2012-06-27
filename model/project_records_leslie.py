#!/usr/bin/env python

__author__ = 'Leslie Tom'
__email__ = 'leslie.tom@gmail.com'
__python_version__ = '3.2.3'

from portfolio_model import DataController

if __name__ == '__main__':
    #p = ProjectLibrary()
    p = DataController()
    p.read_file()
    
    
    print('\n\nPrints portfolio - a test:')

    my_organization_name_projects = p.get_orgs('AIA')
    p.print_titles(my_organization_name_projects)

    my_construction_projects = p.get_project_phases('Construction')
    p.print_titles(my_construction_projects)
    
    #cannot get string year to print
    #my_project_years = p.get_years('2011')
    #p.print_titles(my_project_years)
    

    input('Press enter to continue...')