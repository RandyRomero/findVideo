#!python3

import os
import re
import shutil
import time


def search_video_files(path):
    start_time = time.time()

    video_files_to_move = []  # List of video files to extract from all photos
    extension_dict = {}  # dictionary to count how many appearances of each extension are in the given folder
    video_ext = ['mp4', '3gp', 'mpg', 'wmv', 'mov', 'avi']  # list of video extension to process
    total_size = 0  # total size of video files

    for root, subfolders, files in os.walk(path):

        for file in files:
            # print(os.path.join(root, file))
            extension = re.search(r'\.\w{2,4}$', file).group().lower()
            if extension[1:] in video_ext:
                path_to_file = os.path.join(root, file)
                size_of_file = os.path.getsize(path_to_file)
                print(path_to_file + ' -- {0:.2f} MB'.format(size_of_file / 1024 ** 2))
                total_size += size_of_file
                video_files_to_move.append(path_to_file)
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
    return video_files_to_move


def move_files(put_videos_to, files_to_move):  # Moving files to one specific folder given by user
    for file in files_to_move:
        print('Copying ' + file)
        shutil.move(file, put_videos_to)
        print('Done')

while True:  # Ask user to choose folder where he wants to look for video files
    directory = input('Please, choose directory to scan: \n')
    if os.path.exists(directory):
        print('Got it!')
        list_of_video = search_video_files(directory)
        break
    else:
        print('This path doesn\'t work. Try another one.')
        continue


# while True:  # Ask user where put his video files to
#     move_videos_to = input('Please choose directory where put video files to:\n')
#     if os.path.exists(move_videos_to):
#         print('Gotcha!')
#         move_files(move_videos_to, list_of_video)
#         break
#     else:
#         print('This path doesn\'t exist. Try another one')
#         continue


