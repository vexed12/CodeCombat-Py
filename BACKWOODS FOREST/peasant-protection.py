loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy)
    if distance < 10:
        # Attack if they get too close to the peasant.
        self.attack(enemy)
        
    # Else, stay close to the peasant! Use else.
    else:
        self.moveXY(40, 37)
    
    
