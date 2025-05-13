import os
import gpiod
import subprocess
import time

chip = gpiod.Chip('gpiochip0')
line = chip.get_line(14) # Connect to GPIO 14
line.request(consumer="example", type=gpiod.LINE_REQ_DIR_OUT)

while True:
    result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
    temp_string = result.stdout.strip()
    temp = float(temp_string.replace("temp=", "").replace("'C", ""))
#     print(temp) # Check current temperature
    if temp > 60:
        line.set_value(1)
#         print("high")
    else:
        line.set_value(0)
#         print("low")
    time.sleep(5)

line.release()
