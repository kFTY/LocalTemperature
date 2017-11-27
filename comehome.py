import nmap
nm = nmap.PortScanner()


def CheckExist(ip_addr, port):
    nm.scan(ip_addr, port)
    return nm[ip_addr].state() == "up"


if CheckExist("192.168.1.4", "22"):
    print("YanDi is at home")

if CheckExist("192.168.1.5", "22"):
	print("Lajie is at home")
