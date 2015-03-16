# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

loop:
    flag = self.findFlag()
    if flag:
        # How do we get fx and fy from the flag's pos?
        # (Look below at how to get x and y from items.)
        fx = flag.pos.x + 5
        fy = flag.pos.y
        self.buildXY("fire-trap", fx, fy)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
