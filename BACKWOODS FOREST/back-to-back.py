# Stay in the middle and defend!

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        # Either attack the enemy...
        self.attack(enemy)
        
        
    else:
        # ... or move back to your defensive position.
        self.moveXY(40, 34)
        
        
        
