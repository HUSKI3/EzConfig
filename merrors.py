import time
point = "•"
class merror:
  def __init__(self):
    self.errors = []
  def error(self,msg):
    print("\u001b[31m",point,f"[ERROR] {msg}")
    self.errors+=["Error",msg,time.strftime("%H:%M:%S", time.localtime())]
  def bigpanik(self): 
    print("\u001b[31m",point,f"[PANIC] The program could not handle the request")
    self.errors+=["Panic",time.strftime("%H:%M:%S", time.localtime())]
  def getall(self):
    return self.errors
#USAGE
#error("Could not load anything oopsie")