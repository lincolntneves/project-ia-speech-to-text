## -------------------------------------------------- ##
# Download video from YouTube

#pip install yt-dlp
import yt_dlp

def Download(link):
    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter the YouTube video URL: ")
Download(link)
