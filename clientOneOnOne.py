import os
import socket
import threading
import file_server
import file_client
import time

# This portion will identify the Client info who is getting connected.

nickname = input("Enter Name: ")
FNAME = input("Enter friend's IP: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('#', $)) # Enter Server's IP Address at '#' and port number at $

# Make sure to use the IP on which both clients and server be connected over the same network. This will work when both the clients and server are connected to same network only.

# Recv function

def receive():
    while True:
        message = client.recv(1024).decode('utf-8')

        if message == 'FName':
            client.send(FNAME.encode('utf-8'))
        elif message == 'Disconnect':
            print("Disconnected")
            os._exit(0)

        elif message == "FR":
            fr_thread = threading.Thread(
                target=file_server.rec)
            fr_thread.start()

        else:
            print(message)

# Write Function

def write():
    while True:
        k = input('')
        if k == "FS":
            try:
                message = "FR"
                client.send(message.encode('utf-8'))

                time.sleep(3)
                f = input('Input filename: ')
                fs_thread = threading.Thread(
                    target=file_client.send, args=(FNAME, f))
                fs_thread.start()
            except:
                print("Cannot send file")
        else:
            message = '{}: {}'.format(nickname, k)
            client.send(message.encode('utf-8'))

# Here threads are use so that multiple messages can be exchanged between clients.

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
