from argparse import ArgumentParser
from src.scanners import portscan

# Argparse Instance
parser = ArgumentParser("dagon.py [scantype] [target] [options...]\n\n")

# Script Arguments
parser.add_argument("scantype", nargs="?", default="pscan", help="Scan Type (pscan)")
parser.add_argument("target", help="Target address")
parser.add_argument("-p", "--ports", type=int, nargs="*", help="Ports that must be checked.")
parser.add_argument("-P", "--all-ports", action="store_true", help="Scan all 65535 ports.")
parser.add_argument("-t", "--threads", type=int, default=50 ,help="Limit number of threads to execution. ( Default: 50 )")
parser.add_argument("-v", "--verbose", action="store_true", help="Activate code verbosity")
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
    print("Dagon Scanner v0.2.3\n")
    # Define a scan type
    match args.scantype:
        case "pscan":
            portScan()
        case _:
            print("Invalid scan type. Use: 'pscan'")
            exit(0)

main()
