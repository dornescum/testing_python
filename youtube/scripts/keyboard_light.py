import os
import sys

# Function to set the keyboard backlight brightness


def set_keyboard_backlight(brightness):
    try:
        with open("/sys/class/leds/tpacpi::kbd_backlight/brightness", "w") as file:
            file.write(str(brightness))
        print("Keyboard backlight brightness set to", brightness)
    except IOError:
        print("Error: Keyboard backlight control not available.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys)
        print("Usage: python keyboard_backlight.py <brightness_level>")
        sys.exit(1)

    try:
        # Get the brightness level from command line argument
        brightness_level = int(sys.argv[1])

        # Ensure the brightness level is between 0 and 3 (or the maximum supported level)
        brightness_level = max(0, min(brightness_level, 3))

        # Set the keyboard backlight brightness
        set_keyboard_backlight(brightness_level)
    except ValueError:
        print("Error: Invalid brightness level. Please provide an integer value between 0 and 3.")
