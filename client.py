import socket

#  class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM) #| socket.SOCK_NONBLOCK)

HOST = "127.0.0.1"
PORT = 65432
address = (HOST, PORT)

#connection = socket.create_connection(address, timeout=12, all_errors=True)
connection = socket.create_connection(address, all_errors=True)

with connection as con:
    con.send(b"hello world ")

    filename: str = 'data: '
    con.send(filename.encode())

    #send data in the csv
    with open('data', 'rb') as f:
        data = f.read(10000)
        while data:
            con.sendall(data)
            data = f.read(1024)

    data = con.recv(10000)
    print(f"Received from server {data!r}")
    con.close()