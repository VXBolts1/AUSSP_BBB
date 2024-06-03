# Task:
# Create a python script you can put on the BBB later.
# In your script, make a python class representing the device, which lets you set the device_name to a string when you initialize it.
# Add a method to the class to flash the LED. It should accept one argument, which is the number of seconds between flashes

import serial

class BBB:
    def __init__(self, device_name): #initialer
        self.device_name = device_name #set device_name
        self.ser = serial.Serial('/dev/ttyS1', 9600) #makes connection? 

    def flash_led(self, seconds): #method to flash the LED
        command = f"AAAA{self.device_name} 2 {seconds}\r\n" #create command
        self.ser.write(command.encode()) #send command 

device  = BBB(input('What is the device name: ')) #puts device name from user to the initialer
device.flash_led(input('How many seconds between flashes? ')) #puts the number of seconds from the user to the flash_led method
