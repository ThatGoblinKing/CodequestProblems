#https://lmcodequestacademy.com/problem/bird-watching

EXPECTED_OUTPUT = """Accipitridae
Cathartidae
Accipitridae"""
import math

class Bird:
    def __init__(self, 
                length: float, 
                body_width: float, 
                wingspan: float, 
                wing_angle: float):
        self.length = length
        self.body_width = body_width
        self.wingspan = wingspan
        self.wing_angle = wing_angle
        
    def __str__(self):
        return f"L: {self.length}, W: {self.body_width}, WngSpan: {self.wingspan}, WngAngle: {self.wing_angle}"
    def __repr__(self):
        return self.__str__()
    
    def __sub__(self, other):
        return math.sqrt((self.length - other.length)**2 + 
                         (self.body_width - other.body_width)**2 +
                         (self.wingspan - other.wingspan)**2 +
                         (self.wing_angle - other.wing_angle)**2)

class KnownBird(Bird):
    def __init__(self, 
                name: str, 
                length: float, 
                body_width: float, 
                wingspan: float, 
                wing_angle: float):
        super().__init__(length, body_width, wingspan, wing_angle)
        self.name = name
    
    def __str__(self):
        return f"Name: {self.name}, {super().__str__()}"
    
    def __repr__(self):
        return self.name

class UnknownBird(Bird):
    def to_known(self, name: str) -> KnownBird:
        return KnownBird(name,
                        self.length,
                        self.body_width,
                        self.wingspan,
                        self.wing_angle)

def get_known_bird() -> KnownBird:
    inputs = input().split(" ")
    return KnownBird(inputs[0], float(inputs[1]), float(inputs[2]), float(inputs[3]), float(inputs[4]))

def get_unkown_bird() -> UnknownBird:
    inputs = input().split(" ")
    return UnknownBird(float(inputs[0]), float(inputs[1]), float(inputs[2]), float(inputs[3]))

cases = int(input())
for _ in range(cases):
    line = input()
    known_bird_count, unknown_bird_count = (int(val) for val in line.split(" "))
    known_birds = [get_known_bird() for bird in range(known_bird_count)]
    unknown_birds = [get_unkown_bird() for bird in range(unknown_bird_count)]
    found_birds = []
    
    for bird in unknown_birds:
        k = 5
        found_family = False
        families = {}
        closest_birds = sorted(known_birds, key=lambda x: bird - x)
        while not found_family:
            for i in range(k):
                if closest_birds[i].name not in families:
                    families[closest_birds[i].name] = 1
                else:
                    families[closest_birds[i].name] += 1
            temp_max = 0
            family = sorted(families, key=lambda x: families[x])
            for family in families:
                if temp_max == families[family]:
                    break
                temp_max = families[family] if families[family] > temp_max else temp_max 
            else:
                found_family = True
                found_birds.append(max(families, key=families.get))
            k += 1
final_output = "\n".join(found_birds).rstrip()
print(final_output == EXPECTED_OUTPUT)
print(final_output)
print(unknown_birds[0] - known_birds[-1])