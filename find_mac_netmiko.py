from netmiko import ConnectHandler
import sys

output = ""
# if len(sys.argv) < 3:
#     sys.exit("Must provide IP and MAC as arguments")

# ip, mac = sys.argv[1:3]
ip = "10.234.8.230"
mac = "1234"
password = "test"
try:
    net_connect = ConnectHandler(device_type='cisco_ios', host=ip,
                                 username='scnetter',password='test')

    output = net_connect.send_send_command(f"sho mac addr | i {mac}")
except Exception as e:
    print(f'Error occured connectiong to {ip}')

print(output)
