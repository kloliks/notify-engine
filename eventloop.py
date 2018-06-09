#!/usr/bin/env python3

from interfaces import EventLoopInterface

from kombu import Queue, Exchange, Connection, Producer


class EventLoop(EventLoopInterface):
    def __init__(self, broker, **kwargs):
        conn = Connection(broker)
        name = 'default'
        queue = Queue(name, Exchange(name), name, conn)
        queue.declare()
        producer = Producer(conn, queue.exchange, queue.routing_key)

        self.conn = conn
        self.queue = queue
        self.producer = producer
        self.subscribers = set()

    def _pop_messages(self):
        message = self.queue.get(no_ack=True)
        while self.running and message:
            yield message
            message = self.queue.get(no_ack=True)

    def run(self):
        self.running = True
        for message in self._pop_messages():
            for handler in self.subscribers.copy():
                handler(message.decode())
                if not self.running:
                    break

    def stop(self):
        self.running = False

    def subscribe(self, handler):
        self.subscribers.add(handler)

    def publish(self, event):
        self.producer.publish(event)
