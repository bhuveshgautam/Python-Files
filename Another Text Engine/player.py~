class Player(object):
    """
    The class that holds the current state of the game including inventory and
    the currently active object.

    currentArea: Area | The currently active area used to process commands
    inventory: list of Item | The list of items currently being "carried"
    """
    def __init__(self, startingArea):
        """
        Takes an area to start with and sets it to current area

        startingArea: Area | The Area to start the game with
        """
        self.currentArea = None
        self.loadArea(startingArea)
        self.inventory = []

    def addToInventory(self, item):
        """
        Takes an Item object and adds it to inventory

        item: Item | The Item object to be added to inventory
        """
        self.inventory.append(item)

    def removeFromInventory(self, item):
        """
        Removes given Item from inventory

        item: Item | The Item object to be removed
        """
        self.inventory.remove(item)

    def getInventory(self):
        """
        Returns the inventory

        return: list of Item | The list of Item objects representing inventory
        """
        return self.inventory

    def loadArea(self, area):
        """
        Takes area and sets it as athe currently active Area object as well as
        executes its event function.

        area: Area | The area to become the new active area
        return: None
        """
        self.currentArea = area

        area.executeEvent(self)

    def play(self):
        """
        Starts the game loop.

        return: None
        """

        while True:
            command = raw_input("\n>> ")

            if (command == "exit" or command == "quit" or command == "leave" or
                self.currentArea.getLinkedList() == []):
                break

            self.currentArea.executeCommand(self, command)

        print "Bye!"
