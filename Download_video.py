from __future__ import unicode_literals
import youtube_dl
print("--------------------------------------------")
print("-------YOU TUBE DOWNLOADER------------------") 
url = raw_input("Please enter your video url here\n")
urlstring = str(url)
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([urlstring])
print("--------------------------------------------")
