class MemoryModule:
    def __init__(self, bus, state):
        self.bus = bus
        self.state = state
        self.memory = []

        bus.subscribe("memory_store", self.store)
        bus.subscribe("memory_recall", self.recall)

    def store(self, data):
        self.memory.append(data)
        self.state.memory_count += 1
        print(f"🧠 Memory stored: {data}")

    def recall(self, _=None):
        print("\n🧠 Memory Dump:")
        for i, item in enumerate(self.memory):
            print(f"{i+1}. {item}")
        print()