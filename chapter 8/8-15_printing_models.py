#!/usr/bin/python3

import print_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models.print_models(unprinted_designs, completed_models)
print_models.show_completed_models(completed_models)
