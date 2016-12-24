
class todoItem:
    def __init__(self):
        self.title = None
        self.description = None
        self.tags = []

    # updateTitle takes a string called inTitle and mutates self in order to update the title property.
    # updateTitle: todoItem Str -> None
    # Effects: todoItem is updated
    def updateTitle(self, inTitle):
        self.title = inTitle

    # updateDescription takes a string called inDesc and mutates self in order to update the description property.
    # updateDescription: todoItem Str -> None
    # Effects: todoItem is mutated
    def updateDescription(self, inDesc):
        self.description = inDesc