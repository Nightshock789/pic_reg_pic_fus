import os, cv2

vis_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\vis_dir'
ir_dir = r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\ir_dir'

for fname in os.listdir(vis_dir):
    vis_path = os.path.join(vis_dir, fname)
    ir_path = os.path.join(ir_dir, fname)

    if not os.path.exists(ir_path):
        print(f"[错误] 找不到红外图: {ir_path}")
        continue

    vis = cv2.imread(vis_path)
    ir = cv2.imread(ir_path)

    if vis is None:
        print(f"[错误] 可见光图读取失败: {vis_path}")
    if ir is None:
        print(f"[错误] 红外图读取失败: {ir_path}")
