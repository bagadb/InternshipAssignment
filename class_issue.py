#!/usr/bin/python3

from class_roles import list_of_roles

# This file defines the issue class and generates a test list
# for testing and output verification.

class IssueClass:

	def __init__(self, issue_number, roles):

		self.issue_number = issue_number
		self.roles = roles


# IssueNo. IssueRoles
# 1 	 ['Management', 'Support', 'Software']
# 2 	 ['Sales', 'Software', 'Support']
# 3 	 ['Hardware']
# 4 	 ['Software', 'Management']
# 5 	 ['Sales', 'Support']
# 6 	 ['Software']
# 7 	 ['Sales']
# 8 	 ['Support']
# 9 	 ['Hardware', 'Sales', 'Software']
# 10 	 ['Software', 'Hardware']
# 11 	 ['Management']

list_of_issues = [

	IssueClass(1, [ list_of_roles[4], list_of_roles[0], list_of_roles[2] ] ),

	IssueClass(2, [ list_of_roles[1], list_of_roles[2], list_of_roles[0] ] ),

	IssueClass(3, [ list_of_roles[3] ]),

	IssueClass(4, [ list_of_roles[2], list_of_roles[4] ]),

	IssueClass(5, [ list_of_roles[1], list_of_roles[0] ]),

	IssueClass(6, [ list_of_roles[2] ]),

	IssueClass(7, [ list_of_roles[1] ]),

	IssueClass(8, [ list_of_roles[0] ]),

	IssueClass(9, [ list_of_roles[3], list_of_roles[1], list_of_roles[2] ]),

	IssueClass(10, [ list_of_roles[2] , list_of_roles[3] ]),

	IssueClass(11, [ list_of_roles[4] ])

]