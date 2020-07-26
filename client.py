import socket 
import argparse

parser = argparse.ArgumentParser(description = "This is the client for the multi threaded socket server!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print("Connecting to server: {} on port: {}".format(args.host,args.port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
	try:
		sck.connect((args.host, args.port))
	except Exception as e:
		raise SystemExit("We could not bind the server on host: {} to port: {}, because: {}".format(args.host,args.port,e))

	name=input("Enter name: ")
	nameofc=name.encode('utf-8')
	sck.sendall(name.encode('utf-8'))
	while True:
               	msg = input("Enter your message : ")
               	msg = name+":"+msg
                message = msg.encode('utf-8')
                l = msg.split(":")
                sck.sendall(msg.encode('utf-8'))
                if l[1] =='exit':
                    print("You said goodbye!")
                    break
                #data = sck.recv(1024)
                #print("The server's response was: {}".format(data.decode()))