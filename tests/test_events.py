#!/usr/bin/env python3

import unittest

from notify_engine import CommonEvent


class TestEvents(unittest.TestCase):
    def eq_message_test(self, ev1, ev2):
        self.assertEqual(ev1.message, ev2.message)
        self.assertEqual(ev1.event_type(), ev2.event_type())
        self.assertEqual(ev1.ttl(), ev2.ttl())
        self.assertEqual(ev1.meta(), ev2.meta())

    def test_events_serialize(self):
        '''Test CommonEvent serialize/deserialize'''
        ev0 = CommonEvent()
        ev1 = CommonEvent.deserialize(ev0.serialize())
        self.eq_message_test(ev0, ev1)

        ev0.message = 'test message 0018'
        ev2 = CommonEvent.deserialize(ev0.serialize())
        self.eq_message_test(ev0, ev2)

        ev3 = CommonEvent(ev0.message)
        self.eq_message_test(ev0, ev3)
        self.eq_message_test(ev2, ev3)

        ev4 = CommonEvent.deserialize(ev3.serialize())
        self.eq_message_test(ev0, ev4)
        self.eq_message_test(ev2, ev4)
        self.eq_message_test(ev3, ev4)
        
        serialize_data = ev0.serialize()
        serialize_data['data'] = []
        ev5 = CommonEvent.deserialize(serialize_data)
        self.assertEqual(ev5, None)
        
        serialize_data = ev0.serialize()
        serialize_data['type'] = 'Unknown type'
        ev5 = CommonEvent.deserialize(serialize_data)
        self.assertEqual(ev5, None)

    def test_events_meta(self):
        '''Test CommonEvent publish opts'''
        ev = CommonEvent()
        self.assertEqual(ev.meta()['ttl'], ev.ttl())


if __name__ == '__main__':
    unittest.main()
