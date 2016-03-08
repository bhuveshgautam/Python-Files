import global_commands

class Area(object):
    """
    An Area Object is the basic unit used to drive the game.

    description: string | A string used to describe the "area" in the game

    inspectString: string | The string shown when area is inspected from
                            another area
    
    itemList: list of Item | A list containing all the Item objects in
                             contained in the "area"
    
    linkedAreas: dictionary of Area | A dictionary containing identifier
                                      frozensets as keys and Area objects as
                                      values
    
    event: function | A function that takes calling Area object and a Player
                      object that executes every time the area is loaded
    
    commands: dictionary | A dictionary of available commands with frozenset
                           lists as keys and function(Player, Area, elem) as
                           values
    """
    def __init__(self, description, inspectString):
        def printDescription(player, area):
            """
            Prints the description of Area

            player: Dummy parameter
            area: Dummy parameter
            return: None
            """
            print self.getDescription()
        self.description = description
        self.inspectString = inspectString
        self.itemList = []
        self.linkedAreas = {}
        self.event = printDescription
        self.commands = global_commands.global_commands.copy()

    def getDescription(self):
        """
        Returns the description assocaited with the calling object.

        return: string | The description
        """
        desc = self.description

        for item in self.itemList:
            desc += ' ' + item.getAreaDescription()

        return desc

    def getInspectString(self):
        """
        Returns the string set for when area is inspected outside of itself.

        return: string | The inspect string
        """
        return self.inspectString

    def getLinkedList(self):
        """
        Returns the list of areas accessable through this one.

        return: list of Area | The list of areas that are accessable
        """
        return self.linkedAreas

    def getItemList(self):
        """
        Returns the list of items associated with the calling object

        return: list of Item | The list of items
        """
        return frozenset(self.itemList)

    def addCommand(self, commands, function):
        """
        This will be added to the set of commands for the function and will be
        available for the player to use while in calling Area

        commands: frozenset of string | A frozenset of commands to associate
                                        with the command function

        function: function | A function that takes a Player, Area, and elem
                             resembling the structure of global_commands

        return: None
        """
        self.commands[commands] = function

    def setEvent(self, function):
        """
        Takes a function that takes a Player object and an Area object
        and sets it to event, which runs every time the area is loaded.

        function: function | A fuction that takes the Player object and the
                             active Area object

        return: None
        """
        self.event = function

    def addItem(self, item):
        """
        Adds the given item to the Area's item list.

        item: Item | The Item to be added to the item list

        return: None
        """
        temp = [item]
        self.itemList.append(temp)

    def addLink(self, idList, area):
        """
        Adds the given area to the linked area dictionary

        idList: frozenset of string | Set of identifiers.
        area: Area | The area to be linked.
        return: None
        """
        self.linkedArea[idList] = area

    def takeItem(self, elem):
        """
        Returns the item associated with elem and removes it from itemList.

        elem: string | The identifier associated with intended item

        return: Item | The item which has been removed from itemList
        """
        for item in itemList:
            if elem in item.getIdentifierList():
                itemList.remove(item)
                return item

        raise ValueError(elem + " <- Not in inventory")

    def executeCommand(self, player, command):
        """
        Executes the command indicated by command.

        player: Player | The Player object holding the state of the game        
        command: string | The string indicating which command to be run
        
        return: None
        """
        def extractCommand(splitCmd):
            """
            Finds the command in splitCmd and returns the associated function,
            if none is found it returns None.

            splitCmd: list of string | The split command
            return: tuple with string and Function or None | Returns a string
                                                             and a function if
                                                             a valid command is
                                                             found.
            """
            if splitCmd == []:
                return ('', None)

            tempCmd = ' '.join(splitCmd)

            for idList in self.commands:
                if tempCmd in idList:
                    return (tempCmd, self.commands[idList])

            return extractCommand(splitCmd[:-1])

        com, func = extractCommand(command.split(' '))

        if func == None:
            print "You don't know how to do that."
            return
        
        elem = command[len(com) + 1:]
        func(player, self, elem)

    def executeEvent(self, player):
        """
        Takes the Player object and executes the event associated with the
        the current area.

        player: Player | The player object holding the current stae of the game
        return: None
        """
        self.event(self, player)
