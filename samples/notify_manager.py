#!/usr/bin/env python3

from time import sleep

from notify_engine import (
    NotifyManager, EventLoop, CommonEvent
)


def handler(event):
    print(event.message)
    print(event.__dict__)
    print(event.serialize())


def start_task(task, event):
    task(event)


def nm_factory():
    evl = EventLoop('redis://localhost:6379/9')
    nm = NotifyManager(evl, start_task)
    return nm


if __name__ == '__main__':
    nm = nm_factory()
    nm.subscribe(CommonEvent, handler)
    while True:
        nm.run()
        sleep(1)
