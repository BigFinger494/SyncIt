from pathlib import Path
import zipfile
import os, time

result = list(Path(r"C:\TestSync").rglob("*.*"))
file_list = []
zipFile = zipfile.ZipFile(r'C:\archive.zip', 'w')

for i in result:
    a = os.stat(i)
    file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)])
    zipFile.write(i)
zipFile.close()

print(file_list)