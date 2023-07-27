import platform
import psutil
import subprocess

from hardware import get_system_info


# Function to get CPU information
def get_cpu_info():
    cpu_info = {
        "CPU": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
    }
    return cpu_info

# Function to get RAM information
def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        "Total RAM": f"{ram.total / (1024 ** 3):.2f} GB",
        "Available RAM": f"{ram.available / (1024 ** 3):.2f} GB",
        "Used RAM": f"{ram.used / (1024 ** 3):.2f} GB",
        "RAM Usage Percentage": f"{ram.percent:.2f}%",
    }
    return ram_info

# Function to get storage (disk) information
def get_storage_info():
    storage = psutil.disk_usage('/')
    storage_info = {
        "Total Storage": f"{storage.total / (1024 ** 3):.2f} GB",
        "Used Storage": f"{storage.used / (1024 ** 3):.2f} GB",
        "Free Storage": f"{storage.free / (1024 ** 3):.2f} GB",
        "Storage Usage Percentage": f"{storage.percent:.2f}%",
    }
    return storage_info

# Function to get GPU information (requires lshw on Linux)
def get_gpu_info():
    try:
        gpu_info = subprocess.check_output("lshw -C display", shell=True, text=True)
        return gpu_info
    except Exception as e:
        print(f"Error getting GPU information: {e}")
        return None

# Function to get S.M.A.R.T. data of storage devices
def get_smart_info():
    try:
        import pysmart.smart
        return pysmart.smart.smart_info()
    except Exception as e:
        print(f"Error getting S.M.A.R.T. data: {e}")
        return None

if __name__ == "__main__":
    laptop_info = get_system_info()
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    storage_info = get_storage_info()
    gpu_info = get_gpu_info()
    smart_info = get_smart_info()

    print("== Laptop Information ==")
    for key, value in laptop_info.items():
        print(f"{key}: {value}")

    print("\n== CPU Information ==")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    print("\n== RAM Information ==")
    for key, value in ram_info.items():
        print(f"{key}: {value}")

    print("\n== Storage Information ==")
    for key, value in storage_info.items():
        print(f"{key}: {value}")

    if gpu_info:
        print("\n== GPU Information ==")
        print(gpu_info)

    if smart_info:
        print("\n== S.M.A.R.T. Information ==")
        for device, data in smart_info.items():
            print(f"{device} S.M.A.R.T. Data:")
            for key, value in data.items():
                print(f"  {key}: {value}")
