import platform
import psutil
import subprocess

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Machine": platform.machine(),
        "Node": platform.node(),
    }
    return system_info


if __name__ == "__main__":
    laptop_info = get_system_info()
    for key, value in laptop_info.items():
        print(f"{key}: {value}")
