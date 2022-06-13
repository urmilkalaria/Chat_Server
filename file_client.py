import socket
import os

# Send Function

def send(friendip, filen):

    FORMAT = "utf-8"
    SIZE = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((friendip, 6200))

    script_dir = os.path.dirname(__file__)

    abs_file_path = os.path.join(script_dir, filen)
    file = open(
        abs_file_path, "r")
    data = file.read()
    client.send(filen.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    file.close()
    client.close()
    print("File Sent")
    return
