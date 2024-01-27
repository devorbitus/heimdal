
import time

from src.state import BaseState

class Nodes():
	def __init__(self):
		self.foo = 'bar'

    ### This our test node ... i.e. testing the langgraph implementation
	### We want to change state specifically the service_account_name
	def setAccountName(self, state):
		print("# Setting account name")
		
		state['service_account_name'] = "test"

		return {
			**state,
			"service_account_name": "test"
		}

	def wait_next_run(self, state):
		print("## Waiting for 180 seconds")
		time.sleep(1)
		return state
	
	def setAccontNameResponseCondition(self, state: BaseState):
		if state['service_account_name'] == "test":
			print("## TestPassed")
			return "continue"
		else:
			print("## TestFailed")
			return "end"

	def testFailed(self, state):
		print("## from nodes.py Line 75: testFailed")
		
		return state	


	def testPassed(self, state):
		print("## from nodes.py Line 81: testPassed")
		
		return state
