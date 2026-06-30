class NormanInterface:
    def __init__(self, bus, command_engine):
        self.bus = bus
        self.command_engine = command_engine

    def start(self):
        print("💬 Talk to Norman below:\n")

        while True:
            try:
                text = input("You ➜ ")

                if not text.strip():
                    continue

                self.command_engine.handle(text)

            except KeyboardInterrupt:
                print("\n\n👋 Norman shutting down. See you later.")
                break