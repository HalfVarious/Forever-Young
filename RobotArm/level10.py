from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 3

for a in range(1, 11, 2):
    robotArm.grab()

    for r in range(10-a):
        robotArm.moveRight()

    robotArm.drop()

    for l in range(9-a):
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()