# Python-Port-Scanner
A beginner Python port scanner for learning network enumeration. 

# Usage

```bash
python3 Port_Scanner.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
result = s.connect_ex((target, port))
if result == 0:
    print(f"[*] Port {port} is OPEN")
