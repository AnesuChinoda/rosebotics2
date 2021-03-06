"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Anesu Chinoda.
"""
# ------------------------------------------------------------------------------
# Done: 1. Anesu Chinoda
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, review the "big picture" of laptop-robot
# Done:    communication, per the comment in mqtt_sender.py.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # Done: 3. Construct a Snatch3rRobot.  Test.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # Done: 4. Add code that constructs a   com.MqttClient   that will
    # Done:    be used to receive commands sent by the laptop.
    # Done:    Connect it to this robot.  Test.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    mario(robot)
    # --------------------------------------------------------------------------
    # Done: 5. Add a class for your "delegate" object that will handle messages
    # Done:    sent from the laptop.  Construct an instance of the class and
    # Done:    pass it to the MqttClient constructor above.  Augment the class
    # Dome:    as needed for that, and also to handle the go_forward message.
    # Done:    Test by PRINTING, then with robot.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 6. With your instructor, discuss why the following WHILE loop,
    # Done:    that appears to do nothing, is necessary.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # Done: 7. Add code that makes the robot beep if the top-red button
        # Done:    on the Beacon is pressed.  Add code that makes the robot
        # Done:    speak "Hello. How are you?" if the top-blue button on the
        # Done:    Beacon is pressed.  Test.
        # ----------------------------------------------------------------------
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak("Hello")

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
        print('Robot should start moving.')
        self.robot.drive_system.start_moving(speed, speed)

    def stop(self):
        print('Robot should stop moving.')
        self.robot.drive_system.stop_moving()


def mario(robot):
    mushroom = 0
    ev3.Sound.speak("lets uh go")
    while True:

        if robot.color_sensor.green() > 70:
            ev3.Sound.beep().wait()
            mushroom = 1
            robot.drive_system.start_moving(100, 100)
            time.sleep(3)
        if robot.color_sensor.red() > 70:
            if mushroom == 1:
                robot.drive_system.start_moving(25, 25)
                time.sleep(4)
            if mushroom == 0:
                robot.drive_system.stop_moving()
                ev3.Sound.beep().wait()
                break
        if robot.color_sensor.blue() > 70:
            robot.drive_system.stop_moving()
            print('You won!')
            break
        time.sleep(1/100)




main()
