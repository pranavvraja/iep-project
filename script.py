import serial
import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Function to increase volume
def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(1.0, current_volume + 0.1)  # Increase volume by 10%
    volume.SetMasterVolumeLevelScalar(new_volume, None)

# Function to decrease volume
def decrease_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(0.0, current_volume - 0.1)  # Decrease volume by 10%
    volume.SetMasterVolumeLevelScalar(new_volume, None)

# Open serial connection to Arduino Uno
ser = serial.Serial('COM6', 9600)  # Replace 'COMX' with the appropriate port

while True:
    # Read distance data from Arduino Uno
    # Read distance data from Arduino Uno
    distance_data = ser.readline().strip().decode('utf-8')
    # Extract the numeric part of the string
    distance_value = distance_data.split(': ')[1]
    # Parse distance value
    distance = int(distance_value)
    print(distance)
    # Adjust laptop volume based on distance
    if distance < 10:  # Adjust threshold as needed
        increase_volume()
        print("Volume increased")
    elif distance > 20 and distance < 40:  # Adjust threshold as needed
        decrease_volume()
        print("Volume decreased")
