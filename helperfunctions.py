#!/usr/bin/python3

# Contains smaller functions made for trivial tasks, used in the agentselector funciton.

def list_available_agents(list_of_agents):

	list_of_available_agents = []

	for agent in list_of_agents:

		if agent.is_available == True:

			list_of_available_agents.append(agent)

	return list_of_available_agents



def roles_matcher(issueobject, agentobject):
	
	set_of_issue_roles = set(issueobject.roles)

	set_of_agent_roles = set(agentobject.roles)

	list_of_difference = list(set_of_issue_roles - set_of_agent_roles)

	if len ( list_of_difference ) == 0 :
		return True 
	else:
		return False 



def find_least_busy(list_of_agents):

	list_of_available_agents = list_available_agents(list_of_agents)

	list_of_least_busy_agents = sorted(list_of_available_agents, key=lambda x: x.available_since)

	return list_of_least_busy_agents