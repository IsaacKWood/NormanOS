class PlanningEngine:
    def create_plan(self, intent):
        actions = intent["actions"]

        plan = []

        for action in actions:
            base = action["base"]
            repeat = action["repeat"]

            for _ in range(repeat):
                plan.append({
                    "type": base,
                    "params": {}
                })

        print(f"🧠 BRAIN OUTPUT (PLAN): {plan}")
        return plan