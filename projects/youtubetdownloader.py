from pytube import YouTube

vid = 'https://www.youtube.com/watch?v=nd7JrEcnJaw'

yt = YouTube(vid)

print(yt.title)

# print(dir(YouTube))