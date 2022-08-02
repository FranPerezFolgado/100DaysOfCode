def turn_right():
 turn_left()
 turn_left()
 turn_left()

while not at_goal():
    if not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
