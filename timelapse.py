import cv2
import os

folder = 'photos'
files = [f for f in sorted(os.listdir(folder)) if not f.startswith('.') and not f.startswith('README')]

img_array = []

for filename in files:
    path = os.path.join('.', folder, filename)

    try:
        img = cv2.imread(path)

        height, width, layers = img.shape
        size = (width,height)

        img_array.append(img)
    except Exception:
        print(f'Error in path: {path}')

out = cv2.VideoWriter(os.path.join('output', 'result.mp4'), cv2.VideoWriter_fourcc(*'mp4v'), 20.0, size)

for i in range(len(img_array)):
   out.write(img_array[i])

out.release()