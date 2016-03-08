from area import Area
from item import Item
from player import Player

start = Area(
    "You find yourself stranded in the middle of a road.  Looking to either "
    "side you see nothing but nondescript forest.  It appears your only "
    "path is either forward, farther down to where you were apparently "
    "going, or backwards, from where you apparently came. ",
    "A barren stretch of road.  How did you end up there? "
    )

keychain = Item(
    frozenset(["keys", "keychain", "key"]),
    "The keychain is made up of three keys and a key fob with the word "
    "\"TESIN\" inscribed on a tiny, rubber computer mouse.  Two of the keys "
    "are rather plain but the third has a Toyota symbol on it. ",
    "There is a keychain at your feet. "
    )

wallet = Item(
    frozenset(["wallet", "billfold", "pocketbook"]),
    "Looking inside the wallet, you find a small photo of yourself with your "
    "arm around someone's sholders.  There's a couple fives as well as an old "
    "library card. ",
    "There is a wallet laying on the road to your left. "
    )

forward = Area(
    "After a few hours of walking you notice it's starting to get dark. You "
    "decide it would be better to set up camp before night falls, so you "
    "head to a clearing on the side of the road.  As you start looking for "
    "a suitable place to camp, you hear what sounds like footsteps "
    "approaching behind you.  Before you can turn around, all goes black. ",
    "An empty strand of blacktop with nothing to see for miles. "
    )

carLane = Area(
    "As you walk along the deserted road, you see a mid-nineties Toyota "
    "Corolla stranded in the emergency lane.  It's starting to get dark out "
    "and you think you hear something rustling in the woods.  You can keep "
    "going forward, but it may be safer to try and get in the car. ",
    "Looking furthur down there road, there appears to be a deserted vehicle. "
    )

outsideOfCar = Area(
    "Looking through the driver's side window, you see an interior that looks "
    "spotless. ",
    "A mid-nineties Corolla, in prestine condition except for the spots of "
    "rust starting to form around the edges. "
    )

# start: Area object setup
start.addItem(keychain)
start.addItem(wallet)
start.addLink(frozenset(["forwards","forward","onward"]), forward)

# carLane: Area object setup
carLane.addLink(frozenset(["car", "vehicle", "toyota", "corolla",
                           "toyota corolla"]),
                outsideOfCar)
carLane.addLink(frozenset(["back", "backwards", "away"]), start)

actor = Player(start)
