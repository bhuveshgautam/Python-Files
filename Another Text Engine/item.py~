class Item(object):
    """
    The class for describing various items found throughout the game.

    identifiers: list of string | The identifiers used to access the object
    description: string | The description printed when object is inspected
    areaString: string | The string that's used when describing an area
    useFunc: function | Function that takes a Player and Area and is called
                        when item is "used"
    """
    def __init__(self, identifiers, description, areaString):
        self.identifiers = identifiers
        self.description = description
        self.areaString  = areaString
        self.useFunc     = lambda x, y: None

    def getIdentifierList(self):
        """
        Returns the list of identifiers used to interact with the item

        return: list of string | The list of identifiers
        """
        return self.identifiers

    def getDescription(self):
        """
        Returns the description of the item

        return: string | The description
        """
        return self.description

    def getAreaDescription(self):
        """
        Returns the area string of the item

        return: string | The area string
        """
        return self.areaString

    def setUseFunction(self, function):
        """
        Sets the use function to the given function

        function: function | A function that takes the Player object an the
                             currently active Area object
        return: None
        """
        self.useFunc = function

    def use(self, player, area):
        """
        Executes the use function

        player: Player | The Player object containing the state of the game
        area: Area | The currently active Area object
        return: None
        """
        self.use(player, area)
