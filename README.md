## Tor VPN  *PIF PEONEI* Changer

PIF-PEONEI script allows you to change your IP address using the Tor network. It runs a VPN session that changes the IP address at regular intervals that you specify.

## Features 
- **Starting the Tor Service:** Initiates the Tor service to establish a connection with the Tor network.
- **Change IP Address:** Updates the IP address using the Tor network.
- **Run VPN Session:** Initiates a VPN session with customizable duration and time interval between IP changes.
- **Show Contact Information:** Displays contact details for support. It also saves the IP address you used in a file named temp_ip.txt.

## Dependencies

- Python 3.x
- `stem` library
- `colorama` library                            
- `random2`library
- `logging4` library
- `stem`library
- `colorama` library
- `socket`library

## Do you need the tor package to run this. Instal tor first!
> DEBIAN:
              
          apt update && apt upgrade && apt install tor torsocks -y
> GENTOO: 
       
          emerge tor torsocks

> ARCH: 
          
         pacman tor torsocks -Syu

> OPENSUSE: 
          
   
         zypper install tor torsocks -y `

## Install repositories Kali Linux


    git clone https://github.com/Mohamed9x60/TorVpn.git
    cd TorVpn
    pip install -r requirements.txt
    sudo python3 PIF-PEONEI.py
    
    


## Install repositories on Termux

    git clone https://github.com/Mohamed9x60/TorVpn.git
    cd TorVpn
    pip install -r requirements.txt
    python3 PIF-PEONEI.py
    


## Known Issues and Fixes

1. **OSError: Failed to start Tor service: reached  
'' the specified seconds'' timeout without success**: This error occurs when the script fails to start the Tor service within the specified timeout period. Check your internet connection, firewall settings, and ensure that Tor is allowed to connect to the internet. If the problem persists, execute this command `pkill -f tor` to kill the running Tor session.

**additional**

**Command to kill all running Tor sessions:**

```
pkill -9 tor
```

**Explanation of the command:**

* **pkill:** A tool for killing processes.
* **-9:** A strong kill signal sent to all running Tor processes.
* **tor:** The name of the process you want to kill.

**Notes:**

* This command will kill all running Tor sessions, including those running in the background.
* This command may not work on some operating systems.

**Alternatives:**

* You can use the task manager to kill Tor sessions manually.
* You can use a tool like `ps aux | grep tor` to list all running Tor processes and then use `kill` or `killall` to kill them.

**Tips:**

* If you are having problems with Tor, try restarting it using the command `service tor restart`.
* You can also use the command `tor --version` to check the version of Tor you are using.
* If you need further assistance, you can visit the [Tor](https://www.torproject.org/)





## Contributors

- [Mohamed Fouad](https://github.com/Mohamed9x60)
- [Facebook](https://www.facebook.com/profile.php?id=100014784496206&mibextid=ZbWKwL)
## Screenshot

![Screenshot_٢٠٢٤٠٣٠٥-١٥٢٦٣٧_Termux](https://github.com/Mohamed9x60/TorVpn/assets/162137526/0c75391c-016b-4bee-b946-f9a9d713b473)




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
