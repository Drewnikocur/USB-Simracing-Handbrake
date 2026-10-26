import serial
import pyvjoy
import time
import re

# Inicjalizacja vJoy (urządzenie nr 9)
j = pyvjoy.VJoyDevice(9)

ser = serial.Serial('COM6', 115200, timeout=0.1)
ser.reset_input_buffer()
time.sleep(2)

print("Mostek vJoy aktywny. Sterowanie osią Y...")

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            match = re.search(r'\d+', line)
            if match:
                val = int(match.group())
                
                # Zakres vJoy to zazwyczaj 1 do 32768
                vjoy_val = int((val / 4095.0) * 32768)
                if vjoy_val < 1: vjoy_val = 1
                if vjoy_val > 32768: vjoy_val = 32768

                # Sterowanie wyłącznie osią Y
                j.set_axis(pyvjoy.HID_USAGE_Y, vjoy_val)
                
    except Exception as e:
        print(f"Błąd: {e}")
        break