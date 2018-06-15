import json
import logging

from .interfaces import EventInterface, NotifyManagerInterface
from notify_engine.eventloop import EventLoopInterface


logger = logging.getLogger('notify_manager')


class NotifyManager(NotifyManagerInterface):
    def __init__(self, backend: EventLoopInterface, start_task):
        self._backend = backend
        self._start_task = start_task
        self._subscribers = dict()

        self._backend.subscribe(self._on_event)

    def _on_event(self, event: str):
        event = json.loads(event)
        ev_type = event['type']
        if ev_type not in self._subscribers:
            logger.warning('Received an unknown message type')
            return

        ev = self._subscribers[ev_type][0](event)
        for task in self._subscribers[ev_type][1].copy():
            self._start_task(task, ev)

    def run(self):
        self._backend.run()

    def stop(self):
        self._backend.stop()

    def subscribe(self, event: EventInterface, handler):
        ev_type = event.event_type()
        if ev_type not in self._subscribers:
            self._subscribers[ev_type] = (event.deserialize, set())
        self._subscribers[ev_type][1].add(handler)

    def publish(self, event: EventInterface):
        self._backend.publish(json.dumps(event.serialize()), publish_opts=event.meta())
