# Tor VPN <..PIF PEONEI..> Changer

PIF-PEONEI script allows you to change your IP address using the Tor network. It runs a VPN session that changes the IP address at regular intervals that you specify.

## Features 
- **Starting the Tor Service:** Starts the Tor service to establish a connection with the Tor network. - **Change IP Address:** Change the IP address using the Tor network. - **Play VPN Session:** Launch a VPN session with a customizable duration and time interval between IP changes. - **Show contact information:** Displays contact information for support. It saves the IP you used in a file called temp_ip.txt



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

4.Install dependencies using ` pip install -r requirements.txt `.
 
5. Run the script using ` sudo python3 PIF-PEONEI.py `.


## Use on Termux


1. install tor ` pkg install tor `.

2. install TorVpn ` git clone https://github.com/Mohamed9x60/TorVpn.git `.

3.Enter the tool file ` cd TorVpn `.

4.Install dependencies using ` pip install -r requirements.txt `.
 
6. Run the script using ` python3 PIF-PEONEI.py `.



## Known Issues and Fixes

1. **OSError: Failed to start Tor service: reached  
'' the specified seconds'' timeout without success**: This error occurs when the script fails to start the Tor service within the specified timeout period. Check your internet connection, firewall settings, and ensure that Tor is allowed to connect to the internet
If the problem persists, execute this command ` pkill -f tor ` to kill the running Tor session .



## Contributors

- [ Mohamed Fouad ]([ https://github.com/Mohamed9x60 ])

## Screenshot

![Screenshot_٢٠٢٤٠٣٠٥-١٥٢٦٣٧_Termux](https://github.com/Mohamed9x60/TorVpn/assets/162137526/0c75391c-016b-4bee-b946-f9a9d713b473)



## Video explanation





Uploading XRecorder_Edited_٠٥٠٣٢٠٢٤_١٥٠٣٢٥.mp4…





## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

