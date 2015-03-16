# If there is an enemy, attack it.
# Otherwise, attack the chest!

loop:
    # Use if/else.
    enemy = self.findNearestEnemy()
    if(enemy):
        self.attack(enemy)
    else:
        self.attack("Chest")
    
    
