# coding=utf-8
import socket #socket模块
import commands #执行系统命令模块
from HTTPRequest import HTTPRequest
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime
import urllib2
import httplib
import sys
callBack="""HTTP/1.1 200 OK
Date: Sat, 31 Dec 2005 23:59:59 GMT
Content-Type: text/html;charset=ISO-8859-1
Server: Microsoft-IIS/5.0\n"""
def getIp(domain):
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    return myaddr
def logCommand(data):
    commandLine=open("allCommand","a")
    commandLine.write(data)
    commandLine.close()
def getHttp(data):
    request = HTTPRequest(data)
    # print request.error_code       # None  (check this first)
    # print request.command          # "GET"
    print request.path             # "/who/ken/trust.html"
    # print request.request_version  # "HTTP/1.1"
    # print len(request.headers)     # 3
    # print request.headers.keys()   # ['accept-charset', 'host', 'accept']
    print request.headers['host']  # "cm.bell-labs.com"
    # print request.headers;
    ######
    # req = urllib2.Request(getIp(request.headers['host']),headers=request.headers)
    # for key in request.headers: 
    #     print key+":"+request.headers[key] 
    #     req.add_header(key, request.headers[key])
    # res = urllib2.urlopen("http://"+request.headers['host'])
    # res=urllib2.urlopen(req)
    # print res.info()
    # return res
    #####
    dictHeader={}#构造包头
    for key in request.headers: 
       dictHeader[key]=request.headers[key]
    conn = httplib.HTTPConnection(getIp(request.headers['host']))
    conn.request(request.command, request.path,"",dictHeader)
    r1 = conn.getresponse()
    # print r1.status, r1.reason
    returnData=str(request.request_version)+" "+str(r1.status)+" "+str(r1.reason)+"\n"+str(r1.msg)+"\n"+str(r1.read())
    # print "返回的数据包包头\n"+returnData
    # logCommand(returnData)
    return returnData
HOST='::1'
PORT=8888
addr = (HOST,PORT)
class Servers(SRH):
    def handle(self):
        self.request.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # print 'got connection from ',self.client_address
        # self.wfile.write('connection %s:%s at %s succeed!' % (HOST,PORT,ctime()))
        while True:
            data = self.request.recv(1024)
            if not data: 
                break
            # print data
            # print "RECV from ", self.client_address[0]
            self.request.sendall(getHttp(data))
print 'server is running....'
SocketServer.TCPServer.address_family=socket.AF_INET6
server = SocketServer.ThreadingTCPServer(addr,Servers)
server.serve_forever()

