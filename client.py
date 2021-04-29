import socket
import sys
import zipfile
import os
import time
from Misc.fileUtilities import *

dir = r'C:\Users\Ayaz\Desktop\Александрийская библиотека\Треки для роксмит\\'
dirFiles = get_information(r"C:\Users\Ayaz\Desktop\Александрийская библиотека\Треки для роксмит")
generateJSON(dir)
os.chdir(dir)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8888))
commandString = input('Enter command: ')
sock.sendall(commandString.encode())


answer = sock.recv(1024).decode().strip()
print('Server answered: ', answer)
if(answer == 'Ok'):
    sockFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockFile.connect(('127.0.0.1',8889))

    zip_Files(dirFiles,'aboba2zip.zip')
    readFile = open('aboba2zip.zip','rb')

    readBytes = readFile.read()
    readFile.close()
    sockFile.sendall(readBytes)
    os.remove('aboba2zip.zip')

sock.close()
