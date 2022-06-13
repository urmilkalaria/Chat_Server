from distutils.command.build_scripts import first_line_re
import socket
import threading


def run():

    host = "192.168.214.67"  
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = []
    client_addr = {}

    def broadcast(message, friend):
        for client in clients:
            if client == friend:
                client.send(message)

    def handle(client, friend, address):

        while True:

            try:

                message = client.recv(1024)
                broadcast(message, friend)
            except:

                try:
                    clients.remove(client)
                    friend.send('Friend left!'.encode('utf-8'))
                    friend.send('Disconnect'.encode('utf-8'))
                    client.close()
                    # print(str(address)+' left')

                    # friend.close()
                    break
                except:
                    break

    def onlinereq(client, fname, address):
        while True:
            if fname in client_addr.values():
                break
        client.send('Friend online'.encode('utf-8'))
        friend = list(client_addr.keys())[
            list(client_addr.values()).index(fname)]
        thread = threading.Thread(
            target=handle, args=(client, friend, address,))
        thread.start()

    def receive():
        while True:
            client, address = server.accept()
            print("Connected with {}".format(str(address)))
            client.send('FName'.encode('utf-8'))
            fname = client.recv(1024).decode('utf-8')

            clients.append(client)

            client_addr[client] = address[0]
            client.send("Waiting for friend to be online".encode('utf-8'))
            thread1 = threading.Thread(
                target=onlinereq, args=(client, fname, address,))
            thread1.start()

    receive()
