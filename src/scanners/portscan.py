import socket
from pathlib import Path

class PortScan:

    # Get a target IPv4 address
    def getIp(self, target):
        res = socket.getaddrinfo(target, None, socket.AF_INET)
        return res[2][4][0]

    # Check a single port and confirm whether it is open.
    def checkPort(self, target, port) -> bool:
        # Create a socket and set timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)

        # Check port and print
        try:
            result = sock.connect_ex((target, port))

            sock.close()

            if result == 0:
                return True
            else:
                return False
        except OverflowError:
            print(f"{target}\t\t{port}/tcp not found (Must be 0-65535)")
            return

    # Scan with specific ports
    def specificPortsScan(self, target, ports):
        target_ip = self.getIp(target)

        print(f"Starting port scan in {target}: {target_ip}")
        for port in ports:
            result = self.checkPort(target=target_ip, port=port)

            if result:
                print(f"{target_ip}\t\t{port}/tcp is open")
            elif result == False:
                print(f"{target_ip}\t\t{port}/tcp is closed")
        pass

    # Scan with 1000 TCP ports
    def defaultPortScan(self, target):
        target_ip = self.getIp(target)

        # Path to script
        script_dir = Path(__file__).parent

        # Opens the 1000 common ports file and performs a port scan.
        print(f"Starting port scan in {target}: {target_ip}")
        print("Scanning the 1000 common ports")
        try:
            with open(f"{script_dir.parent}/wordlists/common-1000-ports.txt") as file:
                ports_services = file.readlines()

                for line in ports_services:
                    port = line.split(":")[0]
                    service = line.split(":")[1].replace("\n", "")

                    result = self.checkPort(target=target_ip, port=int(port))

                    if result:
                        print(f"{target_ip}\t{port}/tcp open {service}")
                    elif result == False:
                        pass
        except FileNotFoundError:
            print(f"\nError: No such file or directory: {script_dir.parent}/wordlists/common-1000-ports.txt")
            print("Top 1000 common ports wordlist not found.")