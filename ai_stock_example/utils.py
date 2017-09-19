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
def combine_train_test(train_dev_set, test_set):
	# drop unwanted to select wanted
    train_dev_features = train_dev_set.drop(['weight', 'era', 'label', 'group'], axis=1)
    test_set = test_set.drop(['group'], axis=1)
	# pd.concat to merge dataframes
    train_test_combine = pd.concat([train_dev_features, test_set], axis=0).values
	# use a custom function called standarization(...)
    train_test_combine = standardization(train_test_combine, scaler='stad') # standarization

    return train_test_combine

# make (samples, features) into (samples, window, features)
# train_test_combine: np.array, window: time_steps
# return np.array (samples, window, features)
def make_steps(train_test_combine, window=1):
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
    if window == 1:
        train_test_sequence = train_test_sequence.reshape((train_test_sequence.shape[0], train_test_sequence.shape[2]))
    return train_test_sequence

	# 第0-29天是特征值， 第一个target 是从 label[30] 的label 开始的, 不是label[29]

# split into train_sequence, train_target, train_weight,
# dev_sequence, dev_target, dev_weight, test_sequence
def split_train_dev(train_dev_set=None, test_set=None, train_test_sequence=None, odd_even=False, window=1):
    # train_dev_set: 包含training and validation sets, pd.DataFrame,
    if window == 1:
        target = train_dev_set.loc[:, 'label'] # label[30] 开始
        weight = train_dev_set.loc[:, 'weight'] # 用与损失函数中的样本权重，时间位置应该与目标值对应上
        era = train_dev_set.loc[:, 'era'] # 用于划分 dev set
    else:
        target = train_dev_set.loc[window:, 'label'] # label[30] 开始
        weight = train_dev_set.loc[window:, 'weight'] # 用与损失函数中的样本权重，时间位置应该与目标值对应上
        era = train_dev_set.loc[window:, 'era'] # 用于划分 dev set

    weight = standardization(weight.values.reshape((-1,1)), scaler='mimax') # input array must be 2-d
    weight = pd.DataFrame(weight)

    if window == 1:
		# drop unwanted features or columns, remove group!!!!! or not !!!
        test_sequence = test_set.drop(['group'], axis=1)
        train_dev_sequence = train_dev_set.drop(['group','weight', 'era', 'label'], axis=1)
        # test_sequence = test_set
        # train_dev_sequence = train_dev_set.drop(['weight', 'era', 'label'], axis=1)
    else:
        n_test = test_set.shape[0]
        test_sequence = train_test_sequence[-n_test:, :,:]
        train_dev_sequence = train_test_sequence[:-n_test, :,:]

	# how to select for train and dev sets
    if odd_even:
		# all odd era to be train_set, all even era to be dev set
        if window == 1:
            train_sequence = train_dev_sequence[era.values % 2 == 1, :] # training set
            dev_sequence = train_dev_sequence[era.values % 2 == 0, :] # training set
        else:
            train_sequence = train_dev_sequence[era.values % 2 == 1, :, :] # training set
            dev_sequence = train_dev_sequence[era.values % 2 == 0, :, :] # training set
        train_target = target.values[era.values % 2 == 1]
        train_weight = weight.values[era.values % 2 == 0]
        dev_target = target.values[era.values % 2 == 1]
        dev_weight = weight.values[era.values % 2 == 0]
    else:
		# select particular era to be train and dev sets
        if window == 1:
			# select by era number
            train_sequence = train_dev_sequence.loc[(era.values!=2) & (era.values!=1),:]
            # train_sequence = train_dev_sequence.loc[(era.values>14),:]
            dev_sequence = train_dev_sequence.loc[(era.values==2) | (era.values==1),:]

        else:
            train_sequence = train_dev_sequence.loc[(era.values!=2) & (era.values!=1),:,:]
            dev_sequence = train_dev_sequence.loc[(era.values==2) | (era.values==1),:,:]
        train_target = target.values[(era.values!=2) & (era.values!=1)]
        train_weight = weight.values[(era.values!=2) & (era.values!=1)]
        # train_target = target.values[(era.values>14)]
        # train_weight = weight.values[(era.values>14)]
        dev_target = target.values[(era.values==2) | (era.values==1)]
        dev_weight = weight.values[(era.values==2) | (era.values==1)]

    # train_weight_stad = standardization(train_weight.reshape((-1,1))) # input array must be 2-d
    # dev_weight_stad = standardization(dev_weight.reshape((-1,1)))
    # train_weight_mimax = standardization(train_weight.reshape((-1,1)), scaler='mimax')
    # dev_weight_mimax = standardization(dev_weight.reshape((-1,1)), scaler='mimax')

    return (train_sequence, train_target, train_weight, dev_sequence, dev_target, dev_weight, test_sequence) # only for train and dev combined

# save large np.arrays
# list_arrays: can only be 1-d arrays, not for 2-d or 3-d arrays
# learn h5
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
	train_file = "/Users/Natsume/Documents/AI-challenger-stocks/train_data/20170916/ai_challenger_stock_train_20170916/stock_train_data_20170916.csv"
	test_file = "/Users/Natsume/Documents/AI-challenger-stocks/test_data/20170916/ai_challenger_stock_test_20170916/stock_test_data_20170916.csv"
	train_dev_set, test_set, test_id = get_train_test_sets(train_file=train_file, test_file=test_file)

	# display features distributions: first, middle, last few features if too many
	all_features_distribution(train_dev_set, middle=20)

	# 保存test_set ID 信息
	np.save("/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/test_index.npy", test_id)

	# test standardization() and combine_train_test()
	train_test_combine = combine_train_test(train_dev_set=train_dev_set, test_set=test_set)
	m = train_test_combine.shape[0]

	# only use the later half of dataset to train, validate, test
	# train_test_combine = train_test_combine[np.floor(m/2):,:]

	# test make_steps()
	train_test_sequence = make_steps(train_test_combine=train_test_combine)

	# test split_train_dev()
	train_sequence, train_target, train_weight, dev_sequence, dev_target, dev_weight, test_sequence = split_train_dev(train_dev_set=train_dev_set, test_set=test_set, train_test_sequence=train_test_sequence)


	# test for save_large_arrays()
	# use np.save for individual array as npy file
	# train_sequence_file = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/train_sequence.npy"
	# dev_sequence_file = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/dev_sequence.npy"
	# test_sequence_file = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/test_sequence.npy"
	#
	# np.save(train_sequence_file, train_sequence)
	# np.save(dev_sequence_file, dev_sequence)
	# np.save(test_sequence_file, test_sequence)

	# use np.savez for more arrays as npz file
	train_dev_test_sequence_npz = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/train_dev_test_sequence.npz"
	train_dev_target_weight_sequence_npz = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm.npz"
	train_dev_target_weight_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm_dir/"

	list_arrays = [train_target, dev_target, train_weight, dev_weight]
	save_large_arrays(train_dev_target_weight_sequence_path, list_arrays)

	np.savez(train_dev_target_weight_sequence_npz, train_target=train_target, dev_target=dev_target, train_weight=train_weight, dev_weight=dev_weight)

	np.savez(train_dev_test_sequence_npz, train_sequence=train_sequence,dev_sequence=dev_sequence,test_sequence=test_sequence)

	npzfiles = np.load(train_dev_test_sequence_npz)
	npzfiles['train_sequence'].shape




tests()
