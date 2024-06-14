from PyQt5.QtWidgets import *
import sys
import os
from mutagen.id3 import ID3, TENC
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QListWidgetItem, QMessageBox, QListWidget
from main_form import Ui_Form
from pydub import AudioSegment
from PyQt5.QtCore import Qt, QUrl

class DosyaListWidget(QListWidget):

    def __init__(self, parent= None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent (self, event):
        if event.mimeData().hasUrls():
            event.SetDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().hasUrls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()
        
            print (event.mimeData().Urls())

    def setObjectName(self, name):
        # Bu metodun herhangi bir şey yapmasına gerek yok.
        # Sadece hatayı önlemek için eklenmiştir.
        pass

class Anasayfa(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.converter = Ui_Form()
        self.input_files = []  # Birden fazla dosya seçebilmek için liste oluşturuldu
        self.converter.setupUi(self)
        dosya_listesi = DosyaListWidget()
        self.converter.listWidget = dosya_listesi
        
        self.input = self.converter.listWidget
        self.dosya = self.converter.pushButton.clicked.connect(self.show_file_dialog)
        self.converter.pushButton_4.clicked.connect(self.convert)
        self.converter.pushButton_7.clicked.connect(self.get_output_folder)
        
        self.converter.comboBox.addItem(".mp3")
        self.converter.comboBox.addItem(".wav")
        self.converter.comboBox.addItem(".ogg")
        self.CBR = []
        self.quality = []
        self.CBR = (32,40,48,56,64,80,96,112,128,160,192,224,256,320)
        for bit in self.CBR:
            self.converter.comboBox_2.addItem(str(bit)+"k")
        self.converter.comboBox.currentIndexChanged.connect(self.bitchange)
           

        
    def bitchange(self):
        if self.converter.comboBox.currentText()==".ogg":
            self.converter.comboBox_2.setEnabled(True)
            self.converter.comboBox_2.clear()
            self.quality = (1,2,3,4,5,6,7,8,9,10)
            for kalite in self.quality:
                self.converter.comboBox_2.addItem(str(kalite))
            self.converter.label_3.setText("Kalite:")
        if self.converter.comboBox.currentText()==".mp3":
            self.converter.comboBox_2.setEnabled(True)
            self.converter.comboBox_2.clear()
            for bit in self.CBR:
                self.converter.comboBox_2.addItem(str(bit)+"k")
            self.converter.label_3.setText("Sabit Bit Oranı:")    
        if self.converter.comboBox.currentText()==".wav":
            self.converter.comboBox_2.setEnabled(False)
            self.converter.label_3.setText("44.1Khz, 22k") 

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # Dosya seçme penceresini aç
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Ses dosyaları (*.ogg *.mp3 *.m4a *.wav);;All Files (*)")

        # Birden fazla dosya seçebilmek için
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                print("Seçilen Dosya:", file)
                self.input_files.append(file)  # Seçilen dosya yollarını listeye ekleyin

                # Seçilen dosyayı QListWidget'e ekleyin
                item = QListWidgetItem(file)
                self.input.addItem(item)

    def get_output_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # Klasör seçme penceresini aç
        folder_dialog = QFileDialog()
        folder_dialog.setOptions(options)
        folder_dialog.setFileMode(QFileDialog.Directory)

        if folder_dialog.exec_():
            selected_folder = folder_dialog.selectedFiles()
            if selected_folder:
                self.output_folder = selected_folder[0]
                print("Çıktı Klasörü:", self.output_folder)
        self.converter.lineEdit.setText(self.output_folder)

    
    def convert(self):
        
        if self.converter.lineEdit.text():
            output_mp3_file = self.output_folder
        else:
            QMessageBox.information(self, "UYARI", "Çıktı klasörü boş bırakılamaz!", QMessageBox.Ok) 
            return
        desired_bit_rate = self.converter.comboBox_2.currentText()
        
        # Birden fazla dosyayı dönüştürmek için
        for input_file in self.input_files:
            dosyaadi, uzanti = os.path.splitext(os.path.basename(input_file))
            cikti = output_mp3_file +"/"+dosyaadi+self.converter.comboBox.currentText()
            print("girdi dosyası: ", input_file, "çıktı dosyası: ", cikti, "bitrate: ", desired_bit_rate)
            #print("girdi dosyası: ", input_file, "çıktı dosyası: ", output_mp3_file, "bitrate: ", desired_bit_rate)
            self.ogg_to_mp3(input_file, cikti, desired_bit_rate)

    def ogg_to_mp3(self, input_path, output_path, desired_bit_rate):

        try:
                # ses dosyasını yükle
            audio = AudioSegment.from_ogg(input_path)
            if self.converter.comboBox.currentText() ==".ogg":
                # OGG formatında kaydet      
                audio.export(output_path, format="ogg", codec="libvorbis", parameters=["-b:a", f"{int(desired_bit_rate)*50}k"])
            if self.converter.comboBox.currentText()==".wav":
                # Wav olarak dönüştür.
                # Örnekleme hızını ve örnek boyutunu ayarla
                audio = audio.set_frame_rate(44100)
                audio = audio.set_sample_width(4)
                # WAV olarak kaydet
                audio.export(output_path, format="wav")
            if self.converter.comboBox.currentText()==".mp3":
                # MP3 olarak dönüştür
                mp3_audio = audio.export(output_path, format="mp3", bitrate=desired_bit_rate)
                # ETİKETLEME----------------------------
                audiofile = ID3(output_path) 
                # Yeni encoder etiketini ayarla
                yeni_encoder_etiketi = "JSP Converter-(c)-2023 by JSP Bilgi İşlem - Özgür CENGİZ" 
                # encoded by etiketini değiştir
                audiofile.add(TENC(encoding=3, text=yeni_encoder_etiketi))
                # Etiketleri kaydet
                audiofile.save(output_path)
                # ---------------------------------------
                
                print(f"{input_path} dosyası {output_path} dosyasına {desired_bit_rate} bit hızında dönüştürüldü.")
        except Exception as e:
            print(f"Hata: {e}")
            print(f"{int(desired_bit_rate)*50}k")
            

app = QApplication([])
pencere = Anasayfa()
pencere.show()
app.exec_()
