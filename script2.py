import serial
import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import wmi

# Function to adjust volume (decreasing with higher distance)
def adjust_volume(distance):
  # Normalize the distance to be between 0 and 1 (inverted)
  normalized_distance = 1.0 - min(1.0, max(0.0, distance / MAX_DISTANCE))
  # Adjust volume inversely proportionally to the normalized distance
  volume_change = normalized_distance * MAX_VOLUME_CHANGE
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  current_volume = volume.GetMasterVolumeLevelScalar()
  # Decrease volume based on volume_change
  new_volume = max(0.0, min(1.0, current_volume - volume_change))
  volume.SetMasterVolumeLevelScalar(new_volume, None)

# Function to adjust brightness (decreasing with higher distance)
def adjust_brightness(distance):
#   # Normalize the distance to be between 0 and 1 (inverted)
  normalized_distance = 1.0 - min(1.0, max(0.0, distance / MAX_DISTANCE))
#   Adjust brightness inversely proportionally to the normalized distance
  brightness_change = int(normalized_distance * MAX_BRIGHTNESS_CHANGE)
#   # Decrease brightness based on brightness_change
#   wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(-brightness_change, 0)
    # Calculate brightness_change
    # brightness_change = ...

    # Ensure brightness_change is an integer
  brightness_change = int(brightness_change)

    # Adjust brightness
  wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness_change, 0)

# Open serial connection to Arduino Uno
ser = serial.Serial('COM6', 9600)  # Replace 'COMX' with the appropriate port

# Define maximum distance of the sensors
MAX_DISTANCE = 100  # Adjust as needed

# Define maximum volume change and brightness change
MAX_VOLUME_CHANGE = 0.1  # Adjust as needed
MAX_BRIGHTNESS_CHANGE = 100  # Adjust as needed

while True:
  # Initialize distance1 and distance2 to some default values
  distance1 = distance2 = 0

  # Read distance data from Arduino Uno
  distance_data = ser.readline().strip().decode('utf-8')
  # Check if the delimiter exists in the string
  if ":" in distance_data:
      # Split the string into distances
      distances = distance_data.split(":")
      # Check if the delimiter exists in the strings
      if '= ' in distances[0] and '= ' in distances[1]:
          # Extract the numeric part of the strings
          distance1_value = distances[0].split('= ')[1]
          distance2_value = distances[1].split('= ')[1]
          # Parse distance values
          distance1 = int(distance1_value)
          distance2 = int(distance2_value)
      else:
          print("Invalid data received: ", distances)
  else:
      print("Invalid data received: ", distance_data)

  # Adjust brightness and volume based on separate sensors
  adjust_brightness(distance1)
  print("Brightness adjusted based on distance:", distance1)
  adjust_volume(distance2)
  print("Volume adjusted based on distance:", distance2)
