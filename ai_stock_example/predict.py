import numpy as np
import pandas as pd
from keras.models import load_model
import bcolz
import matplotlib.pyplot as plt


########################### 2-d 数据 ###########################################
# train_dev_test_features_group_norm_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_group_norm/"
# train_feature_group_norm_array, dev_feature_group_norm_array, test_feature_group_norm_array = bcolz.open(train_dev_test_features_group_norm_path)
#
# train_dev_test_stad_group_norm_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_group_stad/"
# train_feature_stad_group_norm_array, dev_feature_stad_group_norm_array, test_feature_stad_group_norm_array = bcolz.open(train_dev_test_stad_group_norm_path)

train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/train_dev_test_sequence.npz"

npzfiles = np.load(train_dev_test_sequence_path)
train_feature_stad_group_norm_array = npzfiles['train_sequence']
dev_feature_stad_group_norm_array = npzfiles['dev_sequence']
test_feature_stad_group_norm_array = npzfiles['test_sequence']
#################################################################################


############################## 直接将 2-d 数据用于 sequence #######################
# test_feature_group_norm_array = test_feature_group_norm_array.reshape((-1, 1, 89))
# test_feature_stad_group_norm_array = test_feature_stad_group_norm_array.reshape((-1, 1, 89))
#################################################################################



####################### for 3-d sequence dataset ################################
# 周期是5天

# train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_group_stad/"
# train_feature_stad_group_norm_array, dev_feature_stad_group_norm_array, test_feature_stad_group_norm_array = bcolz.open(train_dev_test_sequence_path)
#
# train_dev_target_weight_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm/"
# train_target_array, dev_target_array, train_weight_array, dev_weight_array = bcolz.open(train_dev_target_weight_sequence_path)
##########################################################################################



# load model
# model_path="/Users/Natsume/Documents/AI-challenger-stocks/model_output/last.h5"
model_path="/Users/Natsume/Documents/AI-challenger-stocks/model_output/best.60-0.6880.hdf5"
model = load_model(model_path)

# model predict
# pred = model.predict(test_feature_group_norm_array)
pred = model.predict(test_feature_stad_group_norm_array) #


############################## prepare output for submission ##############################
# get test id
test_index = np.load("/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/test_index.npy")
out = pd.concat([pd.DataFrame(test_index), pd.DataFrame(pred)], axis=1)
out.columns = ['id', 'proba']
out_id_index = out.set_index('id')
out_id_index.to_csv("/Users/Natsume/Documents/AI-challenger-stocks/model_output/rnn_lstm.csv")

# check prediction distribution
mean = out_id_index.describe().loc['mean','proba']
std = out_id_index.describe().loc['std','proba']
plt.hist(out_id_index.values, bins=100)
plt.title("mean: "+str(mean)+", std: "+str(std))
plt.show()
