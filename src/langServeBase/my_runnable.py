from langchain_core.runnables import Runnable
#from langchain import Runnable

class MyRunnable(Runnable):
    def run(self, input_data):
        return {"output": input_data["input"] * 2}