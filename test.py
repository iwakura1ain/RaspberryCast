from youtube_dl import YoutubeDL

video = "https://www.youtube.com/watch?v=3n1aC2TYXIA"

with YoutubeDL({
            'logger': None,
            'noplaylist': True,
            'ignoreerrors': True,
        }) as ydl:
      info_dict = ydl.extract_info(video, download=False)
      print(info_dict)
