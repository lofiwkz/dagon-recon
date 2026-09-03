import socket

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
        targetIp = self.getIp(target)

        print(f"Starting port scan in {target}: {targetIp}")
        for port in ports:
            result = self.checkPort(target=targetIp, port=port)

            if result:
                print(f"{targetIp}\t\t{port}/tcp is open")
            elif result == False:
                print(f"{targetIp}\t\t{port}/tcp is closed")
        pass
    

    def teste(self):
        print("Hello!")