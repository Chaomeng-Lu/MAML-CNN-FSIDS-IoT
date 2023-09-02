import sys
import pandas as pd

path = 'F:/GraduateStudy/DataSet/UNSW-NB15/'

csv_data1 = pd.read_csv(path+'UNSW_NB15_testing-set.csv')  # 读取数据
csv_data2 = pd.read_csv(path+'UNSW_NB15_training-set.csv')  # 读取数据
csv_data = pd.concat([csv_data1, csv_data2])
# csv_data.to_csv('1.csv')
# sys.exit(0)
print(csv_data.shape)
# print(csv_data.columns)
# labels = csv_data['attack_cat'].value_counts()
# print(labels)
# sys.exit(0)

csv_data = csv_data.drop(['id', 'label'], axis=1)    # 去除无价值属性

print(csv_data.shape)
labels_values_counts = csv_data['attack_cat'].value_counts()
labels_values = labels_values_counts.index

path1 = 'F:/GraduateStudy/DataSet/!A-IDSFS/UNSW-NB15/'

n = 5000      # 抽取数据量

for labels_value in labels_values:
    df_sample = csv_data[csv_data['attack_cat'] == labels_value]
    sample_count = df_sample['attack_cat'].value_counts()
    if sample_count[0] >= 5000:
        df_sample = df_sample.sample(n)
        filepath = path1 + labels_value + '_extract'+str(n)+'.csv'  # 写入数据
    else:
        print("数据量不足"+str(n))
        filepath = path1 + labels_value + '_extract' + str(sample_count[0]) + '.csv'  # 写入数据
    df_columns = pd.DataFrame([list(csv_data.columns)])
    df_columns.to_csv(filepath, mode='w', header=False, index=0)
    df_sample.to_csv(filepath, mode='a', header=False, index=0)

# labels = csv_data['Label'].value_counts()
#
# print(labels)