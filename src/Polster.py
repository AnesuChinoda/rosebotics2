"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    follow_black_lines()
    
def follow_black_lines():

    robot = rb.Snatch3rRobot()

    while True:
        robot.drive_system.start_moving(50, 50)
        robot.color_sensor.wait_until_intensity_is_greater_than(20)
        robot.drive_system.stop_moving()
        while True:
            if robot.color_sensor.get_reflected_intensity() < 20:
                break
            robot.drive_system.turn_degrees(10)
        if time.time() >= 30:
            break

main()
