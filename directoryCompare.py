import filecmp
import os
import shutil

dir1 = ''
dir2 = ''

def compare_and_copy(dir1, dir2):
    comparison = filecmp.dircmp(dir1, dir2)

    for file_name in comparison.left_only:
        src_path = os.path.join(dir1, file_name)
        dest_path = os.path.join(dir2, file_name)
        
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

    for file_name in comparison.diff_files:
        src_path = os.path.join(dir1, file_name)
        dest_path = os.path.join(dir2, file_name)
        shutil.copy2(src_path, dest_path)
        
    for subdir in comparison.common_dirs:
        compare_and_copy(os.path.join(dir1, subdir), os.path.join(dir2, subdir))

if not os.path.exists(dir2):
    os.makedirs(dir2)

compare_and_copy(dir1, dir2)

print(f"Files in '{dir1}' have been copied and updated in '{dir2}'.")




