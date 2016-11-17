import socket

HOST, PORT = '', 8888
#creating a socket
socket_basic = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_basic.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_basic.bind((HOST, PORT))
socket_basic.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = socket_basic.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
