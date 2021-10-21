import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_minimum = 0
port_maksimum = 65535
open_ports = []

while True:
    ip_add_entered = input("\n Taramak istediğiniz ip adresini girin: ")
    
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
       
        break
    except:
        print("Geçersiz bir ip adresi girdiniz")
    

while True:

    print("Lütfen taramak istediğiniz bağlantı noktası aralığını şu biçimde girin: (ör. 60-120 )")
    port_range = input("Bağlantı noktası aralığını girin: ")

    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:

        port_min = int(port_range_valid.group(1))

        port_max = int(port_range_valid.group(2))
        break


for port in range(port_minimum, port_maksimum + 1):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           s.settimeout(0.5)
          s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
        pass

for port in open_ports:
    print(f"Port {port} açık {ip_add_entered}."