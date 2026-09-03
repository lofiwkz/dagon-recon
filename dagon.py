from argparse import ArgumentParser
from src.scanners import portscan

# Argparse Instance
parser = ArgumentParser("dagon.py [scantype] [target] [options...]\n\n")

# Script Arguments
parser.add_argument("scantype", nargs="?", default="pscan", help="Scan Type (pscan)")
parser.add_argument("target", help="Target address")
parser.add_argument("-p", "--ports", type=int, nargs="*", help="Ports that must be checked.")
args = parser.parse_args()

# Instances
portscan = portscan.PortScan()

def portScan():
    # Specifc ports
    if args.ports != None:
        portscan.specificPortsScan(target=args.target, ports=args.ports)
    else:
        portscan.defaultPortScan(target=args.target)
        #print('Please, use "-p [port port ...]" to specif ports')
        #exit(0)

# Main function
def main():
    print("Dagon Scanner v0.2.0\n")
    # Define a scan type
    match args.scantype:
        case "pscan":
            portScan()
        case _:
            print("Invalid scan type. Use: 'pscan'")
            exit(0)

main()
