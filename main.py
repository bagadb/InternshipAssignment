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

from datetime import datetime, timedelta
import random

# Following is the agentselector function requested in the problem statement.
# Running this file will easily give you all the output for step by step verification

def agentselector(list_of_agents, selection_mode, issue):

	eligible_agents_list = []

	for agent in list_of_agents:
		if roles_matcher(issue,agent) == True & agent.is_available == True:
			eligible_agents_list.append(agent)

	if selection_mode == "all_available":
		
		return eligible_agents_list 
	# List of all eligible agents are returned as we want to present the issue to all agents.
		pass


	if selection_mode == "least_busy":

		least_busy_list = find_least_busy(eligible_agents_list)
		
		if len(least_busy_list) > 0:
			return least_busy_list[0]
		pass


	if selection_mode == "random":

		if len( eligible_agents_list) > 0:
			return random.choice( eligible_agents_list )
		pass

def main():

	current_time = datetime.today()

	print( "Current time is", current_time )

	print( "\nThis is a simple program to help you verify the output!")
	
	print( "\nYou will be shown the Agents and Issues first!")

	input("Press Enter to Continue!")

	view_all_agents_and_issues()

	input("Press Enter to Continue!")

	print("\n\nOnly the available agents can be allocated with issues, Hence the available agents are.....")

	view_all_available_agents()

	input("Press Enter to Continue!")

	print("\nNow a list of all agents assigned to the issues in the mode ALL AVAILABLE will be shown!\n")

	for issue in list_of_issues:
		print(issue.issue_number,end = ": ")
		for agent in agentselector(list_of_agents, 'all_available', issue):
			print(agent.name,end = " ")
		print("")

	input("Press Enter to Continue!")

	print("\nNow a list of all agents assigned to the issues in the mode LEAST BUSY will be shown!")

	for issue in list_of_issues:
		agent = agentselector(list_of_agents, 'least_busy', issue)
		if agent :
			print(issue.issue_number,": ", agent.name)
		
	input("Press Enter to Continue!")

	print("\nNow a list of all agents assigned to the issues in the mode RANDOM will be shown!")

	for issue in list_of_issues:
		agent = agentselector(list_of_agents, 'random', issue)
		if agent :
			print(issue.issue_number,": ", agent.name)
	
	input("Press Enter to Continue!")

	print("\nHope you like the output! The output is also saved in a text file for convenience")

	print("\nCode is carefully arranged and commented for readablity. I hope you give me an opportunity to work with you!")
	return

if __name__ == '__main__':
	main()