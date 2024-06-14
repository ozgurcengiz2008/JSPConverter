import pytube
import certifi
import urllib3
import ssl

def indir(video_url):
    try:
        
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE 
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        yt = pytube.YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        output_file = video.download()
        return output_file
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
