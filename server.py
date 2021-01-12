import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print("Running the server on: {} and {}".format(args.host,args.port))
print("Welcome to the chatroom")
sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	sck.bind((args.host, args.port))
	sck.listen(1)
except Exception as e:
	raise SystemExit("We could not bind the server on host: {} to port: {}, because: {}".format(args.host,args.port,e))


def incoming_client(client, connection):
	ip = connection[0]
	port = connection[1]
	#print("THe new connection was made from IP: {}, and port: {}!".format(ip,port))
	name = client.recv(1024)		
	nameofc = name.decode()
	print("{} joined the chatroom".format(nameofc))
	while True:
		
		msg = client.recv(1024)
		
		message = msg.decode()
		l = message.split(":")
		if l[1] == 'exit':
			break
		print("Client {} : {}".format(l[0],l[1]))
		#reply = "{} : {}".format(l[0],l[1])
		#client.sendall(reply.encode('utf-8'))
	print("Client {} has diconnected!".format(nameofc))
	client.close()

while True:
	try: 
		client, ip = sck.accept()
		threading._start_new_thread(incoming_client,(client, ip))
		
	except KeyboardInterrupt:
		print("Gracefully shutting down the server!")

	except Exception as e:
		print("Well I did not anticipate this: {}".format(e))

sck.close()