import os, shutil

dir_name = 'tempdata'
file_name = 'matty.shakespeare.tar.gz'
full_name = os.path.join(dir_name, file_name)

shutil.unpack_archive(full_name, extract_dir=dir_name)
print('Unpacked', full_name, 'into:', dir_name)
