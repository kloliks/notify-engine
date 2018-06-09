#!/usr/bin/env python3

from time import sleep

from rx import Observable
from kombu import Queue, Exchange, Connection


def queue_declare(name, conn):
    queue = Queue(name, Exchange(name), name, conn)
    queue.declare()
    return queue


def notify_queue_factory():
    conn = Connection('redis://localhost:6379/9')
    queue = queue_declare('default', conn)

    stream = Observable.interval(100) \
            .map(lambda _: queue.get(no_ack=True)) \
            .filter(lambda x: x != None) \
            .map(lambda x: x.decode()) \
            .publish()
    return stream


stream = notify_queue_factory()
stream.connect()

stream.subscribe(lambda x: print('source0:', x))

input('Press any key to add new subscriber\n')

stream.subscribe(lambda x: print('source1:', x))

input('Press any key to quit\n')
print('Done')
