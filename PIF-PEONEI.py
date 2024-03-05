import time
import os
import random
import logging
import stem.process
from stem.control import Controller
from colorama import init, Fore, Style

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
            # Attempt to start Tor service on multiple ports
            available_ports = [9050, 9051, 9052, 9053, 9054]
            for port in available_ports:
                tor_process = stem.process.launch_tor_with_config(
                    config={'SocksPort': str(port)},
                    init_msg_handler=self.print_bootstrap_lines,
                )
                logging.info(f"Tor service started on port {port}")
                return  # If successful, exit the function
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"Port {port} is already in use.")
                self.stop_existing_tor_process(port)
            else:
                # If there's another unexpected error, re-raise the exception to handle it elsewhere
                raise OSError(f"Failed to start Tor service: {e}")

        # If reached here, unable to find a free port to start Tor service
        print("Unable to find a free port to start Tor service.")
        exit()

    def stop_existing_tor_process(self, port):
        try:
            with Controller.from_port(port=port) as controller:
                controller.authenticate()
                controller.signal(stem.Signal.SHUTDOWN)
                logging.info(f"Stopped Tor service using port {port}")
        except Exception as e:
            logging.error(f"Failed to stop Tor service using port {port}: {e}")

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
