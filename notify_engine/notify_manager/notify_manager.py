from .interfaces import EventInterface, NotifyManagerInterface
from notify_engine.eventloop import EventLoopInterface


class NotifyManager(NotifyManagerInterface):
    def __init__(self, backend: EventLoopInterface):
        pass

    def run(self):
        pass

    def stop(self):
        pass

    def subscribe(self, event: EventInterface, handler):
        pass

    def publish(self, event: EventInterface):
        pass
