from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:


for a in range(8):
    robotArm.moveRight()

for a in range(9):
    if robotArm.grab() and robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()

    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()