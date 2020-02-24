while True:
    ip_address = input("Введите адрес: ")
    octets = ip_address.split(".")
    correct_ip = True

    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break
        if correct_ip:
            break
        print("Incorrect IPv4 address")

first_octet = int(octets[0])

if 1 <= first_octet <= 223:
    print("unicast")
elif 224 <= first_octet <= 239:
    print("multicast")
elif ip_address == "0.0.0.0":
    print("unassigend")
elif ip_address == "255.255.255.255":
    print("local broadcast")
else:
    print("unused")
