#!/usr/bin/python3

"""Start with your work from Exercise 9-8 (page 178)
Store the classes User, Privileges, and Admin in one module Create a separate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly """

import users

bob = users.Admin('bob', 100, 'rocket scientist')
bob.priviledges.show_priviledges()

