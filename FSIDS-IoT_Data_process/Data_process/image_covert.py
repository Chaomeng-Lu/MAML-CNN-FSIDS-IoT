from PIL import Image

# im = Image.open("F:/GraduateStudy/TensorflowProject/MAML/maml-master/data/IDSFS_Test/CIC-DDoS2019/BENIGN/pic-1.png")
# im = Image.open("F:/GraduateStudy/TensorflowProject/MAML/maml-master/data/omniglot_resized/Alphabet_of_the_Magi/character01/0709_01.png")
# print(im.getbands())
# from PIL import Image
# import numpy as np
#
# img = Image.open('F:/GraduateStudy/TensorflowProject/MAML/maml-master/data/IDSFS_Test/CIC-DDoS2019/BENIGN/pic-1.png').convert('1')
# print(img.getbands()) # ('P',) 这种是有彩色的，而L是没有彩色的
# img.save('F:/GraduateStudy/TensorflowProject/MAML/maml-master/data/IDSFS_Test/CIC-DDoS2019/BENIGN/pic-1-0.png') # 转换后的进行保存

import os

path = "J:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/RIDS_28_28_RGBA/UNSW-NB15/"
path1 = "J:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/RIDS_84_84_RGB/UNSW-NB15/"


folders = os.listdir(path)
# files = os.listdir(path)
# print(files)
for folder in folders:
    folder_path = os.path.join(path, folder)
    files = os.listdir(folder_path)
    # save_path = path1+folder
    save_path = os.path.join(path1, folder)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    for pic in files:
        # print(pic)
        img = Image.open(os.path.join(folder_path, pic)).convert('RGB')
        img = img.resize((84, 84), resample=Image.LANCZOS)
        print(img.getbands())  # ('P',) 这种是有彩色的，而L是没有彩色的
        print(img.size)

        # file_name, file_extend = os.path.splitext(pic)
        # print(file_name,file_extend)
        # pic_new = os.path.join(os.path.abspath(save_path), file_name + '.jpg')

        # pic_new = os.path.join(os.path.abspath(save_path), pic)
        pic_new = os.path.join(save_path, pic)

        img.save(pic_new)
