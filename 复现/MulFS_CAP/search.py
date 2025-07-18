import os
import shutil
from PIL import Image

# 原始图片文件夹路径（修改为你的路径）
source_folder = r"P:\pic_reg_and_pic_fus\learning\M3FD_Fusion\Ir"

# 目标文件夹路径（修改为你希望复制到的文件夹）
destination_folder = r"P:\pic_reg_and_pic_fus\learning\MulFS-CAP\ir_dir"

# 支持的图片后缀
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

# 如果目标文件夹不存在就创建
os.makedirs(destination_folder, exist_ok=True)

# 计数器
count = 0

# 遍历文件夹
for filename in os.listdir(source_folder):
    if filename.lower().endswith(valid_extensions):
        source_path = os.path.join(source_folder, filename)
        try:
            with Image.open(source_path) as img:
                width, height = img.size
                if width % 16 == 0 and height % 16 == 0:
                    # 满足条件，复制到目标文件夹
                    dest_path = os.path.join(destination_folder, filename)
                    shutil.copy2(source_path, dest_path)
                    count += 1
        except Exception as e:
            print(f"跳过无法打开的图片 {filename}: {e}")

print(f"成功复制了 {count} 张图片到 {destination_folder}")
