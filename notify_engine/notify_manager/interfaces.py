from abc import ABCMeta, abstractmethod


class EventPublishOptsComponent:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def ttl():
        '''Возвращает ttl сообщения'''
        
    @staticmethod
    @abstractmethod
    def meta() -> dict:
        '''Возвращает опции публикации словарём'''


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


class NotifyManagerInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        '''Запускает цикл чтения событий из очереди'''

    @abstractmethod
    def stop(self):
        '''Остановка цикла чтения событий'''

    @abstractmethod
    def subscribe(self, event: EventInterface, handle):
        '''Подписаться на событие'''

    @abstractmethod
    def publish(self, event: EventInterface):
        '''Опубликовать событие в очереди'''
