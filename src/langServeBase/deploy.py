from fastapi import FastAPI
from langserve import add_routes
#from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

###
#def ourRunnable(input_data):
#    return {"output": input_data["input"] * 2} 


runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    extra=RunnablePassthrough.assign(output=lambda x: x["input"] * 3),
    modified=lambda x: x["input"] + 1,
)

app = FastAPI()
 
#add_routes(app, RunnableLambda(
#    ourRunnable
#))
add_routes(app, runnable)
