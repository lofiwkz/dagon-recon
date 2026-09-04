import socket
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import sys

class PortScan:
    # Terminal Messages
    warning_mark = "\033[31m[ ! ]\033[0m"
    ok_mark = "\033[32m[ + ]\033[0m"
    interrupt_message = "\n\033[38;5;208m[!]\033[0m Scan interrupted by the user. See you later! :)"

    def __init__(self, threads, verbose = False):
        # Limit threads
        self.threads = threads
        self.verbose = verbose


    
    # Get a target IPv4 address
    def getIp(self, target):
        try:
            res = socket.getaddrinfo(target, None, socket.AF_INET)
            return res[2][4][0]
        except socket.gaierror:
            print(f"{self.warning_mark} Target [{target}] not known")
    

    # Get a possible service name in common wordlist
    def getService(self, port):
         # Path to script
        script_dir = Path(__file__).parent

        # Opens the 1000 common ports file
        try:
            with open(f"{script_dir.parent}/wordlists/common-1000-ports.txt") as file:
                ports_services = file.readlines()

                for line in ports_services:
                    line_port = line.split(":")[0]

                    # Check port and return your service
                    if line_port == str(port):
                        return line.split(":")[1].replace("\n", "")

        # Error: Wordlist common-1000-ports.txt not found
        except FileNotFoundError:
            return None



    # Check a single port and confirm whether it is open.
    def checkPort(self, target, port, service = None):
        # Create a socket and set timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)

        # Check port and print
        try:
            result = sock.connect_ex((target, port))
            sock.close()
            

            if result == 0:
                if service == None:
                    # Search for service name in wordlist
                    service = self.getService(port=port)
                    if service == None:
                        service = "unknow"

                print(f"{self.ok_mark} {target}\t\t{port}/tcp is \033[32mopen\033[0m {service}")
            else:
                if self.verbose:
                    print(f"[ - ] {target}\t\t{port}/tcp is closed")

        # Port greater than 65535 Error
        except OverflowError:
            print(f"{self.warning_mark} {target}\t\t{port}/tcp not found (Must be 0-65535)")



    # Scan with specific ports
    def specificPortsScan(self, host_target, ports):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        if target_ip != None:
            print(f"Starting port scan in {host_target}: {target_ip}")
        try:
            with ThreadPoolExecutor(max_workers= self.threads) as executor:
                for port in ports:
                    executor.submit(self.checkPort, target=target_ip, port=port)
        except KeyboardInterrupt:
            print(self.interrupt_message)

            executor.shutdown(wait=False, cancel_futures=True)
            sys.exit(0)



    # Scan default 1000 TCP ports
    def defaultPortScan(self, host_target):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        # Path to script
        script_dir = Path(__file__).parent

        # Opens the 1000 common ports file and performs a port scan.
        if target_ip != None:
            print(f"Starting port scan in {host_target}: {target_ip}")
            print("Scanning the 1000 common ports")
        try:
            with open(f"{script_dir.parent}/wordlists/common-1000-ports.txt") as file:
                ports_services = file.readlines()

                # Control all threads
                with ThreadPoolExecutor(max_workers= self.threads) as executor:
                    for line in ports_services:
                        port = line.split(":")[0]
                        service = line.split(":")[1].replace("\n", "")

                        executor.submit(self.checkPort, target=target_ip, port=int(port), service=service)

        # Error: File common-1000-ports.txt not found
        except FileNotFoundError:
            print(f"\n{self.warning_mark} No such file or directory: {script_dir.parent}/wordlists/common-1000-ports.txt")
            print(f"{self.warning_mark} Top 1000 common ports wordlist not found.")
        except KeyboardInterrupt:
            print(self.interrupt_message)

            executor.shutdown(wait=False, cancel_futures=True)
            sys.exit(0)



    # Scan all ports
    def scanAllPorts(self, host_target):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        if target_ip != None:
            print(f"Starting port scan in {host_target}: {target_ip}")
            print("Checking all 65535 ports")

        # Control all threads
        try:
            with ThreadPoolExecutor(max_workers= self.threads) as executor:
                for port in range(65536):
                    # Start a thread to check a port
                    executor.submit(self.checkPort, target=target_ip, port=port)
        
        except KeyboardInterrupt:
            print(self.interrupt_message)

            executor.shutdown(wait=False, cancel_futures=True)
            sys.exit(0)