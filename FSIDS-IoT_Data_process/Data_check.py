import pandas as pd

# csv_data = pd.read_csv('F:/GraduateStudy/DataSet/Z2--NSL-KDD/KDDTest+.txt')  # 读取训练数据

# print(csv_data.shape)
# print(csv_data.columns)
# labels = csv_data['LABEL'].value_counts()
# print(labels)
#
# df_sample1 = csv_data[csv_data['LABEL'] == 'Normal flow']
# df_sample1 = df_sample1.sample(100000)
#
# df_sample2 = csv_data[csv_data['LABEL'] == 'Denial of Service R-U-Dead-Yet']
# df_sample2 = df_sample2.sample(100000)
#
# df_sample3 = csv_data[csv_data['LABEL'] == 'Denial of Service Slowloris']
# df_sample3 = df_sample3.sample(100000)
# df_sample4 = pd.concat([df_sample1, df_sample2])
# df_sample = pd.concat([df_sample3, df_sample4])
#
# filepath = 'F:/GraduateStudy/DataSet/SIMARGL2021/dataset-part2-reduce.csv'
# df_columns = pd.DataFrame([list(csv_data.columns)])
# df_columns.to_csv(filepath, mode='w', header=False, index=0)
# df_sample.to_csv(filepath, mode='a', header=False, index=0)

#kddcup99
col_names = ["duration", "protocol_type", "service", "flag", "src_bytes",

             "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",

             "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
             "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",

             "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
             "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",

             "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
             "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
             "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",

             "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "r"]  # 42个标识

csv_data = pd.read_csv('F:/GraduateStudy/DataSet/Z2--NSL-KDD/KDDTest+.txt', names = col_names)  # 读取训练数据

print(csv_data.shape)
print(csv_data.columns)
labels = csv_data['label'].value_counts()
print(labels)

csv_data.to_csv("F:/GraduateStudy/DataSet/Z2--NSL-KDD/KDDTest+.csv", index=0)#另存为csv文件