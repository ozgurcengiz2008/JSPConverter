from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLabel, QAbstractItemView, QListWidgetItem, QFileDialog, QDialog, QVBoxLayout, QLineEdit, QApplication, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDesktopServices, QMovie, QGuiApplication, QCursor
from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal, pyqtSlot
from mutagen.id3 import ID3, TENC
from pydub import AudioSegment
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import os
from main2_form import Ui_MainWindow
from yt_dlp_instance import indir
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
            indirilen_dizin = indir(self.video_url)
            if indirilen_dizin:
                self.finished_download.emit(indirilen_dizin)
            else:
                self.finished_download.emit(None)

        except Exception as e:
            print(f"Hata: {e}")
            self.finished_download.emit(None)
            



class ConvertThread(QThread):
    finished = pyqtSignal()
    progress_update = pyqtSignal(str, int)  # Yeni sinyal: dosya adı ve ilerleme yüzdesi

    def __init__(self, input_files, output_folder, desired_bit_rate, comboBoxText):
        super().__init__()
        self.input_files = input_files
        self.output_folder = output_folder
        self.desired_bit_rate = desired_bit_rate
        self.comboBoxText = comboBoxText

    def run(self):
        total_files = len(self.input_files)
        progress_step = int(100 / total_files)

        for index, input_file in enumerate(self.input_files):
            dosyaadi, uzanti = os.path.splitext(os.path.basename(input_file))
            cikti = os.path.join(self.output_folder, dosyaadi + self.comboBoxText)
            self.ogg_to_mp3(input_file, cikti, self.desired_bit_rate, uzanti)

            progress_value = (index + 1) * progress_step
            self.progress_update.emit(os.path.basename(input_file), progress_value)  # İlerleme güncellemesi gönder

        self.finished.emit()

    def ogg_to_mp3(self, input_path, output_path, desired_bit_rate, uzanti):
        try:
            if uzanti == ".mp4":
                audio = AudioSegment.from_file(input_path, format="mp4")
            elif uzanti == ".ogg":
                audio = AudioSegment.from_ogg(input_path)
            elif uzanti == ".mp3":
                audio = AudioSegment.from_mp3(input_path)

            if self.comboBoxText == ".mp3":
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
        spnryol = os.getcwd() + "\images\loading-6.gif"
        self.movie = QMovie(spnryol)
        self.movie.setScaledSize(new_size)
        self.loading_label = QLabel(self)
        self.loading_label.setMovie(self.movie)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setGeometry(200, 100, 400, 400)
        self.converter.pushButton_5.clicked.connect(self.show_video_input_dialog)
        self.video_url_from_dialog = None
        self.convert_thread = ConvertThread([], "", "", "")

        self.convert_thread.finished.connect(self.on_convert_finished)
        self.convert_thread.progress_update.connect(self.update_progress)  # Yeni sinyal bağlantısı

        self.CBR = (32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320)
        for bit in self.CBR:
            self.converter.comboBox_2.addItem(str(bit) + "k")

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
                self.converter.comboBox_2.addItem(str(bit) + "k")
            self.converter.label_3.setText("Sabit Bit Oranı:")
        elif self.converter.comboBox.currentText() == ".wav":
            self.converter.comboBox_2.setEnabled(False)
            self.converter.comboBox_2.clear()
            self.converter.label_3.setText("Wav Formatı:")

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Ağ bağlantılarını göstermek için bu seçeneği ekleyin
        files, _ = QFileDialog.getOpenFileNames(self, "Müzik Dosyalarını Seçin", "", "Müzik Dosyaları (*.mp3 *.ogg *.wav *.mp4)")

        if files:
            for file in files:
                self.input_files.append(file)
                item = QListWidgetItem(file)
                self.input.addItem(item)

    def get_output_folder(self):
        self.output_folder = QFileDialog.getExistingDirectory(self, "Çıktı Klasörünü Seçin")
        self.converter.lineEdit.setText(self.output_folder)

    def sil(self):
        selected_items = self.input.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.input_files.remove(item.text())
            self.input.takeItem(self.input.row(item))

    def show_video_input_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("YouTube URL'si Girin")
        dialog.resize(400, 100)

        layout = QVBoxLayout(dialog)
        line_edit = QLineEdit(dialog)
        line_edit.setPlaceholderText("YouTube URL'si buraya girin...")
        layout.addWidget(line_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        layout.addWidget(buttons)

        def accept():
            self.video_url_from_dialog = line_edit.text()
            dialog.accept()
            self.start_download_thread(self.video_url_from_dialog)  # İndirme işlemini başlat

        def reject():
            dialog.reject()

        buttons.accepted.connect(accept)
        buttons.rejected.connect(reject)

        dialog.exec_()

    def start_download_thread(self, video_url):
        if not video_url:
            return

        self.converter.statusbar.showMessage('İndirme işlemi başlıyor...')
        self.movie.start()
        self.loading_label.setHidden(False)

        self.download_thread = DownloadThread(video_url)
        self.download_thread.finished_download.connect(self.on_download_finished)
        self.download_thread.start()

    def on_download_finished(self, output_file):
        self.movie.stop()
        self.loading_label.setHidden(True)

        if output_file:
            self.input_files.append(output_file)
            item = QListWidgetItem(output_file)
            self.input.addItem(item)
            self.converter.statusbar.showMessage('İndirme tamamlandı')
        else:
            self.converter.statusbar.showMessage('İndirme başarısız oldu', 5000)
            QMessageBox.warning(self, "Hata", "İndirme işlemi başarısız oldu.", QMessageBox.Ok)

    def update_progress(self, file_name, progress_value):
        self.converter.statusbar.showMessage(f"{file_name} dosyası işleniyor... {progress_value}%")
        self.progressBar.setValue(progress_value)
        self.progressBar.setFormat(f"{file_name}: {progress_value}%")

    def convert(self):
        if not self.input_files:
            QMessageBox.warning(self, "UYARI", "Dönüştürülecek dosya eklenmemiş!", QMessageBox.Ok)
            return

        if not self.output_folder:
            QMessageBox.warning(self, "UYARI", "Çıktı klasörü seçilmemiş!", QMessageBox.Ok)
            return

        self.movie.start()
        self.loading_label.setHidden(False)
        self.progressBar.setValue(0)
        self.converter.statusbar.showMessage('Dönüştürme işlemi başlıyor...')

        desired_bit_rate = self.converter.comboBox_2.currentText()
        comboBoxText = self.converter.comboBox.currentText()
        self.convert_thread = ConvertThread(self.input_files, self.output_folder, desired_bit_rate, comboBoxText)
        self.convert_thread.progress_update.connect(self.update_progress)  # İlerleme güncellemesi için bağlantı
        self.convert_thread.finished.connect(self.on_convert_finished)
        self.convert_thread.start()

    def on_convert_finished(self):
        self.movie.stop()
        self.loading_label.setHidden(True)
        self.converter.statusbar.showMessage('Dönüştürme tamamlandı')

    def play_music(self):
        selected_item = self.input.currentItem()
        if selected_item:
            file_path = selected_item.text()
            url = QUrl.fromLocalFile(file_path)
            content = QMediaContent(url)
            self.playlist.addMedia(content)
            self.player.play()

if __name__ == '__main__':
    import sys
    
    

    app = QApplication(sys.argv)
    window = Anasayfa()
    window.show()
    sys.exit(app.exec_())

    

    

