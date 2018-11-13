"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    wait_for_ball(robot)
    hike_the_ball(robot)
    while True:
        if robot.color_sensor.green() > 70:
            run_off_blocker(robot)
        elif robot.color_sensor.red() > 70:
            spin_defender(robot)
        elif robot.color_sensor.blue() > 70:
            celebrate(robot)
            break
    time.sleep(10)
    robot.drive_system.stop_moving()


def hike_the_ball(robot):
    robot.arm.motor.start_spinning(100)
    time.sleep(5)
    robot.arm.motor.stop_spinning('brake')


def run_off_blocker(robot):
    """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
    robot.drive_system.start_moving(100, 100)
    time.sleep(2)
    robot.drive_system.start_moving(30, 30)


def celebrate(robot):
    ev3.Sound.speak('Touchdown, touchdown, touchdown')
    robot.drive_system.right_wheel.start_spinning(100)
    robot.drive_system.left_wheel.start_spinning(-100)
    time.sleep(2)
    ev3.Sound.speak('Bengals win')


def spin_defender(robot):
    robot.drive_system.right_wheel.start_spinning(100)
    robot.drive_system.left_wheel.start_spinning(-100)
    time.sleep(4)
    robot.drive_system.right_wheel.start_spinning(30)
    robot.drive_system.left_wheel.start_spinning(30)
    time.sleep(4)


def wait_for_ball(robot):
    """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

    """
    while True:
        if robot.proximity_sensor.get_distance_to_nearest_object() < 10:
            break
        time.sleep(3)
        ev3.Sound.speak('Give me the ball')
    time.sleep(5)
    ev3.Sound.speak('Ball in place, ready for play call')


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def call_play(self, play_string, speed):
        ev3.Sound.speak(play_string + 'Hut, hut')
        speed1= int(speed)
        self.robot.drive_system.start_moving(speed1, speed1)

    def turn_right(self):
        self.robot.drive_system.right_wheel.stop_spinning()
        self.robot.drive_system.left_wheel.start_spinning(50)
        time.sleep(.5)
        self.robot.drive_system.right_wheel.start_spinning(50)

    def turn_left(self):
        self.robot.drive_system.left_wheel.stop_spinning()
        self.robot.drive_system.right_wheel.start_spinning(50)
        time.sleep(.5)
        self.robot.drive_system.left_wheel.start_spinning(50)


# def follow_black_lines(robot):
#     robot.drive_system.start_moving(50, 50)
#     while True:
#         if robot.color_sensor.get_reflected_intensity() > 50:
#             robot.drive_system.left_wheel.start_spinning(20)
#             print(robot.color_sensor.get_reflected_intensity())
#         else:
#             robot.drive_system.left_wheel.start_spinning(50)
#             print(robot.color_sensor.get_reflected_intensity())


main()

# make the sensor in the claw detect if a "ball" is there before picking it up
