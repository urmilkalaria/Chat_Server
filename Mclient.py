import socket
import threading

nickname = input("Enter Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.214.67', 1234)) # IP address of client and portnumber 


def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        if message == 'Name':
            client.send(nickname.encode('utf-8'))
        else:
            print(message)


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
