import os
import pandas as pd
import shutil

# 假设输入的csv文件路径和视频文件夹路径如下
csv_file_path = 'F:/kinetics/kinetics-dataset/k400/annotations/train.csv'
videos_folder_path = 'F:/kinetics/kinetics-dataset/k400/train'
output_folder_path = 'F:/kinetics/kinetics-dataset/k400/test/train'

# 读取CSV文件
df = pd.read_csv(csv_file_path)

# 遍历CSV文件中的每一行
for index, row in df.iterrows():
    video_id = row[1]  # 假设CSV中有'video_id'列
    time_start = row[2]
    time_end = row[3]
    category = row[0]  # 假设CSV中有'category'列

    # 将时间戳格式化为6位，前面补0
    formatted_time_start = str(time_start).zfill(6)
    formatted_time_end = str(time_end).zfill(6)


    # 构建源视频文件和目标文件夹的路径
    source_video_file = os.path.join(videos_folder_path, f"{video_id}_{formatted_time_start}_{formatted_time_end}.mp4")
    target_category_folder = os.path.join(output_folder_path, category)
    # 检查源视频文件是否存在
    if os.path.exists(source_video_file):
        # 创建目标文件夹（如果不存在）
        if not os.path.exists(target_category_folder):
            os.makedirs(target_category_folder)
        # 移动视频文件到目标文件夹
        shutil.move(source_video_file, target_category_folder)
        print(f"视频文件 {video_id}.mp4 已移动到 {category} 文件夹。")
    else:
        print(f"警告：视频文件 {video_id}.mp4 不存在，跳过。")

print("视频文件已按类别分拣到相应文件夹。")