import time
def follow(f):
  f.seek(0,2)
  while True:
    line = f.readline()
    if not line:
      time.sleep(0.1)
      continue
    yield line

def parseName(line):
  return line.split("name=",1)[1].split(" id=",1)[0]
def parseTarget(line):
  return line.split("Target=[name=",1)[1].split(" id=",1)[0]
def parseTag(line):
  return line.split("tag=",1)[1].split(" value=",1)[0]

def getSeek(logfile):
  logfile.seek(0,2)
  line = ''
  count = 0
  while True:
    logfile.seek(-1, 1)
    pos = logfile.tell()
    if logfile.read(1) == '\n':
      line = logfile.readline()
      logfile.seek(pos-1)
    else:
      logfile.seek(-1,1)
    if ("Unloading" in line and "Unused Serialized files" in line):
      count+=1
    if count > 2:
      break
  return logfile.tell()

'''def updateEntity(board, line):
  if "Entity=[" in line
    idnfo = line.split("Entity=[", 1)[1].split("] tag=", 1)[0]
    
  elif
    #check special Entity
    idnfo = line.split("Entity=",1)[1].split(" ",1)[0]'''
  