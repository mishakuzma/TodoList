
class todoItem:
    def __init__(self):
        self.title = None
        self.description = None
        self.tags = []
        self.priority = None

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

    # setPriority takes an integer and updates todoItem with a new priority.
    # setPriorty: todoItem Int -> None
    # Effects: todoItem is mutated
    def setPriority(self, inInt):
        self.priority = inInt

    # addToTags takes a todoItem and a string called inTag to add the string to the item's tag list.
    # addToTags: todoItem Str -> None
    # Effects todoItem is mutated
    def addToTags(self, inTag):
        self.tags.push(inTag)

class todoGroup:
    def __init__(self):
        self.name = None
        self.contents = []
        self.tags = []
        self.priority = None

    def setName(self, inName):
        self.name = inName

    def addToContents(self, inContent):
        self.contents.push(inContent)

    # addToTags takes a todoGroup and a string called inTag to add the string to the group's tag list.
    # addToTags: todoGroup Str -> None
    # Effects todoGroup is mutated
    def addToTags(self, inTag):
        self.tags.push(inTag)

    # sortPriority will take a group object and sort the group based on each item's priority (ascending/descending)
    # sortPriority: todoGroup str -> (anyof None str)
    # Requires: direction is "ascending" or "descending". String returned if neither.
    # Effects: todoGroup is mutated.
    def sortPriority(self, direction):
        if direction == "ascending":
            firstProcess = []
            secondProcess = []
            thirdProcess = []
            for i in range(0, len(self.contents)):

        elif direction == "descending":
            for i in range(0, len(self.contents)):

        else:
            return "Invalid direction given"

class todoList:
    def __init__(self):
        self.groups = []
        self.indivItems = []

    # addGroup takes a todoList and a string called inName and creates a group in the todoList
    # addGroup: todoList Str -> None
    # Effects: todoList is modified
    def addGroup(self, inName):
        addedGroup = todoGroup
        addedGroup.setName(inName)
        self.groups += addedGroup
