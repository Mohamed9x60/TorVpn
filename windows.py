import atexit
import subprocess
import time
import os
import random
import logging
import stem.process
from stem.control import Controller
from colorama import init, Fore, Style
import socket
import sys

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
        self.polipo_process = None

    def generate_countries_list(self):
        # Generate a list of countries
        countries = [
            "Algeria", "Egypt", "Nigeria", "South Africa", "Morocco", "Kenya", "Ethiopia", "Ghana", "Tanzania", "Uganda",
            "China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan", "Philippines", "Vietnam", "Turkey", "Iran",
            "Brazil", "Colombia", "Argentina", "Peru", "Venezuela", "Chile", "Ecuador", "Bolivia", "Paraguay", "Uruguay",
            "United States", "Canada", "Mexico", "Guatemala", "Cuba", "Haiti", "Dominican Republic", "Honduras", "Nicaragua", "El Salvador",
            "Australia", "New Zealand", "Papua New Guinea", "Fiji", "Solomon Islands", "Vanuatu", "Samoa", "Kiribati", "Tonga", "Tuvalu",
            "Russia", "Germany", "United Kingdom", "France", "Italy", "Spain", "Ukraine", "Poland", "Romania", "Netherlands"
        ]
        random.shuffle(countries)
        return countries[:200]

    def check_ports_availability(self):
        # Check available ports
        available_ports = []
        for port in [9050, 9051, 9052, 9053, 9054, 5055, 9056, 9057, 9058, 9059, 9060, 9061, 9062, 9063, 9064, 9065, 9066, 9067, 9068, 9069, 9070]:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex(('127.0.0.1', port))
                if result != 0:
                    available_ports.append(port)
        return available_ports

    def start_tor_service(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                available_ports = self.check_ports_availability()
                if available_ports:
                    for port in available_ports:
                        tor_process = stem.process.launch_tor_with_config(
                            config={'SocksPort': str(port)},
                            init_msg_handler=self.print_bootstrap_lines,
                            tor_cmd="tor"
                        )
                        logging.info(f"Tor service started on port {port}")
                        return
                    else:
                        logging.error("No available ports found for Tor service.")
                else:
                    logging.error("No ports available for Tor service.")
                    sys.exit()
        except Exception as e:
            logging.error(f"Failed to start Tor service: {e}")
            sys.exit()

    def stop_existing_tor_process(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                controller.terminate_all()
                logging.info("All existing Tor sessions have been stopped.")
        except Exception as e:
            logging.error(f"Failed to stop existing Tor sessions: {e}")

    def start_polipo_proxy(self):
        try:
            self.polipo_process = subprocess.Popen(["polipo.exe", "-c", "config.txt"])
            atexit.register(self.stop_polipo_proxy)
            logging.info("Polipo proxy started successfully")
        except Exception as e:
            logging.error(f"Failed to start Polipo proxy: {e}")
            sys.exit()

    def stop_polipo_proxy(self):
        if self.polipo_process:
            try:
                self.polipo_process.terminate()
                logging.info("Polipo proxy stopped successfully")
            except Exception as e:
                logging.error(f"Failed to stop Polipo proxy: {e}")

    def change_ip(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                controller.signal(stem.Signal.NEWNYM)
                logging.info("Changed IP address successfully")
        except Exception as e:
            logging.error(f"Failed to change IP address: {e}")

    def run(self, duration, interval):
        try:
            self.start_tor_service()

            if duration == float('inf'):
                print("VPN session is set to run indefinitely.")
            else:
                print(f"VPN session will run for {duration} minutes.")
            print(f"IP address will change every {interval} seconds.")

            while True:
                self.change_ip()
                time.sleep(interval)
                os.system("curl ifconfig.me > temp_ip.txt")
                with open('temp_ip.txt', 'r') as file:
                    new_ip = file.read().strip()

                logging.info(f"New IP Address: {new_ip}")
                print(f"New IP Address: {new_ip}")

                wait_time = random.randint(duration * 60 // 2, duration * 60) if duration != float('inf') else interval
                logging.info(f"Next IP change in {wait_time} seconds...")
                print(f"Next IP change in {wait_time} seconds...")
                time.sleep(wait_time)
        except OSError as e:
            logging.error(f"Failed to start Tor service: {e}")
            sys.exit()
        finally:
            self.show_contact_info()

    def show_contact_info(self):
        print("\nFor support, please contact:")
        print(f"Username: {self.username}")
        print(f"Phone number: {self.phone_number}")

    def print_bootstrap_lines(self, line):
        if "Bootstrapped" in line:
            print(line)

    def get_current_ip(self):
        try:
            with Controller.from_port(port=9050) as controller:
                controller.authenticate()
                return controller.get_info("ip-to-country/{0}".format(new_ip))
        except Exception as e:
            logging.error(f"Failed to get current IP address: {e}")

if __name__ == "__main__":
    vpn = TorIPChanger()
    vpn.start_polipo_proxy()

    print(Fore.MAGENTA + "Welcome to Tor VPN Changer" + Style.RESET_ALL)

    duration = input("Enter the duration of the VPN session in minutes (Enter 'inf' for infinite duration): ")
    interval = input("Enter the interval between IP changes in seconds: ")

    vpn.run(float(duration) if duration != 'inf' else float('inf'), int(interval))
