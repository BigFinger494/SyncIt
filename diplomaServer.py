import socket
import sys
import time
import zipfile
import os

port = 1337

def get_information(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
    return file_list

#print(get_information(r"C:\Users\Ayaz\Desktop\Александрийская библиотека\Треки для роксмит"))
ss = socket.socket()
print('[+] Server socket is created.')

ss.bind(('', port))
print('[+] Socket is binded to {}'.format(port))

ss.listen(5)
print('[+] Waiting for connection...')

con, addr = ss.accept()
print('[+] Got connection from {}'.format(addr[0]))

filename = con.recv(1024).decode()

f = open(filename, 'wb')
l = con.recv(1024)
while(l):
    f.write(l)
    l = con.recv(1024)
f.close()
print('[+] Received file ' + filename)

with zipfile.ZipFile(filename, 'r') as file:
    print('[+] Extracting files...')
    file.extractall('C:\\TestSync\\')
    print('[+] Done')

os.remove(filename)
con.close()
ss.close()