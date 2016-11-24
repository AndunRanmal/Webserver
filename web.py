import socket

host=''
port=8080

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.bind((host,port))
c.listen(1)
print 'Server run on port %s....' %port


#f= open("index.html","rb")

def get(path):
    if (path == "/"):
        path="/index.html"
    
    sendReply = False
    if path.endswith(".html"):
        mimetype="text/html"
        sendReply =True
    if path.endswith(".PNG"):
        mimetype="image/png"
        sendReply =True
    if path.endswith(".jpg"):
        mimetype="image/jpg"
        sendReply =True
    if path.endswith(".gif"):
        mimetype="image/gif"
        sendReply =True
    if path.endswith(".js"):
        mimetype="application/javascript"
        sendReply =True
    if path.endswith(".css"):
        mimetype="text/css"
        sendReply =True

    if sendReply ==True:

        try:
            f = open(path[1:], 'rb')
            response = "HTTP/1.1 200 OK\n\r"
            response += "Content-Type: %s\n\r" % mimetype
            response +="Connection: keep-alive"
            response +="\n\r\n\r"
            
                #self.send_header('Content-type',mimetype)
                #self.end_header()
                #self.wfile.write(f.read())
            response +=f.read()
            csock.send(response)
                
            
        except IOError:
            csock.send("HTTP/1.1 404 File Not Found %s" %path)

while True:
    csock,caddr = c.accept()
    request=csock.recv(1024)
    line = request.split()
    command, path = line[0], line[1]
    print path, command
    get(path)

    

   # http_response = "HTTP/1.1 200  OK \r\n" +"Contetn-type:text/html"
    #http_response= f.read()



    #csock.sendall(response)
    #csock.close
    
