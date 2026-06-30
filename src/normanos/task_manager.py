class TaskManager:
    def __init__(self, bus, state):
        self.bus = bus
        self.state = state
        self.tasks = []

        bus.subscribe("task", self.add_task)

    def add_task(self, task):
        # HARD SAFETY: prevent nested wrapping
        if isinstance(task.get("type"), dict):
            task = task["type"]

        self.tasks.append(task)
        self.state.task_count += 1

        print(f"📥 TASK STORED: {task}")

    def get_tasks(self):
        return self.tasks

    def pop_task(self):
        if not self.tasks:
            return None
        return self.tasks.pop(0)