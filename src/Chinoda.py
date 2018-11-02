"""
  Capstone Project.  Code written by Anesu Chinoda.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    polyogon(robot, 4, 5)

def polyogon(robot, n, inches):
    for k in range(n):
        robot.drive_system.go_straight_inches(inches)
        robot.drive_system.spin_in_place_degrees(360/n)

def follow_black_line(robot):
    robot.drive_system.start_moving(50, 50)
    while True:
        i = robot.color_sensor.get_reflected_intensity()
        print(i)
        if i > 30:
            robot.drive_system.start_moving(25, 50)
        else:
                robot.drive_system.start_moving(50, 50)


def go_to_color(color):
    robot.drive_system.start_moving()
    while True:
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break


main()
