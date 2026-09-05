from argparse import ArgumentParser, HelpFormatter
from src.scanners import portscan

# Project Version
version = "v0.2.5"
print(f"Dagon Scanner {version}")

# Custom Formatter for help spacing
class CustomFormatter(HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=100)

# Argparse Instance
parser = ArgumentParser(
    description="A CLI tool for network scanning and reconnaissance", 
    usage="dagon.py [scantype] [target] [options...]",
    formatter_class=CustomFormatter
)

# Script Main Arguments
parser.add_argument("scantype", nargs="?", default="pscan", help="Scan Type (pscan: Port Scan)")
parser.add_argument("target", help="Target IPv4 address or domain")
parser.add_argument("-t", "--threads", type=int, default=50 ,help="Limit number of threads to execution. ( Default: 50 )")
parser.add_argument("-v", "--verbose", action="store_true", help="Activate code verbosity")

# Script Arguments Groups
#Port Scan
pscan_group = parser.add_argument_group(title="Port Scan",description="Arguments options for scantype: pscan")
pscan_group.add_argument("-p", "--ports", type=int, nargs="*", help="Ports that must be checked.")
pscan_group.add_argument("-P", "--all-ports", action="store_true", help="Scan all 65535 ports.")

args = parser.parse_args()

# Instances
portscan = portscan.PortScan(threads=args.threads, verbose=args.verbose)

def portScan():
    # Specifc ports
    if args.ports != None:
        portscan.specificPortsScan(host_target=args.target, ports=args.ports)
    elif args.all_ports:
        portscan.scanAllPorts(host_target=args.target)
    else:
        portscan.defaultPortScan(host_target=args.target)

# Main function
def main():
    # Define a scan type
    match args.scantype:
        case "pscan":
            portScan()
        case _:
            print("Invalid scan type. Use: 'pscan'")
            exit(0)

main()
