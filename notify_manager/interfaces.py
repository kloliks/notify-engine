from abc import ABCMeta, abstractmethod


class EventPublishOptsComponent:
    __metaclass__ = ABCMeta

    @staticmethod
    def ttl():
        '''Возвращает ttl сообщения'''


class EventSerializerComponent:
    __metaclass__ = ABCMeta

    @abstractmethod
    def serialize(event) -> dict:
        '''Сериализует событие'''

    @classmethod
    @abstractmethod
    def deserialize(cls, serialize_data: dict):
        '''Десериализует событие'''


class EventInterface(EventSerializerComponent, EventPublishOptsComponent):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def event_type():
        '''Возвращает тип события'''
