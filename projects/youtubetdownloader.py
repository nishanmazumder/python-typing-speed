from pytube import YouTube
from pytube import Playlist

vid = 'https://www.youtube.com/watch?v=nd7JrEcnJaw'

yt = YouTube(vid)

vid_title = yt.title
vid_thumb = yt.thumbnail_url
vid_streams = yt.streams.all()
# vid_streams = yt.streams.filter(only_audio=True) # For audio only

# for i, stream in enumerate(vid_streams):
#     print(i, stream)

# print()

# vid_download = (int(input('Enter the number: ')))

# vid_streams[vid_download].download()
# print('Video downloaded!')

######### PLAYLIST ###########
yt_playlist = Playlist('Link of playlist')

print(f'Downloading: {yt_playlist.title}')

for video in yt_playlist.videos:
    video.streams.first().download() #get_by_resolution

print('Playlist downloaded!')

# print(dir(yt.streams))

