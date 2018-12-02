from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    """Abstract observer"""

    @abstractmethod
    def update(self, message: str) -> None:
        """Receiving new message"""
        pass

class Observable(metaclass=ABCMeta):
    """Abstract observable"""

    def __init__(self) -> None:
        self.observers = []     # list with observers

    def register(self, observer: Observer) -> None:
        """Register new observer"""
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        """pass the notification to all observers, that subsribed on this event"""
        for observer in self.observers:
            observer.update(message)

class Newspaper(Observable):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)

class Citizen(Observer):
    """real observer"""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        """Receiving new update"""
        print('{} learn next: {}'.format(self.name, message))


if __name__ == '__main__':
    newspaper = Newspaper()
    newspaper.register(Citizen('Dmitry')) # register subscribers
    newspaper.register(Citizen('Vlad'))
    newspaper.add_news('This is pattern observer')

