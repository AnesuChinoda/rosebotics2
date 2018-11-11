"""
  Capstone Project.  Code written by Anesu Chinoda.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3


def main():
    """ Runs YOUR specific part of the project """
    print('hello')
    robot = rb.Snatch3rRobot()
    print('goodbye')
    #polyogon(robot, 4, 5)
    #follow_black_line(robot)
    #go_to_color(robot, 5)
    beep_when_in_front_of_camera(robot)
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


def go_to_color(robot, color):
    robot.drive_system.start_moving(20, 20)
    while True:
        print(robot.color_sensor.get_color())
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            print(robot.color_sensor.get_color())
            break

def beep_when_in_front_of_camera(robot):
    while True:
        if robot.camera.get_biggest_blob().get_area() > 1000:
            ev3.Sound.beep().wait()
main()
