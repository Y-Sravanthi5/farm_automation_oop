class Irrigation:
    def __init__(self, capacity):
        self.capacity = capacity
    def irrigate(self, crop):
        if self.capacity > 0:
            print(f"Irrigating {crop.name}")
            crop.grow()
            self.capacity -= 1
        else:
            print("No water left!")