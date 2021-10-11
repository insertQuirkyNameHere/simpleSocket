from socket import *

def createSocket():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        serverSocket.bind(("localhost", 9000))
        serverSocket.listen(5)

        while(1):
            (clientSocket, address) = serverSocket.accept()
            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")
            if(len(pieces) > 0):
                print(pieces[0])
            
            data = "HTTP/1.0 200 OK\r\n"
            data += "Contenet-type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello</body></html>"

            clientSocket.sendall(data.encode())
            clientSocket.shutdown(SHUT_WR)
    
    except Exception as ex:
        print("Shutting down")

    serverSocket.close()

print("Yo wazzup, created socket at http://localhost:9000")
createSocket()