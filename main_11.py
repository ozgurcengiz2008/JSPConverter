from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLabel, QAbstractItemView, QListWidgetItem, QFileDialog, QDialog, QVBoxLayout, QLineEdit, QApplication, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDesktopServices, QMovie, QGuiApplication, QCursor
from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal
from mutagen.id3 import ID3, TENC
from pydub import AudioSegment
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import os
from main2_form import Ui_MainWindow
from pytube import YouTube
import certifi
import urllib3
import ssl



class DownloadThread(QThread):
    finished_download = pyqtSignal(str)  # Download bitince gönderilen sinyal

    def __init__(self, video_url, parent=None):
        super().__init__(parent)
        self.video_url = video_url

    def run(self):
        try:
            
            
            yt = YouTube(self.video_url)
            video = yt.streams.filter(only_audio=True).first()

            if video:
                yol = os.getcwd()+f"\indirilen_video_ses_dosyalari"
                print("video yolu: ", yol)
                output_file = video.download(yol, filename=yt.title+".mp4")
                self.finished_download.emit(output_file)
            else:
                QMessageBox.warning(None, "Hata", "Video sesi bulunamadı.", QMessageBox.Ok)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.warning(None, "Hata:", f"Video indirme sırasında bir hata oluştu. Hata: {e}", QMessageBox.Ok)
            with open("hata_log.txt", "w") as f:
                f.write(f"Hata: {e}")
    
           
        
class ConvertThread(QThread):
    finished = pyqtSignal()

    def __init__(self, input_files, output_folder, desired_bit_rate, comboBoxText,converter):
        super().__init__()
        self.input_files = input_files
        self.output_folder = output_folder
        self.desired_bit_rate = desired_bit_rate
        self.comboBoxText = comboBoxText
        self.converter = converter
        self.current_progress = 0
        

    def run(self):
        
        total_files = len(self.input_files)
        self.progress_step = int(100 / total_files)
        
        for input_file in self.input_files:
            dosyaadi, uzanti = os.path.splitext(os.path.basename(input_file))
            
            cikti = os.path.join(self.output_folder, dosyaadi + self.comboBoxText)
            self.ogg_to_mp3(input_file, cikti, self.desired_bit_rate, uzanti)
            
            self.current_progress = self.current_progress + self.progress_step
            self.converter.progressBar.setValue(self.current_progress)
            self.converter.statusBar().showMessage(os.path.basename(input_file) + ' dosyası ' + os.path.basename(self.output_folder) + ' dosyasına ' + self.desired_bit_rate + ' bit hızında dönüştürülüyor.')
        self.current_progress = 0
        
        self.finished.emit()
        
    def ogg_to_mp3(self, input_path, output_path, desired_bit_rate, uzanti):
        if uzanti == ".mp4":
            # MP4 dosyasını yükle
            audio = AudioSegment.from_file(input_path, format="mp4")
            try:
                if self.comboBoxText == ".mp3":
                    # MP3 olarak kaydet
                    audio.export(output_path, format="mp3", bitrate=desired_bit_rate)
                    audiofile = ID3(output_path)
                    yeni_encoder_etiketi = "JSP Converter-(c)-2023 by JSP Bilgi İşlem - Özgür CENGİZ"
                    audiofile.add(TENC(encoding=3, text=yeni_encoder_etiketi))
                    audiofile.save(output_path)
                elif self.comboBoxText == ".wav":
                    audio = audio.set_frame_rate(44100)
                    audio = audio.set_sample_width(4)
                    audio.export(output_path, format="wav")
                elif self.comboBoxText == ".ogg":
                    audio.export(output_path, format="ogg", codec="libvorbis", parameters=["-b:a", f"{int(desired_bit_rate)*50}k"])
            except Exception as e:
                QMessageBox.warning(self, "Hata", "Video ses dosyası çevirme sırasında bir hata oluştu.", QMessageBox.Ok)
                print(f"Hata: {e}")
                
                
        try:
            audio = AudioSegment.from_ogg(input_path)
            if self.comboBoxText == ".ogg":
                audio.export(output_path, format="ogg", codec="libvorbis", parameters=["-b:a", f"{int(desired_bit_rate)*50}k"])
            elif self.comboBoxText == ".wav":
                audio = audio.set_frame_rate(44100)
                audio = audio.set_sample_width(4)
                audio.export(output_path, format="wav")
            elif self.comboBoxText == ".mp3":
                mp3_audio = audio.export(output_path, format="mp3", bitrate=desired_bit_rate)
                audiofile = ID3(output_path)
                yeni_encoder_etiketi = "JSP Converter-(c)-2023 by JSP Bilgi İşlem - Özgür CENGİZ"
                audiofile.add(TENC(encoding=3, text=yeni_encoder_etiketi))
                audiofile.save(output_path)
                
                print(f"{input_path} dosyası {output_path} dosyasına {desired_bit_rate} bit hızında dönüştürüldü.")
        except Exception as e:
            print(f"Hata: {e}")
            
            
        

class Anasayfa(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.converter = Ui_MainWindow()
        self.input_files = []
        self.converter.setupUi(self)
        self.output_folder = ""
        self.player = QMediaPlayer(self)
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)
        self.progressBar = self.converter.progressBar
        self.input = self.converter.listWidget
        self.dosya = self.converter.pushButton.clicked.connect(self.show_file_dialog)
        self.converter.pushButton_4.clicked.connect(self.convert)
        self.converter.pushButton_7.clicked.connect(self.get_output_folder)
        self.converter.pushButton_2.clicked.connect(self.sil)
        self.converter.pushButton_8.clicked.connect(self.klasorac)
        self.converter.pushButton_3.clicked.connect(self.play_music)
        self.converter.lineEdit.setEnabled(False)
        self.current_progress = 0
        new_size = QSize(200, 100)
        spnryol= os.getcwd()+"\images\loading-6.gif"
        self.movie = QMovie(spnryol)
        self.movie.setScaledSize(new_size)
        self.loading_label = QLabel(self)
        self.loading_label.setMovie(self.movie)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setGeometry(200, 100, 400, 400)
        self.converter.pushButton_5.clicked.connect(self.show_video_input_dialog)
        self.video_url_from_dialog = None 
        self.convert_thread = ConvertThread([], "", "", "",self)

        self.convert_thread.finished.connect(self.on_convert_finished)

        self.CBR = (32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320)
        for bit in self.CBR:
            self.converter.comboBox_2.addItem(str(bit)+"k")

        self.quality = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        for kalite in self.quality:
            self.converter.comboBox_2.addItem(str(kalite))

        self.converter.comboBox.currentIndexChanged.connect(self.bitchange)
        self.input.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.converter.comboBox.addItem(".mp3")
        self.converter.comboBox.addItem(".wav")
        self.converter.comboBox.addItem(".ogg")

        self.movie.stop()
        self.loading_label.setHidden(True)
        self.converter.statusbar.showMessage('Hazır')

    def klasorac(self):
        if self.output_folder:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.output_folder))
        else: 
            QMessageBox.information(self, "UYARI", "Çıktı klasörü seçilmemiş!", QMessageBox.Ok)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.input_files.append(str(url.toLocalFile()))
                else:
                    self.input_files.append(str(url.toString()))
                item = QListWidgetItem(url.toLocalFile())
                self.input.addItem(item)
        else:
            event.ignore()

    def bitchange(self):
        if self.converter.comboBox.currentText() == ".ogg":
            self.converter.comboBox_2.setEnabled(True)
            self.converter.comboBox_2.clear()
            self.quality = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            for kalite in self.quality:
                self.converter.comboBox_2.addItem(str(kalite))
            self.converter.label_3.setText("Kalite:")
        elif self.converter.comboBox.currentText() == ".mp3":
            self.converter.comboBox_2.setEnabled(True)
            self.converter.comboBox_2.clear()
            for bit in self.CBR:
                self.converter.comboBox_2.addItem(str(bit)+"k")
            self.converter.label_3.setText("Sabit Bit Oranı:")    
        elif self.converter.comboBox.currentText() == ".wav":
            self.converter.comboBox_2.setEnabled(False)
            self.converter.label_3.setText("44.1Khz, 22k") 

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Ses dosyaları (*.ogg *.mp3 *.m4a *.wav);;All Files (*)")
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                print("Seçilen Dosya:", file)
                self.input_files.append(file)
                item = QListWidgetItem(file)
                
                self.input.addItem(item)

    def get_output_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        folder_dialog = QFileDialog()
        folder_dialog.setOptions(options)
        folder_dialog.setFileMode(QFileDialog.Directory)

        if folder_dialog.exec_():
            selected_folder = folder_dialog.selectedFiles()
            if selected_folder:
                self.output_folder = selected_folder[0]
                print("Çıktı Klasörü:", self.output_folder)
        self.converter.lineEdit.setText(self.output_folder)

    def sil(self):
        selected_items = self.input.selectedItems()
        for item in selected_items:
            row = self.input.row(item)
            self.input.takeItem(row)
            file_path = item.text()
            self.input_files.remove(file_path)

    def convert(self):
        QGuiApplication.setOverrideCursor(Qt.WaitCursor)  # Bekleme ikonunu aktif hale getir
        if self.converter.lineEdit.text():
            output_mp3_file = self.output_folder
        else:
            QMessageBox.information(self, "UYARI", "Çıktı klasörü boş bırakılamaz!", QMessageBox.Ok)
            return

        desired_bit_rate = self.converter.comboBox_2.currentText()
        comboBoxText = self.converter.comboBox.currentText()
        self.convert_thread.input_files = self.input_files
        self.convert_thread.output_folder = output_mp3_file
        self.convert_thread.desired_bit_rate = desired_bit_rate
        self.convert_thread.comboBoxText = comboBoxText
        #converter = self.converter.statusbar
        #self.statusBar().showMessage(os.path.basename(self.convert_thread.input_files[0]) + ' dosyası ' + os.path.basename(self.convert_thread.output_folder) + ' dosyasına' + desired_bit_rate + ' bit hızında dönüştürülüyor.')
        #self.converter.statusbar.showMessage(os.path.basename(self.convert_thread.input_files[0]) + ' dosyası ' + os.path.basename(self.convert_thread.output_folder) + ' dosyasına' + desired_bit_rate + ' bit hızında dönüştürülüyor.')
        
        
        self.loading_label.setHidden(False)
        self.movie.start()
        
        self.convert_thread.start()

    def on_convert_finished(self):
        self.progressBar.setValue(0)
        self.input.clear()
        self.input_files = []
        self.movie.stop()
        self.loading_label.setHidden(True)
        QGuiApplication.restoreOverrideCursor()
        self.converter.statusbar.showMessage('Dönüştürme Başarılı')
    
    def show_video_input_dialog(self):
        dialog = VideoInputDialog(self)
        self.loading_label.setHidden(False)
        
        if dialog.exec_() == QDialog.Accepted:
            self.movie.start()
            self.video_url_from_dialog = dialog.get_video_url()
            print("video URL: ", self.video_url_from_dialog)
            
            if self.video_url_from_dialog is None:
                QMessageBox.information(self, "UYARI", "Video URL'si boş bırakılamaz!", QMessageBox.Ok)
                return
            
            self.download_thread = DownloadThread(self.video_url_from_dialog)
            self.download_thread.finished_download.connect(self.on_download_finished)
            self.download_thread.start()
            
   
    def on_download_finished(self, output_file):
        self.input_files.append(output_file)
        item = QListWidgetItem(output_file)
        self.input.addItem(item)
        self.loading_label.setHidden(True)
        self.movie.stop()
        QMessageBox.information(self, "Başarılı", "Video sesi başarıyla indirildi.", QMessageBox.Ok)
        
        
            
    def play_music(self):
        try:
            selected_items = self.converter.listWidget.selectedItems()

            if not selected_items:
                selected_items = [self.converter.listWidget.item(i) for i in range(self.converter.listWidget.count())]

            self.playlist.clear()

            for current_item in selected_items:
                file_path = current_item.text()
                media_content = QMediaContent(QUrl.fromLocalFile(file_path))
                self.playlist.addMedia(media_content)

            self.player.setPlaylist(self.playlist)
            self.player.setVolume(100)
            
            if not selected_items:
                # Eğer hiçbir öğe seçilmemişse, tüm çalma listesini oynat
                self.player.play()

            print("Çalma listesi başarıyla ayarlandı.")
        except Exception as e:
            print(f"Hata: {e}")

class VideoInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Video URL")
        self.setGeometry(200, 200, 300, 100)
        layout = QVBoxLayout()
        self.video_url_input = QLineEdit(self)
        self.video_url_input.setGeometry(10,10,280,20)
        self.ok_button = QPushButton("OK", self)       
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
    
    def get_video_url(self):
        print("video URL input: ", self.video_url_input.text())
        return self.video_url_input.text()
    
   
app = QApplication([])
pencere = Anasayfa()
pencere.show()
app.exec_()
