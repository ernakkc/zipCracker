from zipfile import ZipFile
from tqdm import tqdm
import os

banner = """
       _        ______                  _                
      (_)      / _____)                | |               
 _____ _ ____ | /       ____ ____  ____| |  _ ____  ____ 
(___  ) |  _ \| |      / ___) _  |/ ___) | / ) _  )/ ___)
 / __/| | | | | \_____| |  ( ( | ( (___| |< ( (/ /| |    
(_____)_| ||_/ \______)_|   \_||_|\____)_| \_)____)_|    
        |_|                                              
"""
print(banner)


dosya = input("Zip Dosyasının Konumunu Giriniz:  ")
wordlist = input("Wordlist Dosyasının Konumunu Giriniz:   ")

if not dosya.endswith(".zip"):
    exit("Zip Dosyası Girmelisiniz...")
if not wordlist.endswith(".txt"):
    exit("Wordlist dosyası .txt şeklinde bitmelidir...")

# Zip Dosyası Tanıma
try:
    zip_file = ZipFile(dosya)
except FileNotFoundError:
    exit("Dosyaları kontrol ederek tekrar deneyin...")
    
    
os.system("cls")
print(banner , "\n\n\n")
# Password Sayısı
try:
    n_words = len(list(open(wordlist, "rb")))
    print("Denenecek Password Sayısı:", n_words , "\n")
except FileNotFoundError:
    exit("Dosyaları kontrol ederek tekrar deneyin...")


# Password Deneme
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="kelime"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\n[+] Şifre Bulundu:", word.decode().strip())
            exit(0)
print("\n[!] Şifre bulunamadı, başka wordlist deneyin.")
    
