"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    follow_black_lines(robot)
    robot.drive_system.make_polygon(4, 50)

def follow_black_lines(robot):
    robot.drive_system.start_moving(50, 50)
    while True:
        if robot.color_sensor.get_reflected_intensity() > 50:
            robot.drive_system.left_wheel.start_spinning(20)
            print(robot.color_sensor.get_reflected_intensity())
        else:
            robot.drive_system.left_wheel.start_spinning(50)
            print(robot.color_sensor.get_reflected_intensity())




main()
