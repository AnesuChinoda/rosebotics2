"""
  Capstone Project.  Code written by Anesu Chinoda.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
robot = rb.Snatch3rRobot()

def main():
    """ Runs YOUR specific part of the project """

def polyogon(n, inches):
    for k in range(n):
        robot.drive_system.go_straight_inches(inches)
        robot.drive_system.spin_in_place_degrees(360/n)

def follow_black_line():
    while True:
        robot.color_sensor.get_reflected_intensity(10)

def go_to_color(color):
    robot.drive_system.start_moving()
    while True:
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break


main()
