class Farmer:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
    def take_care(self, crop, water_system):
        print(f"{self.name} is taking care of {crop.name}")
        water_system.irrigate(crop)
