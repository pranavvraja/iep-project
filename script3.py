import serial
import pyautogui  # Import library for simulating keystrokes

# Establish serial connection with Arduino
ser = serial.Serial('COM1' , 9600, timeout=1)  # Replace 'COM3' with your port

# Define thresholds and control key combinations based on your system
brightness_up_threshold = 100  # Example threshold for increasing brightness
brightness_down_threshold = 200  # Example threshold for decreasing brightness
volume_up_threshold = 50  # Example threshold for increasing volume
volume_mute_threshold = 25  # Example threshold for muting volume
brightness_up_key = "fn+f8"  # Replace with your system's brightness up key
brightness_down_key = "down"  # Replace with your system's brightness down key
volume_up_key = "volumeup"  # Replace with your system's volume up key
volume_down_key = "volumedown"  # Replace with your system's volume up key
volume_mute_key = "mute"  # Replace with your system's mute key

# Function to translate distance to control signal (you can customize this)
def translate_distance(distance, threshold_up, threshold_down, control_up, control_down):
  if distance < threshold_up:
    return control_up
  elif distance > threshold_down:
    return control_down
  else:
    return "none"  # No control signal if within threshold range

while True:
  # Read data from serial communication
  data = ser.readline().decode('utf-8').strip().split(':')
  if len(data) == 2:
    sensor, distance = data
    distance = int(distance)
    
    # Process data for brightness control
    brightness_control = translate_distance(distance, brightness_up_threshold, brightness_down_threshold, brightness_up_key, brightness_down_key)
    
    # Process data for volume control
    volume_control = translate_distance(distance, volume_up_threshold, volume_mute_threshold, volume_up_key, volume_mute_key)
    
    # Send simulated keystrokes for brightness and volume control
    if brightness_control != "none":
      pyautogui.press(brightness_control)
    if volume_control != "none":
      pyautogui.press(volume_control)

