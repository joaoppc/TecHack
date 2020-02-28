import socket
import sys



def port_scan(ip,port,protocol):
	try:
		socket.setdefaulttimeout(5)
		s = socket.socket()
		s.connect((ip,port))
		service =socket.getservbyport(port,protocol)

		return 'open',service
	except:
		return 'closed'

def main():
	ip = input('enter the ip you want to scan:')
	portStart = int(input('Enter the range of ports:\n start:'))
	portEnd = int(input('end:'))
	protocol = input('Enter protocol tcp or udp:')
	for port in range(portStart,portEnd): 
		scan = port_scan(ip,port,protocol)
		if scan != 'closed':
			print(scan,port)
	print((portEnd - portStart) + 'ports scanned')
if __name__ == '__main__':
	main()