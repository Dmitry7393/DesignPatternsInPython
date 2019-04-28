
class Widget(object):

    def draw(self):
        pass


class TextField(Widget):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def draw(self):
        print('draw TextField with width={} and height={}'.format(self.width, self.height))


class WidgetDecorator(Widget):

    def __init__(self, w):
        self.widget = w

    def draw(self):
        self.widget.draw()


class BorderDecorator(WidgetDecorator):

    def __init__(self, widget):
        WidgetDecorator.__init__(self, widget)

    def draw(self):
        WidgetDecorator.draw(self)
        print('BorderDecorator')


class ScrollDecorator(WidgetDecorator):

    def __init__(self, widget):
        WidgetDecorator.__init__(self, widget)

    def draw(self):
        WidgetDecorator.draw(self)
        print('ScrollDecorator')


widget = TextField(100, 20)
widget = BorderDecorator(widget)
widget = ScrollDecorator(widget)

widget.draw()