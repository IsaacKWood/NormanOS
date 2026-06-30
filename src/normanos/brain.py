class BrainModule:
    def __init__(self, bus, planner):
        self.bus = bus
        self.planner = planner

        bus.subscribe("intent", self.handle)

    def handle(self, intent):
        print(f"🧠 BRAIN INPUT: {intent}")

        plan = self.planner.create_plan(intent)

        print(f"🧠 BRAIN OUTPUT (PLAN): {plan}")

        # IMPORTANT: publish each task once only
        for task in plan:
            self.bus.publish("task", task)
            print("🧠 BRAIN INIT ID:", id(self))