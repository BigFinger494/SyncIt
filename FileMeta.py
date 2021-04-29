import hashlib

class FileMeta(object):
  def __init__(self, name, contentHash, createTime, modifyTime, fileType ):
    self.name = name
    self.createTime = createTime
    self.modifyTime = modifyTime
    self.contentHash = contentHash
    self.fileType = fileType

  def getDict(self):
    return {'name': self.name, 'contentHash': self.contentHash, 'createTime': self.createTime, 'modifyTime': self.modifyTime, 'fileType': self.fileType }