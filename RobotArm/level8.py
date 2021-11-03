from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 3

for a in range(1):
    robotArm.moveRight()

    for b in range(7):
        robotArm.grab()

        for ab in range(8):
            robotArm.moveRight()
        robotArm.drop()

        for c in range(8):
            robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()