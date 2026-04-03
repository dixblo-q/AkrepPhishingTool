#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

def install_package(package):
    """Paketi yükler"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[+] {package} başarıyla kuruldu")
        return True
    except:
        print(f"[-] {package} kurulamadı")
        return False

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🦂 AKREP PHISHER - KURULUM SCRIPT 🦂           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    # Gerekli paketler
    packages = [
        "requests",
        "flask",
        "colorama",
        "pyngrok",
        "termcolor",
        "python-dotenv"
    ]
    
    print("[*] Gerekli paketler kuruluyor...\n")
    
    installed = 0
    failed = 0
    
    for package in packages:
        if install_package(package):
            installed += 1
        else:
            failed += 1
    
    print(f"\n[+] Kurulum tamamlandı!")
    print(f"[+] Başarılı: {installed}")
    print(f"[-] Başarısız: {failed}")
    
    # Ngrok kontrolü
    print("\n[*] Ngrok kontrol ediliyor...")
    try:
        subprocess.run(['ngrok', '--version'], capture_output=True)
        print("[+] Ngrok zaten kurulu")
    except:
        print("[-] Ngrok bulunamadı!")
        print("[*] Ngrok kurulumu için: https://ngrok.com/download")
        print("[*] veya 'pip install pyngrok' ile devam edin")
    
    # Ana script'in çalıştırılabilir yapılması
    if os.name == 'posix':  # Linux/Mac
        try:
            subprocess.run(['chmod', '+x', 'akrep.py'])
            print("[+] akrep.py çalıştırılabilir yapıldı")
        except:
            pass
    
    print("\n[✓] Kurulum tamamlandı!")
    print("[*] Çalıştırmak için: python3 phisher.py")
    print("[*] veya: ./phisher.py")

if __name__ == "__main__":
    main()
