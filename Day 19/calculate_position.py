
class PositionCalculator():
    def __init__(self, height, margin, num_racers):
        self.height = height
        self.margin = margin
        self.num_racers = num_racers

    def calculate_position(self):
        positions = []
        height_to_work = self.height - self.margin
        min_y = int(-(height_to_work/2))
        space_between_racers = height_to_work/self.num_racers
        last_y = 0
        for _ in range(0, self.num_racers):
            if _ == 0:
                last_y = min_y
                
            last_y = last_y+space_between_racers
            positions.append(last_y)
        
        return positions


calculator = PositionCalculator(height=400, margin=30, num_racers=10)
positions = calculator.calculate_position()
print(positions)

