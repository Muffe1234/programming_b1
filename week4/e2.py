devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]
risky_ports = [21, 23, 3389]

for ip, ports in devices:
    for port in ports:
        if port in risky_ports:
            print(f"ip {ip} hat riskanten port {port}")