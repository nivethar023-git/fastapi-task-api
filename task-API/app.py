from task_sdk import TaskClient, TaskAPIError

# Initialize the SDK client
client = TaskClient(
    base_url="http://127.0.0.1:8000",
    api_key="secret123"
)

# 1. Create a task using native Python functions
new_task = client.create_task("Clean room")
print("Created Task:", new_task)

# 2. List all tasks
print("\n--- All Tasks ---")
for task in client.list_tasks():
    print(f"[{task['id']}] {task['title']} - Completed: {task['completed']}")

# 3. Handle errors cleanly
print("\n--- Error Handling ---")
try:
    client.get_task(99)
except TaskAPIError as err:
    print("Caught SDK Error:", err)