loop:
    # Check the distance to the nearest enemy.
    # If it comes closer than 10 meters, cleave it!
    # Else, attack the "Chest" by name.
    enemy = self.findNearestEnemy()
    if self.distanceTo(enemy) <= 10:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
    else:
        self.attack("Chest")
    
    
