<h1 font size="18"> JSPConverter </h1><br>
JSP Converter programı, basitçe ffmpeg modülünü kullanarak ses formatları içerisinde (mp4,mp3,ogg,wav) dönüşüm yapan, dönüşüm yaparken de kalitesini belirleyebildiğiniz bir programdır. Python ile yazılan programın düzgün çalışması için bilgisayarda ffmpeg codec'lerinin kurulu olması ve <i>ffmpeg.exe</i> dosyasının yolunun path içerisine eklenmiş olması gerekmektedir.
<p>Bu bağlamda, hızlı bir çevirici olan JSPConvert programının kullanımı çok kolaydır.</p>
<p></p>
<h2>Gereksinimler</h2>
Program ffmpeg modülünü kullandığından, ffmpeg modülünün bilgisayarınıza kurulmuş ve  sistem <b>"Path"</b> yolunda tanımlanmış olması gereklidir. Modül <i><b>https://www.ffmpeg.org/download.html </i></b>adresinden derlenmiş olarak indirilebilir. ffmpeg'i bilgisayarınıza nasıl kuracağınız konusunda
<i><b>https://www.wikihow.com/Install-FFmpeg-on-Windows </b></i>adresinde adım adım anlatım bulabilirsiniz. Programın ilerleyen versiyonlarında modülü direkt bilgisayarınıza kuracağınız bir paket ile geliştrime yapacağız. 
<h2 font size="14">Programın Kullanılışı</h2>
JSPConverter programı, hızlıca ses formatı dönüştürme işlemi yapabileceğiniz, hatta youtube ve sosyal medya içeriklerinden video indirip, videonun sesini alabileceğiniz güçlü bir programdır. Kullanımı kısaca şöyledir:
<ul>
  <li>Programı açtığınızda basit bir grafik arayüz sizi karşılayacaktır. Bu arayüzde üst kısımdaki ikonlarla belirtilmiş ikonlar, <b>Dosya ekleme, Dosya silme, Video'dan al, Play tuşu, Dönüştür butonu ve Dil seçenekleri</b> butonu olarak sıralanmaktadır.</li>
  <li><b>Dosya ekleme butonuna basarak</b>, farklı formata dönüştürmek istediğiniz ses dosyalarını sisteme yüklemiş olursunuz. Birden fazla dosya ile işlem yapabilirsiniz. Bu tuşa basmadan, windows sürükle bırak işlemi ile de dosya ekleme yapmanız mümkündür. Dosyaları, butonların altındaki, mavi renkli "Edit" alanına bırakmalısınız.</li>
  <li><b>Dosya silme butonu ile</b>, "Dosya ekle" butonuyla veya sürükleyip bırakarak edit alanına koyduğunuz formatı değiştirilecek dosyaların birini veya birkaçını listeden çıkarabilirsiniz.</li>
  <li><b>Video'dan al </b> butonuna basarak, herhangi bir Youtube veya video streaming sitesinden video seçebilirsiniz. Tek yapmanız gereken, bu butona bastıktan sonra açılanacak küçük pencerede videonun URL'sini tam olarak girmektir.</li>
  <li><b>Play</b> tuşu işlevselliği henüz eklenmiştir. bu sayede, çevrimi yapılacak dosyaların seslerini önizleme yapabileceksiniz.</li>
  <li><b>"Dönüştür"</b> düğmesi, edit alanındaki ses dosyalarını, pencerenin alt kısmında belirlemiş olduğunuz opsiyonlar ile yine alt kısımda söylediğiniz formata dönüştürür.</li>
  <li><b>Dil seçenekleri</b> butonuna basarak programı istediğiniz dilde kulanabilirsiniz. Geçerli dil, kullandığınız işletim sisteminin varsayılan dili olarak ayarlanmıştır.</li>
  <li>Mavi edit alanının altındaki <b>"Çıktı dosyalarının kaydedileceği dizini seçiniz"</b> yazan alana, çıktı dosyalarını kaydetmek istediğiniz dizini yazabilir veya bu text alanının sağındaki <b>"Gözat"</b> butonu ile, istediğiniz çıktı klasörünü seçebilirsiniz.</li>
  <li>"Gözat" butonunun yanındaki "Çıktı Klasörünü aç" düğmesi, çıktıların kaydedildiği dizine hızlı erişiminizi sağlar.</li>
  
</ul>
<h2>Çıktı Ayarları ve Durum Çubuğu</h2>
<p>
  JSP Converter programında, ses dönüşümü yapılırken, ses kalitesini değiştirebileceğiniz alan "Çıktı Ayarları" alanıdır. Bu alanda yer alan özellikler şunlardır:
  <ul>
    <li><b>Çıktı Formatı:</b>Çıktı formatı, ses dosyalarınızı dönüştürmek istediğiniz formatı seçtiğiniz alandır. Şimdilik üç adet formata dönüşüm yapabilmektesiniz: mp3, ogg ve wav. İstediğiniz ses formatını buradan seçiniz.</li>
    <li><b>Çıktı Kalitesi:</b>Çıktı formatının yanındaki alan, seçeceğiniz çıktı formatına göre değişecektir. Örneğin, çıktı olarak mp3 seçerseniz, sağ taraftan <b>sabit bit oranını (Constant bit rate - CBR) seçemeniz istenecektir.</b> Varsayılan değer en küçük değer olan 32 kilobittir.Bit değeri yükseldikçe kalite artacaktır. Maksimum kalite 320 k olup, CD kalitesi 128 k'dır. Kalite arttıkça, dosya boyutunun da artacağını unutmayınız.
    <p>Bir başka format olan Wav formatını seçtiğinizde, çıktı ayarı olarak değiştireceğiniz bir değer olmayacaktır. Wav dönüşümleriniz, <b>sabit olarak 44100 hz formatında </b>kaydedilecektir.</p>
    <p>Diğer format ogg'de ise çıktı kalitesi seçeneği karşınızda belirecektir. 1 en düşük, 10 ise en kaliteyi çıktıyı temsil etmektedir.Geri planda vereceğiniz kalite paritesi 50kbit ile çarpılarak, çıktı kalitesi hesaplanmaktadır.</p></li>
    <li>Programın durum çubuğu, o anda yapılan işler veya biten işler hakkında bilgi vermektedir. Durum çubuğunun hemen üzerinde ise çeviri işleminin işleyiş oranını gösteren bir progress bar mevcuttur.</li>
  </ul>
</p>
