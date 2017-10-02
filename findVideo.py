#!python3

import os
import re
import time

while True:
    directory = input('Please, choose directory to scan: \n')
    if os.path.exists(directory):
        print('Got it!')
        break
    else:
        print('This path doesn\'t work. Try another one.')
        continue

extension_dict = {}  # dictionary to count how many appearances of each extension are in the given folder
video_ext = ['mp4']  # list of video extension to process
total_size = 0  # total size of video files


start_time = time.time()

for root, subfolders, files in os.walk(directory):

    for file in files:
        # print(os.path.join(root, file))
        extension = re.search(r'\.\w{2,4}$', file).group().lower()
        if extension[1:] in video_ext:
            total_size += os.path.getsize(os.path.join(root, file))
            # print('Size of ' + file + ' is ' + '{0:.2f} MB.'.format(os.path.getsize(os.path.join(root, file))
            # / 1024 ** 2))

        # Below is short way of this code:
        # if extension in extension_dict:
        #     extension_dict[extension] += 1
        # else:
        #     extension_dict[extension] = 1
        extension_dict[extension] = extension_dict.get(extension, 0) + 1
print('Total size of all video files is {0:.2f} MB.\n'.format(total_size / 1024 ** 2))
print('Here are all extension that have been found in ' + directory)
print(extension_dict)
print('--- {0:.3f} seconds ---'.format(time.time() - start_time))
