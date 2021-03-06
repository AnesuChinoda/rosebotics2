"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Alec Polster.
"""





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


def setup_gui(root_window, mqttclient):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqttclient)


def handle_go_forward(entry, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """

    speed = entry.get()
    print("Sending 'go_forward' to the robot, with a speed", speed)
    mqtt_client.send_message('go_forward', [speed])


main()
