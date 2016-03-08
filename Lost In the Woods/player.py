from item import Item
from area import Area

class Player:
    """
    A class containing the current state of the game:
        The current area the player is in
        The player's inventory
    """
    def __init__(self):
        """
        Initializes the player class.
        """
        self.area = None
        self.inventory = {}

    def useItem(self, com):
        """
        Calls the action of the item associated with com.

        com: string | A lowercase string associated with an item in inventory
        return: boolean | True if executed successfully, False is item is not in
                          inventory.
        """
        try:
            self.inventory[com].executeAction(self.area)
            return True
        except KeyError:
            return False

    def addItem(self, item):
        """
        Adds an item to the inventory.

        item: Item | The item to be added to the inventory
        return: None
        """
        name = item.getName()

        if name in inventory:
            raise ValueError(name + " <- already in inventory!")
        else:
            self.inventory[name] = item

    def executeCommand(self, com):
        """
        Executes a command if in the list of commands:
            "inspect" - "look at" <- Prints the definition of the area or item
            "go" - "go to" <- Goes to given area
            "pick up" - "take" - "get" <- Adds specified item to inveotry
            "use" <- Uses specified item

        com: string | Command to be executed with area or item at the end
        return: boolean | Returns True if command was successfully executed,
                          False otherwise.
        """
        def inInventory(item):
            """
            Determines if given item is in inventory.

            item: Item | Item to check for in inventory.
            return: boolean | Returns True if item is in inventory,
                              False otherwise.
            """
            return item.getName() in self.inventory

        def inLinks(area):
            """
            Determins if given area is linked to current area.

            area: Area | Area to check if linked.
            return: boolean | Returns True if area is linked, False otehrwise.
            """
            return area.getTitle() in self.area.getLinkedAreas()

        splitCommand = com.split(' ')
        command = splitCommand[:-1].join(' ')
        elem = splitCommand[-1]

flashlight = Item("flashlight", "A flashlight to see in dark areas with.")
