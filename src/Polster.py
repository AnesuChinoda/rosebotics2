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
    hike_the_ball(robot)
    while True:
        if robot.color_sensor.blue() > 70:
            print('blue', robot.color_sensor.blue())
            run_off_blocker(robot)
        elif robot.color_sensor.red() > 70:
            print('red', robot.color_sensor.red())
            spin_defender(robot)
        elif robot.color_sensor.green() > 70:
            print('green', robot.color_sensor.green())
            celebrate(robot)
            break
    robot.drive_system.stop_moving()


def hike_the_ball(robot):
    robot.arm.motor.start_spinning(100)
    time.sleep(5)
    robot.arm.motor.stop_spinning('brake')
    robot.drive_system.start_moving(50, 50)


def run_off_blocker(robot):
    """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
    robot.drive_system.start_moving(100, 100)
    time.sleep(2)
    robot.drive_system.start_moving(50, 50)


def celebrate(robot):
    ev3.Sound.speak('Touchdown, touchdown, touchdown')
    robot.arm.raise_arm_and_close_claw()
    robot.drive_system.right_wheel.start_spinning(100)
    robot.drive_system.right_wheel.start_spinning(-100)
    time.sleep(6)
    robot.drive_system.right_wheel.start_spinning(50)
    robot.drive_system.right_wheel.start_spinning(50)



def spin_defender(robot):
    robot.drive_system.right_wheel.start_spinning(100)
    robot.drive_system.right_wheel.start_spinning(-100)
    time.sleep(6)
    robot.drive_system.right_wheel.start_spinning(50)
    robot.drive_system.right_wheel.start_spinning(50)


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def call_play(self, play_string, speed):
        ev3.Sound.speak(play_string)
        self.robot.drive_system.start_moving(speed, speed)


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

# make the sensor in the claw detect if a "ball" is there before picking it up
