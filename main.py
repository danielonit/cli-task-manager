import typer
import json
import time
import os

app = typer.Typer()

# creates json file if it doesn't exist
def ensure_data_file():
    if not os.path.exists("data.json"):
        with open("data.json", "w") as file:
            json.dump({"tasks": {}}, file)
            json.dump({"next_id": 1}, file)

# creates a time stamp
def create_time():
    local_time = time.localtime()
    return str(time.strftime("%B %d, %Y %I:%M:%S", local_time))

# reads a json file
def read_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)
    
# writes to a json file
def write_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# creates a new task and adds it to the json file
@app.command()
def add(task: str):
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    task_id = data["next_id"]

    tasks[task_id] = {"id": task_id, "description": task, "status": "pending", "created_at": create_time(), "updated_at": "not updated"}

    data["next_id"] += 1

    write_file("data.json", data)
    print(f"Task added successfully (ID: {task_id})")

# updates a task in the json file
@app.command()
def update(id: str, task: str):    
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    tasks[id]["description"] = task

    tasks[id]["updated_at"] = create_time()

    write_file("data.json", data)
    print(f"Task updated: {task}")

# deletes a task from the json file
@app.command()
def delete(id: str):
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    del tasks[id]

    write_file("data.json", data)
    print(f"Task deleted: {id}")

# deletes all tasks from the json file
@app.command("delete-all")
def delete_all():
    ensure_data_file()
    data = read_file("data.json")
    data["tasks"] = {}
    data["next_id"] = 1

    write_file("data.json", data)
    print("All tasks deleted")

# marks a task as to-do
@app.command("mark-to-do")
def mark_to_do(id: str):
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    tasks[id]["status"] = "to-do"
    task = tasks[id]["description"]

    write_file("data.json", data)
    print(f"Task marked to do: {task}")

# marks a task as in-progress
@app.command("mark-in-progress")
def mark_in_progress(id: str):
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    tasks[id]["status"] = "in-progress"
    task = tasks[id]["description"]

    write_file("data.json", data)
    print(f"Task marked in progress: {task}")

# marks a task as done
@app.command("mark-done")
def mark_done(id: str):
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    tasks[id]["status"] = "done"
    task = tasks[id]["description"]

    write_file("data.json", data)
    print(f"Task marked done: {task}")

# lists all tasks
@app.command()
def list():
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        print(f"- {task_id}: {task['description']} ({task['status']})")

@app.command("list-pending")
def list_pending():
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "pending":
            print(f"- {task_id}: {task['description']} ({task['status']})")

# lists all tasks marked as to-do
@app.command("list-to-do")
def list_to_do():
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "to-do":
            print(f"- {task_id}: {task['description']} ({task['status']})")

# lists all tasks marked as in-progress
@app.command("list-in-progress")
def list_in_progress():
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "in-progress":
            print(f"- {task_id}: {task['description']} ({task['status']})")

# lists all tasks marked as done
@app.command("list-done")
def list_done():
    ensure_data_file()
    data = read_file("data.json")
    tasks = data.get("tasks", {})

    for task_id, task in tasks.items():
        if task["status"] == "done":
            print(f"- {task_id}: {task['description']} ({task['status']})")

# shows all available commands
@app.command()
def help():
    print("- add: Add a new task")
    print("- update: Update a task")
    print("- delete: Delete a task")
    print("- delete-all: Delete all tasks")
    print("- mark-to-do: Mark a task as to do")
    print("- mark-in-progress: Mark a task as in progress")
    print("- mark-done: Mark a task as done")
    print("- list: List all tasks")
    print("- list-pending: List all tasks marked as pending")
    print("- list-to-do: List all tasks marked as to do")
    print("- list-in-progress: List all tasks marked as in progress")
    print("- list-done: List all tasks marked as done")


if __name__ == "__main__":
    app()