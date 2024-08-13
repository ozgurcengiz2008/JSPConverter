import yt_dlp
import certifi
import urllib3
import ssl
import os

def indir(video_url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE 
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        yol = os.path.join(os.getcwd(), 'indirilen_video_ses_dosyalari')
        if not os.path.exists(yol):
            os.makedirs(yol)
        
        ydl_opts = {
            'format': '140',  # Format kodunu burada belirtiyorsunuz, eski ayar best idi. Artık kullanılmıyor. Video için diğer kodlara ytp-dl --list-formats "youtube linki" ifadesiyle bakılabilir.
            'outtmpl': os.path.join(yol, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([video_url])
            video_info = ydl.extract_info(video_url, download=False)
            output_file = ydl.prepare_filename(video_info)
        return output_file  # Dosyanın indirildiği tam yolunu döndür

    except Exception as e:
        print(f"Hata: {e}")
        with open("hata_log.txt", "w") as f:
            f.write(f"Hata: {e}")
        return None

def main():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output_file = indir(video_url)
    if output_file is not None:
        print(f"Dosya başarıyla indirildi: {output_file}")
    else:
        print("Dosya indirilemedi.")

if __name__ == "__main__":
    main()
