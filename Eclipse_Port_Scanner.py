import socket
import concurrent.futures
import os

os.system("color")
socket.setdefaulttimeout(1)

closed = 0

def isOpen(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, int(port)))
        return True
    except (socket.timeout, socket.error):
        return False

openPorts = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def scan_ports(ip, port):
    if isOpen(ip, port):
        print(bcolors.OKGREEN + f"[OPEN] {port}")

if __name__ == "__main__":
    print(bcolors.OKCYAN + "######## Eclipse port scanner ########")
    ip = input(bcolors.OKBLUE + "Enter host ip: ")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        futures = [executor.submit(scan_ports, ip, port) for port in range(0, 65535)]

        concurrent.futures.wait(futures)
    print(bcolors.HEADER + "! FINISHED !")
    while True:
        input("")