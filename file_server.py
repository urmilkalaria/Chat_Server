import socket

# Recv Function

def rec():
    IP = '192.168.214.67'  # your own ip
    PORT = 1234	# predefined port number
    ADDR = (IP, PORT)
    SIZE = 1024
    FORMAT = "utf-8"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(ADDR)

    server.listen()
    print("WAITING FOR FILE")
    while True:

        conn, addr = server.accept()

        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))
        data = conn.recv(SIZE).decode(FORMAT)
        print("Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))
        print("File Recived")
        file.close()
        conn.close()

        return
