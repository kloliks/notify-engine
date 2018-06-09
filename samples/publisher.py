#!/usr/bin/env python3

from eventloop import EventLoop


def run(m_publish):
    m_publish('bla')


if __name__ == "__main__":
    evl = EventLoop('redis://localhost:6379/9')
    run(evl.publish)
