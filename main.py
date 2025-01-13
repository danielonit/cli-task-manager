import typer
import json
import time
import os

app = typer.Typer()

def ensure_data_file():
    if not os.path.exists("data.json"):
        with open("data.json", "w") as file:
            json.dump({"tasks": {}}, file)

def create_time():
    local_time = time.localtime()
    return str(time.strftime("%B %d, %Y %I:%M:%S", local_time))

@app.command()
def add(task: str):
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})
        
    task_id = len(tasks) + 1

    tasks[task_id] = {"id": task_id, "description": task, "status": "pending", "created_at": create_time(), "updated_at": "not updated"}

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task added successfully (ID: {task_id})")

@app.command()
def update(id: str, task: str):    
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    tasks[id]["description"] = task

    tasks[id]["updated_at"] = create_time()

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task updated: {task}")

@app.command()
def delete(id: str):
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    del tasks[id]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task deleted: {id}")

@app.command("mark-to-do")
def mark_to_do(id: str):
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    tasks[id]["status"] = "to-do"
    task = tasks[id]["description"]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task marked to do: {task}")

@app.command("mark-in-progress")
def mark_in_progress(id: str):
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    tasks[id]["status"] = "in-progress"
    task = tasks[id]["description"]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task marked in progress: {task}")

@app.command("mark-done")
def mark_done(id: str):
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

        tasks[id]["status"] = "done"
        task = tasks[id]["description"]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Task marked done: {task}")

@app.command()
def list():
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        print(f"- {task_id}: {task['description']} ({task['status']})")

@app.command("list-to-do")
def list_to_do():
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "to-do":
            print(f"- {task_id}: {task['description']} ({task['status']})")

@app.command("list-in-progress")
def list_in_progress():
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "in-progress":
            print(f"- {task_id}: {task['description']} ({task['status']})")

@app.command("list-done")
def list_done():
    ensure_data_file()
    with open("data.json", "r") as file:
        data = json.load(file)
        tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "done":
            print(f"- {task_id}: {task['description']} ({task['status']})")


if __name__ == "__main__":
    app()