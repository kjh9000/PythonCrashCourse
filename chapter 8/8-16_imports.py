#!/usr/bin/python3
'''
store a function in a separate file and import it in a main file.
use:
import print_models
from print_models import print_models
from print_models print_models as pm, show_completed_models as scm 
import print_models as pm
from print_models import *


#version 1
import print_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models.print_models(unprinted_designs, completed_models)
print_models.show_completed_models(completed_models)


#version 2
from print_models import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


#version 3
from print_models import print_models as pm, show_completed_models as scm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
scm(completed_models)


#version 4
import print_models as pm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)
'''
#version 5
from print_models import *
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

