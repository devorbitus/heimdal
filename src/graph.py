from dotenv import load_dotenv
load_dotenv()

from langgraph.graph.graph import END

from langgraph.graph import StateGraph

from .state import BaseState
from .nodes import Nodes

class WorkFlow():
	def __init__(self):
		nodes = Nodes()
		workflow = StateGraph(BaseState)

		workflow.add_node("setStateTest", nodes.setAccountName)
		workflow.add_node("testFailed", nodes.testFailed)
		
		workflow.add_node("testPassed", nodes.testPassed)

		workflow.set_entry_point("setStateTest")
		
		workflow.add_conditional_edges(
				"setStateTest",
				nodes.setAccontNameResponseCondition,
				{
					"continue": 'testPassed',
					"end": 'testFailed'
				}
		)
		
		workflow.add_edge('testPassed', END)
		workflow.add_edge('testFailed', END)
		self.app = workflow.compile()

