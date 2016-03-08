class Item:
    """
    A class for describing items found throughout the game.
    """
    def __init__(self, name, description):
        """
        Takes name and description and assigns them accordingly.

        name: string | The name of self
        description: string | The description of self
        """        
        self.name = name
        self.description = description

        def NOT_IMPLEMENTED(x):
            raise NotImplementedError("No action implemented for -> " + \
                                      self.name)
        
        self.action = NOT_IMPLEMENTED

    def getName(self):
        """
        Returns the name of the item.

        return: string | The name of the item.
        """
        return self.name

    def getDescription(self):
        """
        Returns the description of the item.

        return: string | The description of the item.
        """
        return self.description

    def setAction(self, action):
        """
        Sets the action of the item to the given function.

        action: function(Area) | A funciton of one argument that executes the
                                 action of item.
        return: None
        """
        self.action = action

    def executeAction(self, area):
        """
        Executes the action set for the item.

        area: Area | The area in which action will be executed
        return: None
        """
        self.action(area)
