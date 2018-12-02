import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):

    def algorithm_interface(self):
        print("ConcreteStrategyA : real function")


class ConcreteStrategyB(Strategy):

    def algorithm_interface(self):
        print("ConcreteStrategyB : real function")


def main():
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()


if __name__ == "__main__":
    main()