import socket
import threading


def run():

    host = "192.168.214.67"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = []
    names = []

    def broadcast(message):
        for client in clients:
            client.send(message)

    def handle(client):
        while True:

            try:

                message = client.recv(1024)
                broadcast(message)
            except:

                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = names[index]
                broadcast('{} left!'.format(nickname).encode('utf-8'))
                names.remove(nickname)
                break

    def receive():
        while True:
            client, address = server.accept()
            print("Connected with {}".format(str(address)))

            client.send('Name'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            names.append(nickname)
            clients.append(client)

            print("Nickname is {}".format(nickname))
            broadcast("{} joined!".format(nickname).encode('utf-8'))
            client.send('Connected to server!'.encode('utf-8'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

    receive()
