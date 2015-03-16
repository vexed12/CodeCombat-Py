# Survive both waves by shielding and cleaving.
# When "cleave" is not ready, use your shield skill.
# You'll need at least 142 health to survive.

loop:
    enemy = self.findNearestEnemy()
    if(enemy):
        if(self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.shield()
            
