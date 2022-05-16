#Server
from socket import *
serverPort = 12002
listeningSocket = socket(AF_INET, SOCK_STREAM)
listeningSocket.bind(('', serverPort))
listeningSocket.listen(1)
print('Server ready, socket', listeningSocket.fileno(), 'listening on localhost :', serverPort)
connectionSocket, addr = listeningSocket.accept() #client address & socket

while 1:
    msg = bytes.decode(connectionSocket.recv(1024))
    if(msg == 'exit'):
        connectionSocket.close()
        break
    print('Client says: ',msg)
    connectionSocket.send(str.encode(str(addr[0])+':'+str(addr[1])+':'+ msg))

connectionSocket.close()
