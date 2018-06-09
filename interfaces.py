from abc import ABCMeta, abstractmethod


class EventPublishOptsComponent(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    @staticmethod
    def ttl():
        '''Возвращает ttl сообщения'''


class EventSerializerComponent():
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


class EventLoopInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def subscribe(self, handler):
        '''Подписаться на события'''

    @abstractmethod
    def publish(self, message):
        '''Опубликовать событие'''

    @abstractmethod
    def run(self):
        '''Чтение очереди сообщений'''

    @abstractmethod
    def stop(self):
        '''Останов чтения очереди'''
