from colorama import init, Fore, Style
import os
import platform
import subprocess
import time
import __torvpn__ as torvpn

# Made By Eng.Mohamed Fouad | Updated By Arrow-Dev (https://arrow-dev.rf.gd)
# Initialize colorama for colored text
init()
# Requirements Libraries
libraries = ["random", "logging", "stem", "colorama"]
# Starting Labels
hypen = '-' * 27
simple_label = Fore.MAGENTA + hypen + (" Welcome to Tor VPN Changer ") + hypen + Style.RESET_ALL
# Special Charaters | [+] | [-] | For Appearance
input_character = Fore.GREEN + '+' + Style.RESET_ALL
error_charater = Fore.RED + '-' + Style.RESET_ALL
input_character = f'[{input_character}]'
error_charater = f'[{error_charater}]'

# Platform Filter
_os_ = platform.system().strip().lower()
# Commands Depend On System
commands = {
    "arch": "pacman -Syu tor torsocks",
    "debian": "apt update && apt upgrade && apt install tor torsocks -y",
    "windows": "choco install tor torsocks -y"
}
if _os_ not in commands.keys():
    print(f"{error_charater} Your System Isn't Supported At The Moment.")
    exit()


class Init():

    # This Class For Installing Libraries | Adding TorSocks To The Path
    # | Checking If Python Installed
    def clear_console(self):
        os.system("cls") if platform.system().lower() == "windows" else os.system('clear')

    def install_tor_package(self):
        # Use subprocess to run the command to install the package
        try:
            subprocess.run(commands[_os_], shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"{error_charater} Package installation failed.")
            exit()

    def install_libraries(self):
        try:
            for library in libraries:
                print(f"{input_character} Checking '{library}'")
                subprocess.run(["pip", "install", library], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.clear_console()
        except KeyboardInterrupt:
            print(f"{error_charater} Skipped ")
            time.sleep(2)
        except Exception as e:
            print(f"{error_charater} {e}")

    def run(self):
        self.install_tor_package()
        self.install_libraries()
        # Create an object for IP address changer
        vpn = torvpn.TorIPChanger()
        # Running The App
        print(simple_label)
        try:
            # Get VPN session duration and IP change interval from the user
            duration = input(f"{input_character} Enter the duration of the VPN session in minutes (Enter 'inf' for infinite duration):")
            interval = input(f"{input_character} Enter the interval between IP changes in seconds:")
            # Run VPN with the specified duration and interval
            vpn.run(float(duration) if duration != 'inf' else float('inf'), int(interval))
        except KeyboardInterrupt:
            print()
            print(f"{error_charater} Exited")

