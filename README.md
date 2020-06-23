# InternshipAssignment
This is an assignment performed to apply for an Internship at SupportGenie.

Run main.py using python3 for easy output verification.

The function of interest is present in main.py itself. The main.py file is carefully commented 
for easier navigation of code and readability.

The output.txt is also given for easier output verification.It has all the 
generated data and the outcomes of the functions in all modes. 

I hope you like my solution and I am looking forward for this opportunity.


The problem statement:

Exercise 2
Agent selector
You are given the following data for agents 
agent
    • is_available
    • available_since (the time since the agent is available)
    • roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Please write a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.
