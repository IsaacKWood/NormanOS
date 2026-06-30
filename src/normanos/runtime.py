import time

class RobotRuntime:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def start(self):

        while True:
            task = self.task_manager.pop_task()

            if task:
                self.execute(task)

            time.sleep(0.1)

    def execute(self, task):
        task_type = task.get("type", "")

        # safety cleanup
        task_type = task_type.strip().strip("_")

        print(f"⚙️ Executing: {task_type}")

        if task_type == "move_forward":
            self.move_forward()

        elif task_type == "stop":
            self.stop()

        else:
            print(f"⚠️ Unknown task: {task_type}")

    def move_forward(self):
        print("➡️ Moving forward")

    def stop(self):
        print("🛑 Stopping")