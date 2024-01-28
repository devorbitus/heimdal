from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def modify_input(input_data):
    print("input_data")
    print(input_data)
    input_data['output'] = int(input_data.get('input', 0)) * 3
    return input_data

runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    extra=RunnablePassthrough(),
    modified=modify_input,
)

app = FastAPI()
add_routes(app, runnable)