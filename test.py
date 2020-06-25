#!/usr/bin/python3

from class_agent import AgentClass, list_of_agents 
#This file contains the Agents List and the Class Declaration. You can change roles and the agent list here.

from class_issue import IssueClass, list_of_issues
#This file contains the Issues List and the Class Declaration. You can change roles and the issues list here.

#The roles are defined in a list inside class_roles.py

from helperfunctions import list_available_agents, roles_matcher, find_least_busy
#This file contains the above functions used in the Agent Selector Function.

from displayfunctions import *
#This file contains the functions used to format and display sample data.

from main import agentselector

from datetime import datetime, timedelta
import random

import unittest

class TestAllFunctions(unittest.TestCase):

	def test_roles_matcher(self):

		self.assertFalse(roles_matcher(list_of_issues[2],list_of_agents[0]))

		self.assertTrue(roles_matcher(list_of_issues[0],list_of_agents[0]))

		self.assertTrue(roles_matcher(list_of_issues[3],list_of_agents[0]))

		print("Roles Matcher OK!\n")

		return

	
	def test_list_available(self):

		names = []

		for agent in list_available_agents(list_of_agents):
			names.append(agent.name)

		self.assertEqual(names, ['Akash', 'Shreyas', 'Pooja', 'Onkar', 'Malvika', 'Kunal' ])

		print("list_available_agents OK!\n")
		
		return

	
	def test_find_least_busy(self):
		
		names = []

		for agent in find_least_busy(list_of_agents):
			names.append(agent.name)

		self.assertEqual(names,['Malvika', 'Pooja', 'Shreyas', 'Onkar', 'Akash', 'Kunal'])
		
		print("find_least_busy OK!\n")

		return

	
	def test_agentselector(self):

		outputlist= []

		for agent in agentselector(list_of_agents, 'all_available', list_of_issues[5]):
			outputlist.append(agent.name)

		self.assertEqual(outputlist, ['Akash', 'Pooja', 'Malvika'])

		output = agentselector(list_of_agents, 'least_busy', list_of_issues[5])

		self.assertEqual(output.name,'Malvika')

		print('agentselector OK!')

		return

if __name__ == '__main__':
    unittest.main()