import threading
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class DataSource:
    def __init__(self, few_data, startLine=0, maxcount=None):
        # self.dataFileName = few_data
        self.startLine = startLine  # 第一行行号为1
        self.line_index = startLine # 当前读取位置
        self.maxcount = maxcount  # 读取最大行数
        self.lock = threading.RLock() # 同步锁
        self.__data__ = few_data

        # self.__data__ = open(self.dataFileName, 'r', encoding= 'utf-8')
        for i in range(self.startLine):
            l = self.__data__.readline()

    def getLine(self):
        self.lock.acquire()
        try:
            if self.maxcount is None or self.line_index < (self.startLine + self.maxcount):
                line = self.__data__[self.line_index]
                # print('line:',line)
                # sys.exit(0)
                if len(line):
                    self.line_index += 1
                    return True, line
                else:
                    return False, None
            else:
                return False, None

        except Exception as e:
            return False, "处理出错:" + e.args
        finally:
            self.lock.release()

    # def __del__(self):
    #     if not self.__data__.closed:
    #         self.__data__.close()
            # print("关闭数据源:", self.dataFileName)


def process(worker_id, datasource, patht):
    count = 0
    while True:
        status, data1 = datasource.getLine()
        # print(data)
        # sys.exit(0)
        if status:
            print(">>> 线程[%d] 获得数据， 正在处理……" % worker_id)
            n = 28
            matrix = np.zeros((n, n))
            # print(matrix)
            # matrix[0][0] = sample[0]
            i = 0
            for j in range(n * n - 5):
                if (j + 1) % 10 == 6:
                    # print((j+1)//n,(j+1)%n)
                    p, q = (j + 1) // n, (j + 1) % n
                    # sys.exit(0)
                    matrix[p][q] = data1[i]
                    i = i + 1
            plt.imshow(matrix)
            plt.axis('off')
            plt.savefig(patht + '/pic-' + str(count) + '.png', dpi=22.8, bbox_inches='tight',
                        pad_inches=0)  # plt.savefig('./img/pic-{}.png'.format(epoch + 1))
            print(">>> 线程[%d] 处理数据 完成" % worker_id)
            count += 1
        else:
            break # 退出循环
    print(">>> 线程[%d] 结束， 共处理[%d]条数据" % (worker_id, count))

def main():
    path = 'G:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/IDSFS-all5000extraction-new/CIC-DDoS2019/'
    path1 = 'G:/Desktop 2022.06.08 File Backup/GraduateStudy/DataSet/Processed data for G-CNN/RIDS_84_84_RGBA/CIC-DDoS2019/'

    files = os.listdir(path)
    for file in files:
        pathf = os.path.join(path, file)
        data = pd.read_csv(pathf)  # 读取数据
        data = np.array(data)
        # print(data.shape)
        # data = data[:,:-1]
        few_data = data[:, 7:-1]
        few_data = np.delete(few_data, -2, axis=1)
        # np.savetxt(file + '.csv', few_data)
        patht = os.path.join(path1, file)
        if not os.path.isdir(patht):
            os.makedirs(patht)
        datasource = DataSource(few_data)
        workercount = 10 # 开启的线程数，注意：并非越多越快哦
        workers = []
        for i in range(workercount):
            worker = threading.Thread(target=process, args=(i+1, datasource, patht))
            worker.start()
            workers.append(worker)

        for worker in workers:
            worker.join()

if __name__ == "__main__":
    main()