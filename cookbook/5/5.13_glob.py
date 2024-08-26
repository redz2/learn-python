"""
glob库提供了一个简单而强大的方法来管理文件和目录

glob 返回列表
iglob 返回迭代器
"""
import glob
import os

# 获取当前目录下的py文件列表
# 结合了os.listdir()以及fnmatchcase()的功能
matched_files = glob.glob("./**/*.py*", recursive=True)
sorted_files_by_size = sorted(matched_files, key=os.path.getsize)
print(sorted_files_by_size)

# 拼接文件路径
# os.path.join(base_dir_path, file_name)

# 删除csv文件
csv_files = glob.glob("./*.csv")
for csv_file in csv_files:
    os.remove(csv_file)
