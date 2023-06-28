import os
import platform
import psutil

os.system("ls -l")
os.system("ls")

# Get the CPU information using platform library
cpu_info = platform.processor()
print("CPU:", cpu_info)

# Get the CPU usage using psutil library
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu_usage)
