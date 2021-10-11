
from socket import *
mySocket = socket(AF_INET, SOCK_STREAM)
mySocket.connect(("localhost", 9000))
cmd = "GET http://localhost/this.html\r\n\r\n"
mySocket.send(cmd.encode())

while(True):
    data = mySocket.recv(50)
    if(len(data) < 1):
        break
    print(data.decode(), end="")
mySocket.close()