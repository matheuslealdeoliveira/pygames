import random

def on_grid_random_monster():
    x = random.randint(0,590)
    y = random.randint(0,590)
    
    pos1 = ((x+10)//10) * 10, y//10 * 10
    pos2 = ((x+20)//10) * 10, y//10 * 10
    pos3 = x//10 * 10, ((y+10)//10) * 10
    pos4 = x//10 * 10, ((y+20)//10) * 10
    
    return[(pos1), (pos2), (pos3), (pos4)]

print(on_grid_random_monster())