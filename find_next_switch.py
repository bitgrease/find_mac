# Prep test data
output = ""
with open('mac.txt', 'r') as f:
    output = f.read()


host_port_channels = ['Po14', 'Po22', 'Po23']

switch_ips = {
                         "neta-r2": "10.234.8.42",
                         "swa-r3" : "10.234.8.43",
                         "swa-r4" : "10.234.8.44",
                         "swa-r5" : "10.234.8.45",
                         "swa-r6" : "10.234.8.46",
                         "swa-r7" : "10.234.8.47",
                         "netb-r1": "10.234.8.51",
                         "netb-r2": "10.234.8.52",
                         "swb-r3" : "10.234.8.53",
                         "swb-r4" : "10.234.8.54",
                         "swb-r5" : "10.234.8.55",
                         "swb-r6" : "10.234.8.56",
                         "swb-r7" : "10.234.8.57",
                         }

# best way to determine next switch is to get cdp putput and hostname of port-channel
# remote end
