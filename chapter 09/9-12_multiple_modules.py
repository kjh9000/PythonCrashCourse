#!/usr/bin/python3

""" Store the User class in one module, and store the
Privileges and Admin classes in a separate module In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly """

import user_mod, admin_priviledges_mod

bob = admin_priviledges_mod.Admin('bob', 100, 'rocket scientist')
bob.priviledges.show_priviledges()

