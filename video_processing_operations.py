import os

from PIL import Image, ImageFilter
from moviepy.video.io import ImageSequenceClip


def blur_frames(input_dir, output_dir, classmap):
    for filename in os.listdir(input_dir):
        print(filename)
        path = input_dir + filename
        img = Image.open(path)
        if classmap[filename]['1'] > 0.7 or classmap[filename]['3'] > 0.7:
            print(f"Not blurring {filename}")
            img.save(output_dir + filename)
        else:
            print(f"Blurring {filename}...")
            img = img.filter(ImageFilter.GaussianBlur(100))
            img.save(output_dir + filename)


def sort_frames(input_dir):
    images = [img for img in os.listdir(input_dir) if img.endswith(".jpg")]
    images = sorted(images, key=lambda x: int(x.split('.')[0]))
    images = [input_dir + img for img in images]
    return images


def frames_to_video(input_dir, fps, output_dir):
    images = sort_frames(input_dir)
    print(images)
    clip = ImageSequenceClip.ImageSequenceClip(images, fps)
    clip.write_videofile(output_dir + "video.mp4", fps=fps)

# def frames_to_video(input_dir, fps, output_dir):
#     try:
#         images = sort_frames(input_dir)
#         if not images:
#             raise ValueError("No images found in directory")
        
#         clip = ImageSequenceClip.ImageSequenceClip(images, fps)
#         output_path = os.path.join(output_dir, "video.mp4")
#         clip.write_videofile(output_path, fps=fps)
#         return output_path
#     except Exception as e:
#         logging.error(f"Error in video processing: {str(e)}")
#         raise
