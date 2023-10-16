def obstacle_detected():
    pass

def move_forward():
    pass

def move_till_obstacle():
    while (not(obstacle_detected())):
        move_forward()
    return

def distance_covered():
    pass

def move_for_width(width):
    while (distance_covered() < width or not(obstacle_detected())):
        move_forward()
    return

def turn_right():
    pass

def lawnmover(width_of_boat: int):
    while(True):
        move_till_obstacle()
        turn_right()
        move_for_width(width=width_of_boat)
        turn_right()
        
        