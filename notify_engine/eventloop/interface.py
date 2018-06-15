from abc import ABCMeta, abstractmethod


class EventLoopInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def subscribe(self, handler):
        '''Подписаться на события'''

    @abstractmethod
    def publish(self, message, publish_opts=None):
        '''Опубликовать событие'''

    @abstractmethod
    def run(self):
        '''Чтение очереди сообщений'''

    @abstractmethod
    def stop(self):
        '''Останов чтения очереди'''
