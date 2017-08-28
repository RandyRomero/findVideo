#!python3

import os
import re

while True:
    directory = input('Please, choose directory to scan: \n')
    if os.path.exists(directory):
        print('Got it!')
        break
    else:
        print('This path doesn\'t work. Try another one.')
        continue

extension_dict = {}

for root, subfolders, files in os.walk(directory):
    # print(root)

    # for subfolder in subfolders:
    #     print(os.path.join(root + subfolder))

    for file in files:
        # print(os.path.join(root, file))
        extension = re.search(r'\.\w{2,4}$', file).group()
        print(extension)