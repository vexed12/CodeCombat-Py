# Use your new "cleave" skill as often as you can.

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        # Cleave the enemy!
        self.cleave(enemy)
        
    else:
        # Else (if cleave isn't ready), do your normal attack.
        self.attack(enemy)
        
