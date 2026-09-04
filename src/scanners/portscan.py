import socket
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

class PortScan:
    def __init__(self, threads):
        # Limit threads
        self.threads = threads


    
    # Get a target IPv4 address
    def getIp(self, target):
        res = socket.getaddrinfo(target, None, socket.AF_INET)
        return res[2][4][0]

    

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

                print(f"{target}\t\t{port}/tcp is open {service}")

        # Port greater than 65535 Error
        except OverflowError:
            print(f"{target}\t\t{port}/tcp not found (Must be 0-65535)")



    # Scan with specific ports
    def specificPortsScan(self, host_target, ports):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        print(f"Starting port scan in {host_target}: {target_ip}")
        with ThreadPoolExecutor(max_workers= self.threads) as executor:
            for port in ports:
                executor.submit(self.checkPort, target=target_ip, port=port)



    # Scan default 1000 TCP ports
    def defaultPortScan(self, host_target):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        # Path to script
        script_dir = Path(__file__).parent

        # Opens the 1000 common ports file and performs a port scan.
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
            print(f"\nError: No such file or directory: {script_dir.parent}/wordlists/common-1000-ports.txt")
            print("Top 1000 common ports wordlist not found.")



    # Scan all ports
    def scanAllPorts(self, host_target):
        # Get a target IPv4
        target_ip = self.getIp(host_target)

        print(f"Starting port scan in {host_target}: {target_ip}")
        print("Checking all 65535 ports")

        # Control all threads
        with ThreadPoolExecutor(max_workers= self.threads) as executor:
            for port in range(65536):
                # Start a thread to check a port
                executor.submit(self.checkPort, target=target_ip, port=port)