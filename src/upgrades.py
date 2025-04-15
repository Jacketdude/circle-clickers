
class Upgrades:
    def __init__(self):
        self.time_accumulated = 0.0
        self.addition_factor = 1

    def MoreClicksPerClick(self, button: bool, counter: int, clicksPCLick: int, demand: int):
        if button and counter >= demand:
            counter -= demand
            clicksPCLick += 1
            demand *= 2
        return counter, clicksPCLick, demand

    def PassiveClicks(self, isUpgradeUnlocked: bool, counter: int, dt:float):
        if isUpgradeUnlocked:
            self.time_accumulated += dt
            if self.time_accumulated >= 1.0:
                counter += 1
                self.time_accumulated = 0.0
        return counter

