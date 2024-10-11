<h1 font size="18"> JSPConverter___(En)</h1><br>
The JSP Converter program is a simple application that converts audio formats (mp4, mp3, ogg, wav) using the ffmpeg module, allowing you to set the quality during the conversion. For the program, written in Python, to work properly, the ffmpeg codecs must be installed on the computer, and the path to the <i>ffmpeg.exe</i> file must be added to the system path.
<p>In this context, the JSPConvert program, a fast converter, is very easy to use.</p>
<p></p>
<h2>Requirements</h2>
Since the program uses the ffmpeg module, the ffmpeg module must be installed on your computer and defined in the system <b>"Path"</b>. The module can be downloaded precompiled from <i><b>https://www.ffmpeg.org/download.html</i></b>. For a step-by-step guide on how to install ffmpeg on your computer, you can refer to <i><b>https://www.wikihow.com/Install-FFmpeg-on-Windows</b></i>. In future versions of the program, we will develop a package that will directly install the module on your computer.<p>
  <p>Secondly, VLC player must be downloaded and installed. Libraries of VLC, an open source media player, are used for video conversion. For this reason it is necessary. You can download and install VLC Player from its original location at https://www.videolan.org/index.tr.html.<b><i>You must download and install 64bit VLC Player Windows, not 32 bit, otherwise it wont work!</i></b></p>
<h2 font size="14">Usage of the Program</h2>
The JSPConverter program is a powerful tool for quickly converting audio formats and even downloading videos from YouTube and social media content and extracting the audio from the video. Here's a brief overview of how to use it:
<ul>
  <li>When you open the program, a simple graphical interface will greet you. The icons indicated by the icons at the top are <b>Add File, Delete File, Extract from Video, Play Button, Convert Button, and Language Options</b>.</li>
  <li>By pressing the <b>Add File button</b>, you can upload the audio files you want to convert to a different format. You can process multiple files at once. You can also add files by drag-and-drop without pressing this button. You should drop the files into the blue "Edit" area below the buttons.</li>
  <li>With the <b>Delete File button</b>, you can remove one or more files from the list that you have added to the edit area for format conversion by the "Add File" button or by drag-and-drop.</li>
  <li>By pressing the <b>Extract from Video</b> button, you can select a video from any YouTube or video streaming site. All you need to do is enter the exact URL of the video in the small window that opens after pressing this button.</li>
  <li>The <b>Play</b> button functionality has just been added. This allows you to preview the audio of the files to be converted.</li>
  <li>The <b>Convert</b> button converts the audio files in the edit area to the format specified in the options at the bottom of the window.</li>
  <li>By pressing the <b>Language Options</b> button, you can use the program in your preferred language. The current language is set to the default language of your operating system.</li>
  <li>In the area below the blue edit area that says <b>"Select the directory to save output files"</b>, you can write the directory where you want to save the output files or use the <b>"Browse"</b> button to select the desired output folder.</li>
  <li>The "Open Output Folder" button next to the "Browse" button provides quick access to the directory where the outputs are saved.</li>
</ul>
<h2>Output Settings and Status Bar</h2>
<p>
  In the JSP Converter program, the area where you can change the audio quality during the conversion is the "Output Settings" area. The features in this area are as follows:
  <ul>
    <li><b>Output Format:</b> The output format is the area where you select the format to which you want to convert your audio files. Currently, you can convert to three formats: mp3, ogg, and wav. Select your desired audio format here.</li>
    <li><b>Output Quality:</b> The area next to the output format will change according to the selected output format. For example, if you select mp3 as the output, you will be asked to choose the <b>constant bit rate (CBR)</b> on the right. The default value is the lowest, 32 kilobits. The higher the bit value, the higher the quality. The maximum quality is 320 kbps, and CD quality is 128 kbps. Note that as the quality increases, the file size will also increase.
    <p>If you select the Wav format, there will be no value to change in the output settings. Your Wav conversions will be saved in a <b>constant 44100 Hz format</b>.</p>
    <p>For the ogg format, the output quality option will appear. 1 represents the lowest quality, and 10 represents the highest quality. The quality parity you provide in the background is calculated by multiplying it by 50 kbps to determine the output quality.</p></li>
    <li>The program's status bar provides information about the tasks being performed or completed. Above the status bar, there is a progress bar showing the progress of the conversion process.</li>
  </ul>
</p>
  
<hr>
<h1 font size="18"> JSPConverter___(Tr) </h1><br>
JSP Converter programı, basitçe ffmpeg modülünü kullanarak ses formatları içerisinde (mp4,mp3,ogg,wav) dönüşüm yapan, dönüşüm yaparken de kalitesini belirleyebildiğiniz bir programdır. Python ile yazılan programın düzgün çalışması için bilgisayarda ffmpeg codec'lerinin kurulu olması ve <i>ffmpeg.exe</i> dosyasının yolunun path içerisine eklenmiş olması gerekmektedir.<p>
  
<h2>Gereksinimler</h2>
Program ffmpeg modülünü kullandığından, ffmpeg modülünün bilgisayarınıza kurulmuş ve  sistem <b>"Path"</b> yolunda tanımlanmış olması gereklidir. Modül <i><b>https://www.ffmpeg.org/download.html </i></b>adresinden derlenmiş olarak indirilebilir. ffmpeg'i bilgisayarınıza nasıl kuracağınız konusunda
<i><b>https://www.wikihow.com/Install-FFmpeg-on-Windows </b></i>adresinde adım adım anlatım bulabilirsiniz. Programın ilerleyen versiyonlarında modülü direkt bilgisayarınıza kuracağınız bir paket ile geliştrime yapacağız. 
  <p> İkinci olarak VLC player indirilip kurulmalıdır. Açık kaynak bir medya oynatıcısı olan VLC'nin video çevirme için kütüphaneleri kullanılmaktadır. Bu sebeple gereklidir. VLC Player'i https://www.videolan.org/index.tr.html adresindeki orjinal konumundan indirip kurabilirsiniz. <b><i>VLC'nin mutlaka 64 bit Windows için olan sürümünü indiriniz!</i></b>
<p>Bu bağlamda, hızlı bir çevirici olan JSPConvert programının kullanımı çok kolaydır.</p>
<p></p>
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
