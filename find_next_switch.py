# Prep test data
output = ""

with open('mac.txt', 'r') as f:
    output = f.read()

# TODO: Account for potential (though unlikely) scenario where port-ch
# differs between separate lines in output.

current_port_channel = output.split()[-1]
print(current_port_channel)

# Will always start from net-r1
current_switch = "net-r1"

host_port_channels = ['Po14', 'Po22', 'Po23']

switch_ips = {
                         "neta-r2": "10.234.8.42",
                         "swa-r3": "10.234.8.43",
                         "swa-r4": "10.234.8.44",
                         "swa-r5": "10.234.8.45",
                         "swa-r6": "10.234.8.46",
                         "swa-r7": "10.234.8.47",
                         "netb-r1": "10.234.8.51",
                         "netb-r2": "10.234.8.52",
                         "swb-r3": "10.234.8.53",
                         "swb-r4": "10.234.8.54",
                         "swb-r5": "10.234.8.55",
                         "swb-r6": "10.234.8.56",
                         "swb-r7": "10.234.8.57",
                         }


if current_switch == 'net-r1':
     if current_port_channel == 'Po100':
          next_switch_ip = switch_ips['netb-r1']
     elif current_port_channel == 'Po12':
          next_switch_ip = switch_ips['neta-r2']
     elif current_port_channel.startswith('Po3'):
          next_switch_ip = switch_ips['neta-r3']
     elif current_port_channel.startswith('Po5'):
          next_switch_ip = switch_ips['neta-r5']
     elif current_port_channel.startswith('Po7'):
          next_switch_ip = switch_ips['neta-r7']
else:
     if current_port_channel = == 'Po100':
          next_switch_ip = switch_ips['netb-r1']
     elif current_port_channel == 'Po12':
          next_switch_ip = switch_ips['neta-r2']
     elif current_port_channel.startswith('Po3'):
          next_switch_ip = switch_ips['neta-r3']
     elif current_port_channel.startswith('Po5'):
          next_switch_ip = switch_ips['neta-r5']
     elif current_port_channel.startswith('Po7'):
          next_switch_ip = switch_ips['neta-r7']

# best way to determine next switch is to get cdp putput and hostname
# of port-channel remote end
