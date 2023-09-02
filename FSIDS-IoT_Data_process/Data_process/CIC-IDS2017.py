import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

path = 'G:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/IDSFS_Original/CIC-IDS2017/'
path1 = 'G:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/RIDS_28_28_RGBA/CIC-IDS2017/'

files = os.listdir(path)
for file in files:
    pathf = os.path.join(path, file)
    data = pd.read_csv(pathf)  # 读取数据
    data = np.array(data)
    few_data = data[:20, 1:-1]
    # print(few_data.shape)
    # print(few_data[0, :])
    # sys.exit(0)
    # print(few_data.shape)
    # print(few_data[0,:])
    # sample = few_data[17,:]
    patht = os.path.join(path1, file)
    if not os.path.isdir(patht):
        os.makedirs(patht)
    s = 1
    # 特征数 = 77
    for sample in few_data:
        # print(sample)
        n = 28
        matrix = np.zeros((n,n))
        # print(matrix)
        # matrix[0][0] = sample[0]
        i = 0
        for j in range(n*n-10):
            if (j+1)%10 == 6:
                # print((j+1)//n,(j+1)%n)
                p, q = (j+1)//n,(j+1)%n
                matrix[p][q] = sample[i]
                i = i+1

        # plt.imshow(matrix, plt.cm.gray)   #生成灰度图像
        # np.savetxt('Text/result' + str(s) + '.txt', matrix)
        # 矩阵转图像方法二
        matplotlib.image.imsave(patht + '/pic-' + str(s) + '.png', matrix)

        # plt.imshow(matrix)
        # plt.axis('off')
        # plt.savefig(patht+'pic-'+str(s)+'.png', dpi=7.3, bbox_inches='tight') #plt.savefig('./img/pic-{}.png'.format(epoch + 1))
        # plt.savefig(patht + '/pic-' + str(s) + '.png', dpi=22.8, bbox_inches='tight',
        #             pad_inches=0)  # plt.savefig('./img/pic-{}.png'.format(epoch + 1))
        s = s+1