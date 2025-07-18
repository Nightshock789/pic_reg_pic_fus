import os
import cv2

# 输入文件夹路径
ir_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\ir_dir'
vis_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\vis_dir'

# 输出文件夹路径
cropped_ir_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\cropped_ir'
cropped_vis_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\cropped_vis'

# 创建输出目录（如不存在）
os.makedirs(cropped_ir_dir, exist_ok=True)
os.makedirs(cropped_vis_dir, exist_ok=True)

# 裁剪区域（手动指定）
crop_x, crop_y = 0, 0       # 左上角坐标
crop_w, crop_h = 256, 256   # 裁剪尺寸

# 遍历可见光图像，并寻找对应的红外图像
for filename in os.listdir(vis_dir):
    vis_path = os.path.join(vis_dir, filename)
    ir_path = os.path.join(ir_dir, filename)

    if not os.path.exists(ir_path):
        print(f"跳过 {filename}，因红外图不存在")
        continue

    # 读取图像
    vis_img = cv2.imread(vis_path)
    ir_img = cv2.imread(ir_path)

    if vis_img is None or ir_img is None:
        print(f"跳过 {filename}，因图像读取失败")
        continue

    # 检查图像是否大于裁剪尺寸
    if (vis_img.shape[1] < crop_x + crop_w or vis_img.shape[0] < crop_y + crop_h or
        ir_img.shape[1] < crop_x + crop_w or ir_img.shape[0] < crop_y + crop_h):
        print(f"跳过 {filename}，因图像尺寸过小")
        continue

    # 执行裁剪
    vis_crop = vis_img[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]
    ir_crop = ir_img[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]

    # 保存
    cv2.imwrite(os.path.join(cropped_vis_dir, filename), vis_crop)
    cv2.imwrite(os.path.join(cropped_ir_dir, filename), ir_crop)

    print(f"已裁剪并保存 {filename}")

print("✅ 批量裁剪完成！")
