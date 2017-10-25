import csv

class Firewall(object):
    data = {}

    def __init__(self, csv):
        self.initStorage()
        with open(csv) as data:
            for row in data:
                newlineIndex = row.find("\n")
                if newlineIndex != -1:
                    row = row[:newlineIndex]
                direction, protocol, port, ip = row.split(",")
                portDict = self.data[direction][protocol]
                if port in portDict:
                    self.data[direction][protocol][port] += [ip]
                else:
                    self.data[direction][protocol][port] = [ip]
                    
    def accept_packet(self, direction, protocol, port, ip_address):
        try:
            ports = self.data[direction][protocol]
        except KeyError:
            return False
        for portVal, ips in ports.items():
            if self.checkPort(port, portVal):
                for ip in ips:
                    if self.checkIP(ip_address, ip):
                        return True
        return False

    def initStorage(self):
        self.data["inbound"] = {}
        self.data["outbound"] = {}
        self.data["inbound"]["tcp"] = {}
        self.data["inbound"]["udp"] = {}
        self.data["outbound"]["tcp"] = {}
        self.data["outbound"]["udp"] = {}

    def checkPort(self, port, firewallPort):
        rangeIndex = firewallPort.find("-")
        if rangeIndex == -1:
            firewallPort = int(firewallPort)
            return port == firewallPort
        else:
            minBound = int(firewallPort[:rangeIndex])
            maxBound = int(firewallPort[rangeIndex+1:])
            return minBound <= port and port <= maxBound

    def checkIP(self, ip, firewallIP):
        rangeIndex = firewallIP.find("-")
        if rangeIndex == -1:
            return ip == firewallIP
        else:
            minBound = firewallIP[:rangeIndex]
            minBound = int(minBound.replace(".", ""))
            maxBound = firewallIP[rangeIndex+1:]
            maxBound = int(maxBound.replace(".", ""))
            ip = int(ip.replace(".",""))
            return minBound <= ip and ip <= maxBound
