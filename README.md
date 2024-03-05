# Tor VPN <..PIF PEONEI..> Changer

This Python script allows you to change your IP address using the Tor network. It runs a VPN session that changes the IP address at regular intervals.

## Features

- **Start Tor Service:** Initiates the Tor service to establish a connection with the Tor network.
- **Change IP Address:** Changes the IP address using the Tor network.
- **Run VPN Session:** Runs a VPN session with customizable duration and interval between IP changes.
- **Show Contact Information:** Displays contact information for support.

## Dependencies

- Python 3.x
- `stem` library
- `colorama` library                            
- `random2`library
- `logging4` library
- ` stem`library
- `colorama` library

## Before installation

- Update packages and upgrade repositories 
- `sudo apt update `.
- `sudo apt upgrade `.


## Use on Kali Linux

1. install tor ` sudo apt install tor `.

2. install TorVpn ` git clone https://github.com/Mohamed9x60/TorVpn.git `.

3. Enter the tool file ` cd TorVpn `.

4. Install dependencies using ` pip install -r requirements.txt `.
 
5. Run the script using ` sudo python3 PIF-PEONEI.py `.


## Use on Termux


1. install tor ` pkg install tor `.

2. install TorVpn ` git clone https://github.com/Mohamed9x60/TorVpn.git `.

3 .Enter the tool file ` cd TorVpn `.

4. Install dependencies using ` pip install -r requirements.txt `.
 
5. Run the script using ` python3 PIF-PEONEI.py `.



## Known Issues and Fixes

1. **OSError: Failed to start Tor service: reached  
'' the specified seconds'' timeout without success**: This error occurs when the script fails to start the Tor service within the specified timeout period. Check your internet connection, firewall settings, and ensure that Tor is allowed to connect to the internet
If the problem persists, execute this command ` pkill -f tor ` to kill the running Tor session .



## Contributors

- [Mohamed Fouad]([https://github.com/Mohamed9x60)]


## Video explanation

Uploading XRecorder_Edited_٠٥٠٣٢٠٢٤_١٥٠٣٢٥.mp4…

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

