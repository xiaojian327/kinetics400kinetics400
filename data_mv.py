import os
import shutil

# 源文件夹路径
source_folder = 'F:/kinetics/kinetics-dataset/k400/data/train'
# 目标文件夹路径
destination_folder = 'F:/kinetics/kinetics-dataset/k400/data/trains'

# 创建目标文件夹（如果不存在）
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 递归遍历源文件夹中的每个子文件夹
for root, dirs, files in os.walk(source_folder):
    # 遍历子文件夹中的每个文件
    for file in files:
        # 检查文件是否为MP4文件
        if file.endswith('.mp4'):
            # 构建源文件和目标文件的完整路径
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)
            # 移动文件
            shutil.move(source_file, destination_file)
            print(f"MP4文件 {file} 已移动到 {destination_folder} 文件夹。")

print("所有MP4文件已成功汇总到指定文件夹。")
