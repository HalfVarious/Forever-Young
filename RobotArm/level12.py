from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:


for a in range(9):
    robotArm.moveRight() 

for a in range(10):
    if robotArm.grab() and robotArm.scan() == 'red':
        for i in range(10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(a):
            robotArm.moveLeft()

    else:
        robotArm.drop()
    
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()