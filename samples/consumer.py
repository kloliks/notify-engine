#!/usr/bin/env python3

from notify_engine import EventLoop
from time import sleep


def handler(event):
    print('handler:', event)


def bla(evl):
    def wrap(event):
        print('wrap:', event)
        evl.subscribe(handler)

    return wrap


def run(evl):
    evl.subscribe(bla(evl))
    while True:
        evl.run()
        sleep(0.1)


if __name__ == "__main__":
    evl = EventLoop('redis://localhost:6379/9')
    run(evl)
