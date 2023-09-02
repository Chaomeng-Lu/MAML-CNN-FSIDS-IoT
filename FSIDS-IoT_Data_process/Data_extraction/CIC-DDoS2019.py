import sys
import pandas as pd

path = 'I:/Temp/临时3/CIC-DDoS2019-reduce/01-12/'

#01-12
csv_data0 = pd.read_csv(path+'DrDoS_DNS.csv')  # 读取数据
csv_data1 = pd.read_csv(path+'DrDoS_LDAP.csv')  # 读取数据
csv_data2 = pd.read_csv(path+'DrDoS_MSSQL.csv')  # 读取数据
csv_data3 = pd.read_csv(path+'DrDoS_NetBIOS.csv')  # 读取数据
csv_data4 = pd.read_csv(path+'DrDoS_NTP.csv')  # 读取数据
csv_data5 = pd.read_csv(path+'DrDoS_SNMP.csv')  # 读取数据
csv_data6 = pd.read_csv(path+'DrDoS_SSDP.csv')  # 读取数据
csv_data7 = pd.read_csv(path+'DrDoS_UDP.csv')  # 读取数据
csv_data8 = pd.read_csv(path+'Syn.csv')  # 读取数据
csv_data9 = pd.read_csv(path+'TFTP.csv')  # 读取数据
csv_data10 = pd.read_csv(path+'UDPLag.csv')  # 读取数据
csv_data = pd.concat([csv_data1, csv_data2])
csv_data = pd.concat([csv_data, csv_data3])
csv_data = pd.concat([csv_data, csv_data0])
csv_data = pd.concat([csv_data, csv_data4])
csv_data = pd.concat([csv_data, csv_data5])
csv_data = pd.concat([csv_data, csv_data6])
csv_data = pd.concat([csv_data, csv_data7])
csv_data = pd.concat([csv_data, csv_data8])
csv_data = pd.concat([csv_data, csv_data9])
csv_data = pd.concat([csv_data, csv_data10])

#03-11
# csv_data1 = pd.read_csv(path+'LDAP.csv')  # 读取数据
# csv_data2 = pd.read_csv(path+'MSSQL.csv')  # 读取数据
# csv_data3 = pd.read_csv(path+'NetBIOS.csv')  # 读取数据
# csv_data4 = pd.read_csv(path+'Portmap.csv')  # 读取数据
# csv_data5 = pd.read_csv(path+'Syn.csv')  # 读取数据
# csv_data6 = pd.read_csv(path+'UDP.csv')  # 读取数据
# csv_data7 = pd.read_csv(path+'UDPLag.csv')  # 读取数据
# csv_data = pd.concat([csv_data1, csv_data2])
# csv_data = pd.concat([csv_data, csv_data3])
# csv_data = pd.concat([csv_data, csv_data4])
# csv_data = pd.concat([csv_data, csv_data5])
# csv_data = pd.concat([csv_data, csv_data6])
# csv_data = pd.concat([csv_data, csv_data7])

print(csv_data.shape)
# print(csv_data.columns)
labels = csv_data[' Label'].value_counts()
print(labels)

# csv_data = csv_data.drop(['Unnamed: 0'], axis=1)    # 去除无价值属性

labels_values_counts = csv_data[' Label'].value_counts()
labels_values = labels_values_counts.index

path1 = 'I:/Temp/临时3/CIC-DDos2019FS/01-12/01-12_'

n = 5000      # 抽取数据量

for labels_value in labels_values:
    df_sample = csv_data[csv_data[' Label'] == labels_value]
    sample_count = df_sample[' Label'].value_counts()
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