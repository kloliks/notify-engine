from .interfaces import (
    EventInterface,
    EventSerializerComponent,
    EventPublishOptsComponent
)


class CommonPublishOpts(EventPublishOptsComponent):
    @staticmethod
    def ttl():
        return None


class CommonEventSerialize(EventSerializerComponent):
    def serialize(event: EventInterface) -> dict:
        return {
            'type': event.event_type(),
            'data': event.__dict__,
        }

    @classmethod
    def deserialize(cls, serialize_data):
        if serialize_data.get('type') != cls.event_type():
            return None

        if not isinstance(serialize_data.get('data'), dict):
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
