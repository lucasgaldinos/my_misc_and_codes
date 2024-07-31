"""ref = https://stackoverflow.com/questions/37467561/renaming-multiple-files-in-a-directory-using-python"""

import os
path = 'how_to_databricks_jobs'
files = os.listdir(path)

print(files)

# for index, file in enumerate(files):
#     os.rename(os.path.join(path, file), os.path.join(
#         path, ''.join([str(index), '.jpg'])))
