import nmap
nm = nmap.PortScanner()


def CheckExist(ip_addr, port):
    nm.scan(ip_addr, port)
    return nm[ip_addr].state() == "up"


if CheckExist("192.168.1.1", "22"):
    print("R7000 is at home")
