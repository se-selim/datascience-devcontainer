import hashlib
import json
import os

USERS_FILE = "users.json"
TASKS_DIR = "tasks"


def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_tasks_file(username):
    os.makedirs(TASKS_DIR, exist_ok=True)
    return os.path.join(TASKS_DIR, f"{username}.json")


# ---------- Authentication ----------

def register():
    users = load_json(USERS_FILE)
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return None
    password = input("Choose a password: ").strip()
    users[username] = hash_password(password)
    save_json(USERS_FILE, users)
    print("Registration successful.")
    return username


def login():
    users = load_json(USERS_FILE)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if users.get(username) == hash_password(password):
        print(f"Welcome back, {username}!")
        return username
    print("Invalid username or password.")
    return None


# ---------- Task Functions ----------

def load_tasks(username):
    data = load_json(get_tasks_file(username))
    return data.get("tasks", [])


def save_tasks(username, tasks):
    save_json(get_tasks_file(username), {"tasks": tasks})


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(username):
    tasks = load_tasks(username)
    description = input("Task description: ").strip()
    task = {"id": next_id(tasks), "description": description, "status": "Pending"}
    tasks.append(task)
    save_tasks(username, tasks)
    print(f"Task {task['id']} added.")


def view_tasks(username):
    tasks = load_tasks(username)
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"  [{t['id']}] {t['description']} - {t['status']}")


def mark_completed(username):
    tasks = load_tasks(username)
    view_tasks(username)
    task_id = int(input("Enter task ID to mark completed: "))
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Completed"
            save_tasks(username, tasks)
            print(f"Task {task_id} marked as Completed.")
            return
    print("Task not found.")


def delete_task(username):
    tasks = load_tasks(username)
    view_tasks(username)
    task_id = int(input("Enter task ID to delete: "))
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found.")
        return
    save_tasks(username, new_tasks)
    print(f"Task {task_id} deleted.")


# ---------- Menus ----------

def task_menu(username):
    while True:
        print(f"\n--- Task Manager ({username}) ---")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                task_menu(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()