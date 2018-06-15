#!/usr/bin/env python3

import unittest

from notify_engine import EventLoop


class TestEventLoop(unittest.TestCase):
    def test_event_loop(self):
        '''Test EventLoop{.publish, .subscribe}'''
        message = 'test message 0081'
        ev = EventLoop('redis://localhost/10')
        ev.publish(message)

        ok = {'called': False}
        def handle(mes):
            ok['called'] = True
            self.assertEqual(mes, message)

        ev.subscribe(handle)
        ev.run()
        self.assertTrue(ok['called'])


if __name__ == '__main__':
    unittest.main()
