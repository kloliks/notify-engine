#!/usr/bin/env python3

from .interface import EventLoopInterface

from kombu import Queue, Exchange, Connection, Producer


class EventLoop(EventLoopInterface):
    def __init__(self, broker, queue=None, **kwargs):
        conn = Connection(broker)
        name = 'default'
        queue = queue or Queue(name, Exchange(name), name, conn)
        queue.declare()
        producer = Producer(conn, queue.exchange, queue.routing_key)

        self._conn = conn
        self._queue = queue
        self._producer = producer
        self._subscribers = set()

    def _pop_messages(self):
        message = self._queue.get(no_ack=True)
        while self.running and message:
            yield message
            message = self._queue.get(no_ack=True)

    def run(self):
        self.running = True
        for message in self._pop_messages():
            for handler in self._subscribers.copy():
                handler(message.decode())
                if not self.running:
                    break

    def stop(self):
        self.running = False

    def subscribe(self, handler):
        self._subscribers.add(handler)

    def publish(self, event, publish_opts=None):
        meta={}
        if publish_opts:
            meta['ttl'] = publish_opts.get('ttl') or None
        self._producer.publish(event, **meta)
