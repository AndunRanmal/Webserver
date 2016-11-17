import socket

host=''
port=8080

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.bind((host,port))
c.listen(1)
print 'Server run on port %s....' %port


while 1:
    csock,caddr = c.accept()
    cfile = csock.makefile('rw',0)

    line = cfile.readline().strip()

    cfile.write('HTTP/1.0 200  OK\n\n')
    cfile.write('<html><head><title>My First Web Server. It on port %s</title></head>')
    cfile.write('<body><h1>Follow the link</h1>')
    cfile.write('All the server needs to is deliver the text to the socket')
    cfile.write('It delivers the HTML code to the serveer')
    cfile.write('and the web browser converts it')
    cfile.write('<h3><a href="http://python.about.com/od/networkingwithpython/ss/PythonWebServer.htm#showall">click here</a></h3>')
    cfile.write('<p>This link direct you to get help to build a web server</p>')
    cfile.write('</body></html>')
    cfile.close()
    #csock.close()
    
    

    
                           
