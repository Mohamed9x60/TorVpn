import time
import os
import random
import logging
import stem.process
from stem.control import Controller
from colorama import init, Fore, Style
import socket

# Initialize colorama for colored text
init()

# Configure logging
logging.basicConfig(filename='tor_ip_changer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TorIPChanger:
    def __init__(self):
        # Contact information
        self.username = "Eng: Mohamed Fouad"
        self.phone_number = "01021213274"
        self.countries = self.generate_countries_list()

    def generate_countries_list(self):
        africa = ["Algeria", "Egypt", "Nigeria", "South Africa", "Morocco", "Kenya", "Ethiopia", "Ghana", "Tanzania", "Uganda"]
        asia = ["China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan", "Philippines", "Vietnam", "Turkey", "Iran"]
        south_america = ["Brazil", "Colombia", "Argentina", "Peru", "Venezuela", "Chile", "Ecuador", "Bolivia", "Paraguay", "Uruguay"]
        north_america = ["United States", "Canada", "Mexico", "Guatemala", "Cuba", "Haiti", "Dominican Republic", "Honduras", "Nicaragua", "El Salvador"]
        australia = ["Australia", "New Zealand", "Papua New Guinea", "Fiji", "Solomon Islands", "Vanuatu", "Samoa", "Kiribati", "Tonga", "Tuvalu"]
        europe = ["Russia", "Germany", "United Kingdom", "France", "Italy", "Spain", "Ukraine", "Poland", "Romania", "Netherlands"]

        all_countries = africa + asia + south_america + north_america + australia + europe
        random.shuffle(all_countries)
        return all_countries[:200]

    def check_ports_availability(self):
        available_ports = []
        for port in [9050, 9051, 9052, 9053, 9054]:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex(('127.0.0.1', port))
                if result != 0:
                    available_ports.append(port)
        return available_ports

    def start_tor_service(self):
        # Clear the screen
        os.system("clear")
        # Print logo in color
        print(Fore.CYAN + """
██████╗░██╗███████╗  ██████╗░███████╗░█████╗░███╗░░██╗███████╗██╗
██╔══██╗██║██╔════╝  ██╔══██╗██╔════╝██╔══██╗████╗░██║██╔════╝██║
██████╔╝██║█████╗░░  ██████╔╝█████╗░░██║░░██║██╔██╗██║█████╗░░██║
██╔═══╝░██║██╔══╝░░  ██╔═══╝░██╔══╝░░██║░░██║██║╚████║██╔══╝░░██║
██║░░░░░██║██║░░░░░  ██║░░░░░███████╗╚█████╔╝██║░╚███║███████╗██║
╚═╝░░░░░╚═╝╚═╝░░░░░  ╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝
""" + Style.RESET_ALL)

        try:
            # Check if any Tor sessions are running and stop them
            self.stop_existing_tor_process()

            # Check available ports
            available_ports = self.check_ports_availability()
            if not available_ports:
                print("No available ports to start Tor service.")
                exit()

            # Attempt to start Tor service on available ports
            for port in available_ports:
                tor_process = stem.process.launch_tor_with_config(
                    config={'SocksPort': str(port)},
                    init_msg_handler=self.print_bootstrap_lines,
                )
                logging.info(f"Tor service started on port {port}")
                return  # If successful, exit the function

        except OSError as e:
            raise OSError(f"Failed to start Tor service: {e}")

    def stop_existing_tor_process(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                for tor_pid in controller.get_pid_list():
                    logging.info(f"Stopping Tor process with PID: {tor_pid}")
                    controller.terminate_process(tor_pid)
                    time.sleep(1)  # Wait for process termination
                logging.info("All existing Tor sessions have been stopped.")
        except Exception as e:
            logging.error(f"Failed to stop existing Tor sessions: {e}")

    def change_ip(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                controller.signal(stem.Signal.NEWNYM)
                logging.info("Changed IP address successfully")
        except Exception as e:
            logging.error(f"Failed to change IP address: {str(e)}")

    def run(self, duration, interval):
        try:
            # Start Tor service
            self.start_tor_service()

            # Check VPN session duration
            if duration == float('inf'):
                print("VPN session is set to run indefinitely.")
            else:
                print(f"VPN session will run for {duration} minutes.")
            print(f"IP address will change every {interval} seconds.")

            while True:
                # Change IP address
                self.change_ip()
                time.sleep(interval)
                os.system("curl ifconfig.me > temp_ip.txt")
                with open('temp_ip.txt', 'r') as file:
                    new_ip = file.read().strip()

                # Display new IP address
                logging.info(f"New IP Address: {new_ip}")
                print(f"New IP Address: {new_ip}")

                # Random wait time before changing to a new IP address
                wait_time = random.randint(duration * 60 // 2, duration * 60) if duration != float('inf') else interval
                logging.info(f"Next IP change in {wait_time} seconds...")
                print(f"Next IP change in {wait_time} seconds...")
                time.sleep(wait_time)
        except OSError as e:
            logging.error(f"Failed to start Tor service: {e}")
            # You can increase the timeout or use another port here
            raise
        finally:
            # Call show_contact_info function after VPN session ends
            self.show_contact_info()

    def show_contact_info(self):
        print("\nFor support, please contact:")
        print(f"Username: {self.username}")
        print(f"Phone number: {self.phone_number}")

    # Function to print bootstrap progress during Tor service startup
    def print_bootstrap_lines(self, line):
        if "Bootstrapped" in line:
            print(line)

if __name__ == "__main__":
    # Create an object for IP address changer
    vpn = TorIPChanger()
    print(Fore.MAGENTA + "Welcome to Tor VPN Changer" + Style.RESET_ALL)

    # Get VPN session duration and IP change interval from the user
    duration = input("Enter the duration of the VPN session in minutes (Enter 'inf' for infinite duration): ")
    interval = input("Enter the interval between IP changes in seconds: ")

    # Run VPN with the specified duration and interval
    vpn.run(float(duration) if duration != 'inf' else float('inf'), int(interval))
