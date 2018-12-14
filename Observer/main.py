from abc import ABCMeta, abstractmethod

class Subsriber(metaclass=ABCMeta):
    """Abstract observer"""

    @abstractmethod
    def update(self, message: str) -> None:
        pass

class News(metaclass=ABCMeta):
    """Abstract observable"""

    def __init__(self) -> None:
        self.observers = [] # list with observers

    def register(self, observer: Subsriber) -> None:
        """Register new observer"""
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        """pass the notification to all observers, that subsribed on this event"""
        for observer in self.observers:
            observer.update(message)


class DeveloperTeckNews(News):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class SoftwareTestingNews(News):
    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class ITManagementNews(News):
    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class PoliticalNews(News):
    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class WeatherNews(News):
    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class Developer(Subsriber):
    """real observer"""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        """Receiving new update"""
        print('{} received following message: {}'.format(self.name, message))


class Tester(Subsriber):
    """real observer"""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        """Receiving new update"""
        print('{} received following message: {}'.format(self.name, message))


class Manager(Subsriber):
    """real observer"""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        """Receiving new update"""
        print('{} received following message: {}'.format(self.name, message))


if __name__ == '__main__':
    dev_news = DeveloperTeckNews()
    qa_news = SoftwareTestingNews()

    weather_news = WeatherNews()
    developer = Developer('test_name')

    dev_news.register(developer)
    weather_news.register(developer)

    tester = Tester('qa')
    qa_news.register(tester)

    dev_news.add_news('Nvidia open-sources PhysX engine for games, AI, cars, and more')
    qa_news.add_news('Revolutions in QA – testing smart devices')


