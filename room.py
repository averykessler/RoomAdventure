######################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name):
    # rooms have a name, exits (e.g., south), exit
    # locations (e.g., to the south is room n), items
    # (e.g., table), item descriptions (for each item),
    # and grabbables (things that can be taken into
    # inventory)
        self.name = name
        self.image = image
        self.description = ""
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self._time = "day"
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image = value
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, t):
        self._time = t
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and exit to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
    # adds a grabbable item to the room
    def delItem(self, item):
        self._items.remove(item)
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)
        # removes a grabbable item from the room
        # the item is a string (e.g., key)
    def delGrabbable(self, item):
    # remove the item from the list
        self._grabbables.remove(item)
    # returns a string description of the room
    def __str__(self):
    # first, the room name
        s = "You are in {}.\n".format(self.name)
        s += "Time = {}.\n".format(self._time)
        s += "{}\n".format(self.description)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s
