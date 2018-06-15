import logging

from .interfaces import (
    EventInterface,
    EventSerializerComponent,
    EventPublishOptsComponent
)


logger = logging.getLogger('notify_manager')


class CommonPublishOpts(EventPublishOptsComponent):
    @staticmethod
    def ttl():
        return None

    @staticmethod
    def meta() -> dict:
        return {
            'ttl': CommonPublishOpts.ttl(),
        }


class CommonEventSerialize(EventSerializerComponent):
    def serialize(event: EventInterface) -> dict:
        return {
            'type': event.event_type(),
            'data': event.__dict__,
        }

    @classmethod
    def deserialize(cls, serialize_data):
        if serialize_data.get('type') != cls.event_type():
            logger.warning('CommonEventSerialize: {} != {}. event({})'.format(
                serialize_data.get('type'), cls.event_type(), serialize_data
            ))
            return None

        if not isinstance(serialize_data.get('data'), dict):
            logger.warning((
                'CommonEventSerialize: serialize_data["data"] != dict. '
                'event({})'.format(
                    serialize_data
            )))
            return None

        ev = cls()
        ev.__dict__.update(serialize_data['data'])
        return ev


class CommonEvent(EventInterface, CommonEventSerialize, CommonPublishOpts):
    def __init__(self, message=None):
        self.message = message

    @staticmethod
    def event_type():
        return 'Common event'
