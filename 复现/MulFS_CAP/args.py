
import argparse

parser = argparse.ArgumentParser(description='**MulFS-CAP**')
parser.add_argument('--vis_train_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\vis_dir', type=str)
parser.add_argument('--ir_train_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\ir_dir', type=str)
parser.add_argument('--vis_test_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\vis_dir', type=str)
parser.add_argument('--ir_test_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\ir_dir', type=str)

parser.add_argument('--train_save_img_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\check_point\image', type=str)
parser.add_argument('--train_save_model_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\check_point\model', type=str)
parser.add_argument('--pretrain_model_dir', default=r'P:\pic_reg_and_pic_fus\learning\MulFS-CAP\pretrained')
parser.add_argument('--save_image_num', dest='save_image_num', default=1, type=int)
parser.add_argument('--save_model_num', dest='save_model_num', default=10, type=int)
parser.add_argument('--img_size', type=int, default=256)
parser.add_argument('--small_w_size', type=float, default=16)
parser.add_argument('--large_w_size', type=float, default=16)
parser.add_argument('--batch_size', dest='batch_size', default=1, type=int)
parser.add_argument('--LR', type=float, default=0.0002)
parser.add_argument('--LR_target', type=float, default=0.001)
parser.add_argument('--Epoch', type=float, default=10)
parser.add_argument('--Warm_epoch', type=float, default=160)
parser.add_argument('--dropout', type=float, default=0.1)
args = parser.parse_args()