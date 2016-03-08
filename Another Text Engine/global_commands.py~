def _travel(player, area, elem):
    """
    Loads indicated zone for Player.

    player: Player | The Player object holding the state of the game
    area: Area | The currently active Area object
    elem: string | The identifier used to access the area
    return: None
    """
    areaList = area.getLinkedList()
    
    for link in areaList:
        if elem in link:
            player.loadArea(areaList[link])
            return
    
    print "You don't know how to get there!"

def _pickup(player, area, elem):
    """
    Takes indicated Item from area if it exists

    player: Player | The Player object holding the state of the game
    area: Area | The currently active Area object
    elem: string | The identifier for desired Item
    return: None
    """
    for item in area.getItemList():
        if elem in item.getIdentifierList():
            player.addToInventory(area.takeItem(elem))
            return
    
    print "You don't see that."

def _use(player, area, elem):
    """
    Calls the indicated items use function.

    player: Player | The Player object holding the state of the game
    area: Area | The currently active Area object
    elem: string | The identifier indicating which Item to "use"
    return: None
    """
    for item in player.getInventory():
        if elem in item.getIdentifierList():
            item.use(player, area)
            return
            
    print "That's not in your inventory"

def _inspect(player, area, elem):
    """
    Returns the description of desired elem.
    Special case for when elem is "around" or "here":
        Prints the description of the current area.

    player: Player | The Player object holding the state of the game
    area: Area | The currently active Area object
    elem: string | The identifier indicating what to inspect
    return: None
    """
    if elem == "around" or elem == "here":
        print area.getDescription()
        return

    if (elem == "inventory" or elem == "backpack" or elem == "pockets" or
        elem == "sack" or elem == "rucksack" or elem == "purse"):
        if player.getInventory() == []:
            print "You're not carrying anything."
        else:
            print "You're currently carrying: ",
            inventory = player.getInventory()

            for i in range(len(inventory) - 1):
                print inventory[i].getIdentifierList()[0] + ", ",

            print inventory[len(inventory) - 1].getIdentifierList()[0]
        return

    masterList = (player.getInventory() +
                  area.getItemList())

    areaDict = area.getLinkedList()
    for lst in areaDict:
        if elem in lst:
            print areaDict[lst].getInspectString()
    
    for e in masterList:
        if elem in e.getIdentityList():
            print e.getDescription()
            return

    print "You don't know what that is!"

global_commands = {frozenset(["go", "go to", "travel",
                              "travel to", "walk", "walk to"]):
                   _travel,
                   frozenset(["pick up", "take", "grab", "get",
                              "acquire", "collect", "obtain"]):
                   _pickup,
                   frozenset(["use"]):
                   _use,
                   frozenset(["inspect", "look", "look at",
                              "examine", "analyze"]):
                   _inspect}
