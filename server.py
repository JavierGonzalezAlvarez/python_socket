import socket

s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM) #| socket.SOCK_NONBLOCK)

HOST = "127.0.0.1"
PORT = 65432
address = (HOST, PORT)

'''
if socket.has_dualstack_ipv6():
    #server = socket.create_server(address, family=socket.AF_INET6, backlog=None, dualstack_ipv6=False)
else:
    server = socket.create_server(address, family=socket.AF_INET)
'''

print("type: ", socket.SocketType)
print("host name: ", socket.gethostname())
print("host name: ", socket.gethostbyname(HOST))
print(socket.getnameinfo(address, 3))

s.bind(address)
s.listen(5)

while True:
    conn, addr = s.accept()
    print("connected to: ", addr)
    data = conn.recv(10000)
    print(f"data received from client {data}")
    conn.sendall(data + b" - socket")
    conn.close()


