import socket

serversocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port = 9999

serversocket.bind((host,port))
#queue upto 5 request
serversocket.listen(5)

while True:
    #establish a connection
    clientsocket, addr=serversocket.accept()

    msg = 'Thankyou for connecting'
    clientsocket.send(msg.encode())
    clientsocket.close()
