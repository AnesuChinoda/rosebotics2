"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import time
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com




def main():
    """ Runs YOUR specific part of the project """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    setup_gui(root, mqtt_client)
    root.mainloop()


def setup_gui(root_window, mqttclient):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=30)
    frame.grid()
    label1 = ttk.Label(frame, text='Enter the play you want the robot to call')
    label1.grid(row=4, column=0)
    widget = ttk.Label(frame, text='ROBO-FOOTBALL 2018', font=80)
    widget.grid(row=0, column=1)
    new_thing = ttk.LabeledScale(frame, from_=0, to=100)
    new_thing.grid(row=5, column=2)
    label2 = ttk.Label(frame, text='Enter the starting speed', width=30)
    label2.grid(row=4, column=2)
    play_entry_box = ttk.Entry(frame)
    call_play_button = ttk.Button(frame, text="Call Play", width=20)

    play_entry_box.grid(row=5, column=0)
    call_play_button.grid(row=6, column=1)

    call_play_button['command'] = \
        lambda: handle_call_play(play_entry_box, new_thing, mqttclient)

def handle_call_play(entry, slider, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the slider and say
    the play in the entry box.
    """
    speed = int(slider.value)
    play = entry.get()
    print("Sending 'call_play' to the robot, with the play", play, "and the speed", speed)
    mqtt_client.send_message('call_play', [play, speed])


main()
