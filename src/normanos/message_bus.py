class MessageBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        print(f"🔗 SUBSCRIBE: {event} → {callback.__name__}")

        if event not in self.subscribers:
            self.subscribers[event] = []

        self.subscribers[event].append(callback)

    def publish(self, event, message):
        if event not in self.subscribers:
            return

        # iterate over copy to avoid mutation bugs
        for callback in list(self.subscribers[event]):
            callback(message)