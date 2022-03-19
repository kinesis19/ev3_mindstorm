#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.

# Motor_Ctrl -- 1.st
# ev3.speaker.beep()
# Motor(Port.A).run(500) 
# Motor(Port.C).run(500)
# sleep(2)

# Motor(Port.A).Stop(Stop.BREAKE)
# Motor(Port.D).Stop(Stop.HOLD)
# sleep(0.5)
# Motor_Ctrl -- 2.nd
# ev3.speaker.beep()
# Motor(Port.A).run_time(500, 2000, Stop.BRAKE, False)
# Motor(Port.C).run_time(500, 2000)

# Motor_Ctrl -- 3.th
Motor(Port.A).run_target(500, 360, Stop.BRAKE, False) # 파워가 약해도, 입력 된 각도만큼 끝까지 수행함.
Motor(Port.C).run_angle(500, 360)