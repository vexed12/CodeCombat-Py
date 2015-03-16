# Collect all the coins in each meadow.
# Use flags to move between meadows.
# Press Submit when you are ready to place flags.

loop:
    flag = self.findFlag()
    if flag:
        pass  # pass is a placeholder, it has no effect.
        # Pick up the flag.
        self.pickUpFlag(flag)
    else:
        # Automatically move to the nearest item you see.
        item = self.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)
