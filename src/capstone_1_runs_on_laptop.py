"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Anesu Chinoda.
"""
# ------------------------------------------------------------------------------
# Done: 1. Anesu Chinoda.  Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, discuss the "big picture" of laptop-robot
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 29
# Done:    to use YOUR robot's number instead of 99.
# Done:    Commit and push the change, then other team members Update Project.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 4. Run this module.
# Done:    Study its code until you understand how the GUI is set up.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)
    root.mainloop()
    # --------------------------------------------------------------------------
    # Done: 5. Add code above that constructs a   com.MqttClient   that will
    # Done:    be used to send commands to the robot.  Connect it to this pc.
    # Done:    Test.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=30)
    frame.grid()
    label1 = ttk.Label(frame, text='Mario', font=100)
    go_forward_button = ttk.Button(frame, text="Go forward", width=20)
    stop_button = ttk.Button(frame, text="stop", width=20)
    mario = ttk.Button(frame, text="It's a me, Mario!", width=20)
    label2 = ttk.Label(frame, text='Adjust starting speed:')
    speed_adjuster = ttk.LabeledScale(frame, from_=0, to=100)

    go_forward_button.grid(row=2, column=0)
    stop_button.grid(row=2, column=1)
    mario.grid(row=2, column=2)
    label1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    speed_adjuster.grid(row=3, column=0)
    go_forward_button['command'] = \
        lambda: handle_go_forward(mqtt_client, speed_adjuster)

    stop_button['command'] = lambda: handle_stop(mqtt_client)

    # mario['command'] = lambda: handle_mario(mqtt_client)


def handle_go_forward(mqtt_client, speed_adjuster):

    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """

    speed = speed_adjuster.value
    print("Sending 'go_forward' to the robot, with a speed", speed)
    mqtt_client.send_message('go_forward', [speed])


def handle_stop(mqtt_client):
    print("sending 'stop' to the robot")
    mqtt_client.send_message('stop',[])


def handle_mario(mqtt_client):
    print("Here we go")
    mqtt_client.send_message('mario', [])
    # --------------------------------------------------------------------------
    # Done: 6. This function needs the entry box in which the user enters
    # Done:    the speed at which the robot should move.  Make the 2 changes
    # Done:    necessary for the entry_box constructed in  setup_gui
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 7. For this function to tell the robot what to do, it needs
    # Done:    the MQTT client constructed in main.  Make the 4 changes
    # Done:    necessary for that object to make its way to this function.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 8. Add the single line of code needed to get the string that is
    # Done:    currently in the entry box.
    # Done:
    # Done:    Then add the single line of code needed to "call" a method on the
    # Done:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # Done:    "delegate" object that is constructed when the ROBOT's code
    # Done:    runs on the ROBOT.  Send to the delegate the speed to use
    # Done:    plus a method name that you will implement in the DELEGATE's
    # Done:    class in the module that runs on the ROBOT.
    # Done:
    # Done:    Test by using a PRINT statement.
    # --------------------------------------------------------------------------


main()
