import socket

def socketLoginChecker():

    bind_ip = socket.gethostname()
    bind_port = 9999

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((bind_ip,bind_port))
    server.listen(5)

    print("[*] Listening on "+bind_ip,bind_port)

    while True:
        client,addr = server.accept()
        print('Connected by '+str(addr))

        while True:
            data = client.recv(1024)
            print("Client recv data:"+str(data))
            client.send("ACK！".encode())
            return data
