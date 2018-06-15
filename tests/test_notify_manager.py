#!/usr/bin/env python3

import unittest

from notify_engine import (
    NotifyManager, EventLoopInterface, CommonEvent, EventInterface,
)

from notify_engine.notify_manager.events import (
    CommonEventSerialize, CommonPublishOpts,
)


class myEvent(EventInterface, CommonEventSerialize, CommonPublishOpts):
    def __init__(self, message=None, additional=None):
        self.message = message
        self.additional = additional

    @staticmethod
    def event_type():
        return 'myEvent'


class EventLoop(EventLoopInterface):
    def __init__(self):
        self.subscribers = set()
        self.messages = list()

    def subscribe(self, handle):
        self.subscribers.add(handle)

    def publish(self, message):
        self.messages.append(message)

    def stop(self):
        return

    def _pop_message(self):
        while self.messages:
            m = self.messages.pop()
            yield m

    def run(self):
        for message in self._pop_message():
            for subscriber in self.subscribers:
                subscriber(message)


class TestNotifyManager(unittest.TestCase):
    def test_notify_manager(self):
        '''Test nofity manager subscribe/publish'''
        evl = EventLoop()
        nm = NotifyManager(evl, lambda task, event: task(event))

        test_message = 'test message 0081'
        additional_message = 'additional message 9240'

        ok = {
            'called_common': False,
            'called_my': False,
        }

        def task_common_handler(event):
            ok['called_common'] = True
            self.assertEqual(event.message, test_message)

        def task_my_handler(event):
            ok['called_my'] = True
            self.assertEqual(event.message, test_message)
            self.assertEqual(event.additional, additional_message)

        nm.publish(CommonEvent(test_message))
        nm.subscribe(CommonEvent, task_common_handler)
        nm.subscribe(myEvent, task_my_handler)

        nm.run()
        self.assertTrue(ok['called_common'])
        self.assertFalse(ok['called_my'])

        ok['called_common'] = False
        nm.run()
        self.assertFalse(ok['called_common'])
        self.assertFalse(ok['called_my'])
        
        nm.publish(myEvent(test_message, additional_message))
        nm.run()
        self.assertFalse(ok['called_common'])
        self.assertTrue(ok['called_my'])
        
        ok['called_my'] = False
        nm.publish(CommonEvent(test_message))
        nm.publish(myEvent(test_message, additional_message))
        nm.run()
        self.assertTrue(ok['called_common'])
        self.assertTrue(ok['called_my'])

        
if __name__ == '__main__':
    unittest.main()
