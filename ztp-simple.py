import cli
from cli import configurep
from cli import executep

print "\n\n *** Sample ZTP Day0 Python Script *** \n\n"
cli.configurep(["hostname JCOHOE-9840-ZTP"])
print "Configure vlan interface, gateway, aaa, and enable netconf-yang\n\n"
cli.configurep(["int GigabitEthernet0", "ip address 10.85.134.78 255.255.255.192", "no shut", "end"])
cli.configurep(["username admin privilege 15 secret 0 Cisco123"])
cli.configurep(["aaa new-model", "aaa authentication login default local", "end"])
cli.configurep(["aaa authorization exec default local", "aaa session-id common", "end"])
cli.configurep(["netconf-yang", "end"])
cli.configurep(["ip http secure-server", "restconf", "end"])
cli.configurep(["line vty 0 15", "transport input all", "exec-timeout 0 0", "end"])
print "\n\n *** Executing show ip interface brief  *** \n\n"
cli_command = "sh ip int brief"
cli.executep(cli_command)
print "\n\n *** ZTP Day0 Python Script Execution Complete *** \n\n"
