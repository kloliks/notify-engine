#!/usr/bin/env python3

from notify_engine import (
    NotifyManager, EventLoop, CommonEvent
)


def nm_factory():
    evl = EventLoop('redis://localhost:6379/9')
    nm = NotifyManager(evl, lambda x, y: x(y))
    return nm


if __name__ == '__main__':
    nm = nm_factory()
    nm.publish(CommonEvent('bla'))
