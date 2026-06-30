class MotionModule:
    def __init__(self, bus, state):
        self.bus = bus
        self.state = state

        bus.subscribe("execute_task", self.execute)

    def execute(self, task):
        action = task.get("action")

        if action == "move_forward":
            self.move_forward()

        elif action == "stop":
            self.stop()

    def move_forward(self):
        print("🤖 Motion: moving forward")
        self.state.motion_active = True

    def stop(self):
        print("🛑 Motion: stopped")
        self.state.motion_active = False