# port_scanner.py
import socket
from datetime import datetime

# Target input
target = input("Enter target IP address or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

# Scan each port in range
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Timeout for connection attempt
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[*] Port {port} is OPEN")
    s.close()

end_time = datetime.now()
print(f"\n[+] Scan completed in {end_time - start_time}")
