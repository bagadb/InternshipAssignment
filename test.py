#!/usr/bin/python3

from main import *

for agent in find_least_busy(list_of_agents):
	print(agent.name, " ", agent.available_since)
