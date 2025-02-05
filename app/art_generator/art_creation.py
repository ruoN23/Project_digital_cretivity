import random
from app.art_generator.shapes import Circle, Square

def generate_random_art():
    shapes = [Circle, Square]
    artwork = []
    for _ in range(10):  # Créer 10 formes
        shape_type = random.choice(shapes)
        color = random.choice(["red", "blue", "green", "yellow"])
        size = random.randint(20, 100)
        position = (random.randint(-300, 300), random.randint(-300, 300))
        shape = shape_type(color, size, position)
        artwork.append(shape)
    return artwork
