# import pytube


# def download_video(url, output_path):
#     print("Downloading video...")
#     yt = pytube.YouTube(url, use_oauth=True, allow_oauth_cache=True)
#     yt = yt.streams.get_highest_resolution().download(output_path)
#     return yt


import pytube
from pytube.exceptions import RegexMatchError

def download_video(url, output_path):
    try:
        print("Downloading video...")
        yt = pytube.YouTube(url)
        yt.streams.get_highest_resolution().download(output_path)
        print("Download complete!")
    except RegexMatchError as e:
        print(f"Regex match error occurred: {e}")
        # You can add a fallback mechanism or log further details
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
