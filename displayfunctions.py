#!/usr/bin/python3

from class_agent import AgentClass, list_of_agents
from class_issue import IssueClass, list_of_issues

def view_all_issues():

	print("----------------------------------------------------------------------------------------------")

	print("Following is the queue of issues")

	print("----------------------------------------------------------------------------------------------")

	print("IssueNo. IssueRoles")

	for issue in list_of_issues:
		print(issue.issue_number,"\t",issue.roles)
	
	print("----------------------------------------------------------------------------------------------")

	
	return None

def view_all_agents():

	print("----------------------------------------------------------------------------------------------")

	print("Following is the test list of all agents and their attributes")

	print("----------------------------------------------------------------------------------------------")

	for agent in list_of_agents:
		print(agent.name, "| Avalibility:", agent.is_available, "| Available Since:", agent.available_since, "| Roles:", agent.roles, "|\n")

	print("----------------------------------------------------------------------------------------------")

	print("Following is the queue of issues")

	print("----------------------------------------------------------------------------------------------")

	return None

def view_all_available_agents():

	print("----------------------------------------------------------------------------------------------")

	print("Following is the test list of available agents and their attributes")

	print("----------------------------------------------------------------------------------------------")

	for agent in list_of_agents:
		if agent.is_available == True:
			print(agent.name, "| Avalibility:", agent.is_available, "| Available Since:", agent.available_since, "| Roles:", agent.roles, "|\n")

	print("----------------------------------------------------------------------------------------------")

	return None

def view_all_agents_and_issues():

	print("----------------------------------------------------------------------------------------------")

	for agent in list_of_agents:
		print(agent.name, "| Avalibility:", agent.is_available, "| Available Since:", agent.available_since, "| Roles:", agent.roles, "|\n")

	print("----------------------------------------------------------------------------------------------")

	print("Following is the queue of issues")

	print("----------------------------------------------------------------------------------------------")

	print("IssueNo. IssueRoles")

	for issue in list_of_issues:
		print(issue.issue_number,"\t",issue.roles)
	
	print("----------------------------------------------------------------------------------------------")

	return None

def show_menu1():
	print("1. View Data\n2. Verify Output\n3. Exit\n")

def show_menu11():
	print("1. View all agents and issues\n2. View all Agents\n3. View all issues\n4. Back")

def show_menu12():
	print("1. Send issue to function and see agent allocation\n2. Back")

def show_menu121():
	print("1. All Available\n2. Least Busy\n3. Random\n4. Back")

