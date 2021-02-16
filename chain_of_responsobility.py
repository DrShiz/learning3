class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


E_INT, E_FLOAT, E_STR = "INT", "FLOAT", "STR"
# class Event:
#     def __init__(self, kind):
#         self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_INT:
            if event.data is None:
                return obj.integer_field
            else:
                obj.integer_field = event.data
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_FLOAT:
            if event.data is None:
                return obj.float_field
            else:
                obj.float_field = event.data
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_STR:
            if event.data is None:
                return obj.string_field
            else:
                obj.string_field = event.data
        else:
            return super().handle(obj, event)


class EventSet:
    def __init__(self, data):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[type(data)]
        self.data = data


class EventGet:
    def __init__(self, data):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[data]
        self.data = None
