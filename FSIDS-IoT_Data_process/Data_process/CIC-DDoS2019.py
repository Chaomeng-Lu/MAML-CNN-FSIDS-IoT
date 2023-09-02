import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

path = 'J:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/IDSFS_Original/CIC-DDoS2019/'
path1 = 'J:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/RIDS_28_28_RGBA/CIC-DDoS2019/'

files = os.listdir(path)
for file in files:
    pathf = os.path.join(path, file)
    data = pd.read_csv(pathf)  # 读取数据
    data = np.array(data)
    # print(data.shape)
    # data = data[:,:-1]
    few_data = data[:20,7:-1]
    few_data = np.delete(few_data, -2, axis=1)
    s = 1
    patht = os.path.join(path1, file)
    if not os.path.isdir(patht):
        os.makedirs(patht)
    # 特征数 = 78
    for sample in few_data:
        # print(sample)
        n = 28
        matrix = np.zeros((n,n))
        # print(matrix)
        # matrix[0][0] = sample[0]
        i = 0
        for j in range(n*n-5):
            if (j+1)%10 == 6:
                # print((j+1)//n,(j+1)%n)
                p, q = (j+1)//n,(j+1)%n
                matrix[p][q] = sample[i]
                i = i+1
        # print(matrix)
        # temp = pd.DataFrame(matrix)
        # temp.to_csv('result1.csv', header=0, index=0)
        # np.savetxt("result1.txt", matrix)
        # sys.exit(0)
        # plt.imshow(matrix, plt.cm.gray)   #生成灰度图像

        # 矩阵转图像方法三
        # import cv2
        # import numpy as np
        # cv2.imwrite(patht+'/pic-'+str(s)+'.png', matrix)

        # 矩阵转图像方法二 #
        matplotlib.image.imsave(patht+'/pic-'+str(s)+'.png', matrix)

        # path55 = 'J:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for MAML/RIDS_28_28_RGBA/CIC-DDoS2019/01-12_DrDoS_DNS_extract5000.csv/pic-19.png'
        # ar = matplotlib.image.imread(patht+'/pic-'+str(s)+'.png', format=None)
        # ar = matplotlib.image.imread(path55, format=None)
        # for i in range(4):
        #     ar1 = ar[:, :, i]
        #     temp = pd.DataFrame(ar1)
        #     temp.to_csv('result2-'+ str(i) +'.csv', header=0, index=0)

        # np.savetxt("result2.txt", ar.reshape(1,-1))

        #矩阵转图像方法一
        # plt.imshow(matrix)
        # plt.axis('off')
        # plt.savefig(patht+'/pic-'+str(s)+'.png', dpi=22.8, bbox_inches='tight', pad_inches=0) #plt.savefig('./img/pic-{}.png'.format(epoch + 1))
        s = s+1
        sys.exit(0)