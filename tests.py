from Firewall import Firewall

fw = Firewall("test.csv")

print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))

#Incorrect parameter
print(fw.accept_packet("outbound", "tc", 10234, "192.168.10.11"))
#Test inclusivity
print(fw.accept_packet("outbound", "tc", 10000, "192.168.10.11"))
#Repeated port, different IP
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.4"))
#Inclusivity of ip
print(fw.accept_packet("inbound", "udp", 53, "192.168.1.1"))
