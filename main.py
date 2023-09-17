from typing import Union
from models import ToDo
from fastapi import FastAPI

app = FastAPI()

todos = []
@app.get("/")
def read_root():
    return {"hello": "world"}

# list all  todo
@app.get("/todos")
async def list_todos():
	return {"todos": todos}

# create a todo
@app.post("/todos")
async def create_todos(todo: ToDo):
	todos.append(todo)
	return {"message": "todo is added"}


# update a todo
@app.put("/todos/{todo_id}")
async def update_todos(todo_id: int, todo_obj: ToDo):
	# todos.append(todo)
    for todo in todos:
        print(todo)
        if todo.id == todo_id:
            todo.id = todo.id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "no todo is found to be updated."}

# get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    print(todos)
    for todo in todos:
        print(todo)
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No Todos"}

#  delete todo
@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    print(todos)
    for todo in todos:
        print(todo)
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo has been deleted"}
    return {"message": "No Todos"}