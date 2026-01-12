class Crop:
    def __init__(self, name, water_need, fertilizer_need):
        self.name = name
        self.water_need = water_need
        self.fertilizer_need = fertilizer_need
        self.growth_stage = 0
    def grow(self):
        self.growth_stage += 1
        print(f"{self.name} growth stage: {self.growth_stage}")
    def harvest(self):
        if self.growth_stage >= 5:
            print(f"{self.name} is ready for harvest!")
        else:
            print(f"{self.name} is not ready yet.")