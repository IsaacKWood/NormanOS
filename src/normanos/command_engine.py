class CommandEngine:
    def __init__(self, bus, state, task_manager):
        self.bus = bus
        self.state = state
        self.task_manager = task_manager

    def handle(self, text: str):
        cmd = text.strip().lower()

        # ---------------- SYSTEM COMMANDS ----------------

        if cmd == "tasks":
            print("\n📋 Task Queue")
            print("--------------------")

            tasks = self.task_manager.get_tasks()

            if not tasks:
                print("No tasks.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task['type']}")

            print("--------------------\n")
            return True

        if cmd == "status":
            print("\n📊 Norman System Status")
            print("------------------------")
            print(f"✔ Running: {self.state.running}")
            print(f"🤖 Motion Active: {self.state.motion_active}")
            print(f"📌 Tasks: {self.state.task_count}")
            print(f"🧠 Memory Entries: {self.state.memory_count}")
            print("------------------------\n")
            return True

        if cmd == "help":
            print("\n🧠 Commands:")
            print("- status")
            print("- tasks")
            print("- help")
            print("- shutdown")
            print("- natural language (e.g. move forward)")
            print()
            return True

        if cmd == "shutdown":
            print("🛑 Shutting down Norman...")
            exit()

        # ---------------- IMPORTANT FIX ----------------
        # NOT a system command → send to AI pipeline

        self.bus.publish("command", text)
        return True