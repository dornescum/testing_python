import os

# Function to read CPU temperature in degrees Celsius


def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp_millidegrees = int(file.read().strip())
            temp_celsius = temp_millidegrees / 1000
            return temp_celsius
    except IOError:
        return None

# Function to convert degrees Celsius to Fahrenheit


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


if __name__ == "__main__":
    # Read CPU temperature in degrees Celsius
    cpu_temp_celsius = get_cpu_temperature()

    if cpu_temp_celsius is not None:
        # Convert to Fahrenheit
        cpu_temp_fahrenheit = celsius_to_fahrenheit(cpu_temp_celsius)

        # Display the temperature
        print(f"CPU Temperature: {cpu_temp_celsius:.2f} °C ({cpu_temp_fahrenheit:.2f} °F)")
    else:
        print("Error: CPU temperature reading not available.")
