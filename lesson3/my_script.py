ip_addr = input("Enter IP address: ")
if not ip_addr:
    ip_addr = "10.10.10.10"
for octet in ip_addr.split("."):
    print(octet)
