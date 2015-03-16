# Only attack enemies of type "munchkin" and "thrower".
# Don't attack a "burl". Run away from an "ogre"!
loop:
    enemy = self.findNearestEnemy()
    
    # Remember: don't attack type "burl"!
    if enemy.type is "burl":
        self.say("I'm not attacking that Burl!")

    # The "type" property tells you what kind of creature it is.
    if enemy.type is "munchkin":
        self.attack(enemy)
    
    # Use "if" to attack a "thrower".
    if enemy.type is "thrower":
        self.attack(enemy)
    
    # If it's an "ogre", run away to the village gate!
    if enemy.type is "ogre":
        self.moveXY(41, 47)
    
