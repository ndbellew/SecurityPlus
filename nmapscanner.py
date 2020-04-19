import nmap
import sys

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080] #popular ports

scan_v = nmap.PortScanner() #Scan Variable

print(f"Scanning {target} for ports {ports} ")

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print(f"Port: {port} is {portscan['scan'][target]['tcp'][port]['state']}")

print(f"HOST: {target} is {portscan['scan'][target]['status']['state']}")
