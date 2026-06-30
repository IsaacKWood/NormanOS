class IntentEngine:
    def __init__(self, bus):
        self.bus = bus
        bus.subscribe("command", self.process)

    def process(self, text):
        text = text.strip().lower()

        print("\n🧠 INTENT TRIGGERED")

        intent = {
            "actions": self.parse(text)
        }

        print(f"🧠 Intent parsed: {intent}")
        print("🧠 INTENT FORWARDED → BRAIN")

        self.bus.publish("intent", intent)

    def parse(self, text):
        text = text.replace(",", " then ")
        text = text.replace(" and ", " then ")

        parts = [p.strip() for p in text.split("then") if p.strip()]

        actions = []
        for p in parts:
            actions.append(self.normalize(p))

        return actions

    def normalize(self, part):
        part = part.strip()

        if "x3" in part:
            base = part.replace("x3", "").strip()
            return {"base": self.clean(base), "repeat": 3}

        if "x2" in part:
            base = part.replace("x2", "").strip()
            return {"base": self.clean(base), "repeat": 2}

        return {"base": self.clean(part), "repeat": 1}

    def clean(self, text):
        text = text.replace(" ", "_")
        text = text.replace("__", "_")
        return text