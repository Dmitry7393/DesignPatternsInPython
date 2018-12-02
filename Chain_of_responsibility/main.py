import abc


class Handler(metaclass=abc.ABCMeta):
    """an interface for handling requests"""

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self):
        print('HANDLE_REQUEST IN BASE CLASS ')
        pass


class ConcreteHandler1(Handler):
    """Handle request, otherwise forward it to the successor."""

    def handle_request(self):
        print("ConcreteHandler1 handle_request")
        if True:  # if can_handle:
            print('handle')
            pass
        elif self._successor is not None:
            self._successor.handle_request()


class ConcreteHandler2(Handler):
    """Handle request, otherwise forward it to the successor."""

    def handle_request(self):
        print("ConcreteHandler2 handle_request")
        if False:  # if can_handle:
            pass
        elif self._successor is not None:
            print('pass to successor')
            self._successor.handle_request()


def main():
    concrete_handler_1 = ConcreteHandler1()
    concrete_handler_2 = ConcreteHandler2(concrete_handler_1) # concrete_handler_1 is successor of concrete_handler_2
    concrete_handler_2.handle_request()


if __name__ == "__main__":
    main()