import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bcolz
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# load train, test set from csv
# csv: id, headers
# train_set file: contain training and dev set
# test_set file: just test set
# return (train_set, test_set, test_id)
def get_train_test_sets(train_file, test_file):
	# print all rows and columns when needed
    pd.get_option('display.max_rows')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_column_width', None)

	# load into pd.DataFrame
    train_set = pd.read_csv(train_file)
    test_set = pd.read_csv(test_file)

	# extract test_set id Series, for submission
    test_id = test_set.loc[:, 'id']

	# use id as index
    train_set.set_index('id', inplace=True) # set id as index
    test_set.set_index('id', inplace=True)
    return (train_set, test_set, test_id)

# standarize all features with standard scaler or mimax scaler
# raw_features: np.array or pd.DataFrame
# scaler: stad or mimax
# return: np.array
def standardization(raw_features, scaler='stad'):
	# standardize arrays: stad vs mimax
    """ raw_features: pd.DataFrame or np.array both ok
    """
    if scaler == 'stad':
        standardized_features = StandardScaler().fit_transform(raw_features)
    elif scaler == 'mimax':
        standardized_features = MinMaxScaler().fit_transform(raw_features)
    return standardized_features

# combine train_set and test_set
# train and test sets are pd.DataFrame
# train_set: 包含training and validation sets
# select features
# combine train and test
# standardize it all
# return np.array
def combine_train_test(train_set, test_set):
	# drop unwanted to select wanted
    train_features_group = train_set.drop(['weight', 'era', 'label'], axis=1)
	# pd.concat to merge dataframes
    train_test_combine = pd.concat([train_features_group, test_set], axis=0).values
	# use a custom function called standarization(...)
    train_test_combine = standardization(train_test_combine, scaler='stad') # standarization

    return train_test_combine

# make (samples, features) into (samples, window, features)
# train_test_combine: np.array, window: time_steps
# return np.array (samples, window, features)
def make_steps(train_test_combine, window=5):
    p = 0 # 计数
    features_list = [] # 特征值容器

	# must use "<" here !!!! due to target is one day forward
    while p + window < train_test_combine.shape[0]:
        x = train_test_combine[p:p + window, :]
		# 第一次循环：A_arr[0:30,:] 实际[0,1,2...29], 第二次循环：A_arr[1:31,:]...
		# 每30天为一个新样本，赋值给x，一天一天往前推进

        features_list.append(x)
        p += 1
	# 将list 转化为 np.array
    train_test_sequence = np.asarray(features_list)
    return train_test_sequence

	# 第0-29天是特征值， 第一个target 是从 label[30] 的label 开始的, 不是label[29]

# split into train_sequence, train_target, train_weight,
# dev_sequence, dev_target, dev_weight, test_sequence
def split_train_dev(train_dev_set, train_test_sequence, n_test, odd_even=True, window=5):
    # train_dev_set: 包含training and validation sets, pd.DataFrame
    target = train_dev_set.loc[window:, 'label'] # label[30] 开始
    weight = train_dev_set.loc[window:, 'weight'] # 用与损失函数中的样本权重，时间位置应该与目标值对应上
    era = train_dev_set.loc[window:, 'era'] # 用于划分 dev set


    train_target = target.values[era.values % 2 == 1]
    train_weight = weight.values[era.values % 2 == 0]
    dev_target = target.values[era.values % 2 == 1]
    dev_weight = weight.values[era.values % 2 == 0]
    # train_target = target.values[(era.values != 20)]
    # train_weight = weight.values[(era.values != 20)]
    # dev_target = target.values[(era.values == 20)]
    # dev_weight = weight.values[(era.values == 20)]

    test_sequence = train_test_sequence[-n_test:, :,:]
    train_dev_sequence = train_test_sequence[:-n_test, :,:]

	# how to select for train and dev sets
    if odd_even:
		# all odd era to be train_set, all even era to be dev set
	    train_sequence = train_dev_sequence[era.values % 2 == 1, :, :] # training set
	    dev_sequence = train_dev_sequence[era.values % 2 == 0, :, :] # training set
    else:
		# select particular era to be train and dev sets
        train_sequence = train_set.loc[(era.values!=20) & (era.values!=10),:,:]
        dev_sequence = train_set.loc[(era.values==20) | (era.values==10),:,:]

    return (train_sequence, train_target, train_weight, dev_sequence, dev_target, dev_weight, test_sequence) # only for train and dev combined

# save large np.arrays
def save_large_arrays(dir_path, list_arrays):
	c = bcolz.carray(list_arrays, rootdir=dir_path, mode='w')
	c.flush()
	print("saved %d arrays" % len(list_arrays))

# see all features distributions in one fiture
# features_array must be 2-d
def all_features_distribution(features_array, first=None, middle=None, last=None):
	if first is not None:
		features_array.iloc[:, :first].hist()
		plt.show()
	if last is not None:
		features_array.iloc[:, -last:].hist()
		plt.show()
	if middle is not None:
		mid = round(features_array.shape[1]/2)
		half_middle = round(middle/2)
		features_array.iloc[:, (mid-half_middle):(mid+half_middle)].hist()
		plt.show()


# examples
# 选择数据版本 20170910
def tests():
	# test get_train_test_sets()
	train_file = "/Users/Natsume/Documents/AI-challenger-stocks/train_data/20170910/ai_challenger_stock_train_20170910/stock_train_data_20170910.csv"
	test_file = "/Users/Natsume/Documents/AI-challenger-stocks/test_data/20170910/ai_challenger_stock_test_20170910/stock_test_data_20170910.csv"
	train_dev_set, test_set, test_id = get_train_test_sets(train_file=train_file, test_file=test_file)

	# display features distributions: first, middle, last few features if too many
	all_features_distribution(train_dev_set, middle=20)

	# 保存test_set ID 信息
	np.save("/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/test_index.npy", test_id)

	# test standardization() and combine_train_test()
	train_test_combine = combine_train_test(train_set=train_dev_set, test_set=test_set)
	train_test_combine.shape

	# test make_steps()
	train_test_sequence = make_steps(train_test_combine=train_test_combine)

	# test split_train_dev()
	n_test = test_set.shape[0]
	train_features_sequence, train_target, train_weight, dev_features_sequence, dev_target, dev_weight, test_sequence = split_train_dev(train_dev_set, train_test_sequence, n_test=n_test)

	# test for save_large_arrays()
	# paths for storing preprocessed dataset
	train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_group_stad/"
	train_dev_target_weight_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm/"
	list_seqs = [train_features_sequence,dev_features_sequence,test_sequence]
	save_large_arrays(train_dev_test_sequence_path, list_arrays=list_seqs)
	list_tw = [train_target, dev_target, train_weight, dev_weight]
	save_large_arrays(dir_path=train_dev_target_weight_sequence_path, list_arrays=list_tw)

tests()
