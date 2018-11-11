"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Alec Polster.
"""


import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
            ev3.Sound.speak('I love you bitch, I aint never gonna stop loving you, bitch').wait()
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
         Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def go_forward(self, speed_string):
        speed = int(speed_string)
        print('Robot should start moving')
        self.robot.drive_system.start_moving(speed, speed)


main()

