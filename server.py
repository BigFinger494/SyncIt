import socketserver
import time
import threading
import socketserver
from socketserver import BaseRequestHandler
from Misc.fileUtilities import *
port = 1337

#Обработчик для общения и обработки команд
class EchoTCPHandlerForChat(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print('Address: {}'.format(self.client_address[0]))
        #print('Data: {}'.format(data.decode()))

        if(b'transfer' == data):
            print('Got response from client: ', data, data.decode())
            self.request.send(b'Ok')
        
        if(b'Hi' == data):
            print('Got response from client: ', data, data.decode())
            self.request.send(b'Hello there')


#TO-DO: Попробовать реализовать фабрику для многопоточной передачи нескольких файлов
# Обработчик для передачи файлов
class EchoTCPHandlerForTransfer(socketserver.BaseRequestHandler):
    def handle(self):
        #Путь, где создастся архив переданных файлов
        f = open(r'D:\destinationDir\aboba3zip.zip', 'wb')
        print('New Address Connected: {}'.format(self.client_address[0]))
        while True:
            recvfile = self.request.recv(1024)
                #print(recvfile)
            if not recvfile: break
            f.write(recvfile)
        f.close()
        unzip_File(r'D:\destinationDir\aboba3zip.zip', r'D:\destinationDir\extracted' )
        print('Done')
        #После этого должен производится опрос других подключенных машин для сравнения директорий
            



if __name__ == '__main__':
    launchme = socketserver.TCPServer(('', 8888), EchoTCPHandlerForChat)
    launchme2 = socketserver.TCPServer(('', 8889), EchoTCPHandlerForTransfer)

    t1 = threading.Thread(target=launchme.serve_forever)
    t2 = threading.Thread(target=launchme2.serve_forever)

    for t in t1, t2: t.start()
    for t in t1, t2: t.join()

