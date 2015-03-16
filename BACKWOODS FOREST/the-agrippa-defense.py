loop:
    enemy = self.findNearestEnemy()
    if enemy:
        pass  # Replace this with your own code.
        # Find the distance to the enemy with distanceTo.
        distance = self.distanceTo(enemy)
        # If the distance is less than 5 meters...
        if distance < 5:
            # ... if "cleave" is ready, cleave!
            if self.isReady("cleave"):
                self.cleave(enemy)
            # ... else, just attack.
            else:
                self.attack(enemy)
