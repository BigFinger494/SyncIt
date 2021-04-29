import os
import time
import zipfile
import hashlib
import json

class FileMeta:
    def __init__(self, name, contentHash, createTime, modifyTime, fileType ):
        self.name = name
        self.createTime = createTime
        self.modifyTime = modifyTime
        self.contentHash = contentHash
        self.fileType = fileType

    def getDict(self):
        return {'name': self.name, 'contentHash': self.contentHash, 'createTime': self.createTime, 'modifyTime': self.modifyTime, 'fileType': self.fileType }

#Получение списка файлов в директории и их метаданные
def get_information(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
       
        file_list.append([i,os.path.join(directory,i),time.ctime(a.st_atime),time.ctime(a.st_ctime),' md5Hashed']) #[file,most_recent_access,created]
    return file_list

# Упаковка списка файлов в один архив для передачи разом
def zip_Files(dirFiles, zip_name):
    print('This is files, that gonna be inside zip: ', dirFiles)
    with zipfile.ZipFile(zip_name, 'w') as file:
        for j in dirFiles:
            file.write(j[1])
            print(f'[+] {j[0]} zipped in')
        return file
    return 'error'

#Распакова архива
def unzip_File(zip_name, dir_to_Extract ):
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(dir_to_Extract)

def read_Bytes(file):
    with open(file, 'rb') as file_data:
        bytes_content = file_data.read()
        return bytes_content

def generateJSON(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
       
        fileMeta = FileMeta(i, 'md5Hashed',time.ctime(a.st_atime),time.ctime(a.st_ctime), 'file')
        file_list.append(fileMeta.getDict()) #[file,most_recent_access,created]
    to_json= json.dumps(file_list)
    with open('data.json', 'w') as outfile:
        json.dump(file_list, outfile)
    print('JSON',to_json)
    