#!/usr/bin/python3

from class_roles import list_of_roles
from datetime import datetime, timedelta

# This file contains the Agent class and a test list of agents for 
# testing and output verification.
# 
# I have used datetime objects to set "available_since" and set it to random intervals for testing purposes.


class AgentClass:

	def __init__(self, name, is_available, available_since, roles):

		self.name = name
		self.is_available = is_available
		self.available_since = available_since
		self.roles = roles

current_instant = datetime.today()

# Akash | Avalibility: True | Available Since: 2020-06-23 23:38:47.302758 | Roles: ['Management', 'Support', 'Software'] |
# 
# Shreyas | Avalibility: True | Available Since: 2020-06-23 23:08:47.302758 | Roles: ['Sales', 'Support'] |
# 
# Abhishek | Avalibility: False | Available Since: None | Roles: ['Software'] |
# 
# Pooja | Avalibility: True | Available Since: 2020-06-23 22:38:47.302758 | Roles: ['Software'] |
# 
# Nikhil | Avalibility: False | Available Since: None | Roles: ['Support'] |
# 
# Onkar | Avalibility: True | Available Since: 2020-06-23 23:08:47.302758 | Roles: ['Hardware'] |
# 
# Priya | Avalibility: False | Available Since: None | Roles: ['Sales', 'Software', 'Support'] |
# 
# Aishwarya | Avalibility: False | Available Since: None | Roles: ['Software', 'Hardware'] |
# 
# Malvika | Avalibility: True | Available Since: 2020-06-23 22:08:47.302758 | Roles: ['Software', 'Hardware'] |
# 
# Kunal | Avalibility: True | Available Since: 2020-06-24 00:08:47.302758 | Roles: ['Sales'] |

list_of_agents = [

	AgentClass("Akash", True, ( current_instant - timedelta(hours=1.5)), [ list_of_roles[4], list_of_roles[0], list_of_roles[2] ] ), #Available since 1.5 hours

	AgentClass("Shreyas", True, ( current_instant - timedelta(hours=2) ), [ list_of_roles[1], list_of_roles[0] ] ), #Available since 2 hours 

	AgentClass("Abhishek", False, None, [ list_of_roles[2] ] ), #Not available

	AgentClass("Pooja", True, ( current_instant - timedelta(hours=2.5)), [ list_of_roles[2] ] ), #Not available

	AgentClass("Nikhil", False, None, [ list_of_roles[0] ] ), #Not available

	AgentClass("Onkar", True, ( current_instant - timedelta(hours=2) ), [ list_of_roles[3] ] ), #Available since 2 hours 

	AgentClass("Priya", False, None, [ list_of_roles[1], list_of_roles[2], list_of_roles[0] ] ), #Not available

	AgentClass("Aishwarya", False, None, [ list_of_roles[2] , list_of_roles[3] ] ), #Not available

	AgentClass("Malvika", True, ( current_instant - timedelta(hours=3) ), [ list_of_roles[2] , list_of_roles[3] ] ), #Available since 3 hours 

	AgentClass("Kunal", True, ( current_instant - timedelta(hours=1) ), [ list_of_roles[1] ] ) #Available since 1 hours 

]

