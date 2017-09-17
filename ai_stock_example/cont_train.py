from keras.layers import Dense, LSTM, Activation, BatchNormalization, Dropout, initializers, Input
# from renormalization import BatchRenormalization
from keras.models import Sequential
from keras.optimizers import SGD, RMSprop, Adam
from keras.models import load_model
from keras.callbacks import TensorBoard, ModelCheckpoint
import bcolz
import numpy as np

########################### load dataset ###########################
# train_dev_test_no_norm_no_group_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/no_norm_no_group"
# train_feature_array, dev_feature_array, test_feature_array = bcolz.open(train_dev_test_no_norm_no_group_path)

# train_dev_test_stad_no_group_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_no_group"
# train_feature_stad_array, dev_feature_stad_array, test_feature_stad_array = bcolz.open(train_dev_test_stad_no_group_path)
#
# train_dev_test_mimax_no_group_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_mimax_no_group"
# train_feature_mimax_array, dev_feature_mimax_array, test_feature_mimax_array = bcolz.open(train_dev_test_mimax_no_group_path)
#
# train_dev_test_group_no_norm_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/group_no_norm/"
# train_feature_group_array, dev_feature_group_array, test_feature_group_array = bcolz.open(train_dev_test_group_no_norm_path)
#
# train_dev_test_features_group_norm_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_group_norm/"
# train_feature_group_norm_array, dev_feature_group_norm_array, test_feature_group_norm_array = bcolz.open(train_dev_test_features_group_norm_path)
#
# train_dev_test_stad_group_norm_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_group_stad/"
# train_feature_stad_group_norm_array, dev_feature_stad_group_norm_array, test_feature_stad_group_norm_array = bcolz.open(train_dev_test_stad_group_norm_path)
#
# train_dev_target_weight_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm/"
# train_target_array, dev_target_array, train_weight_array, dev_weight_array, train_weight_stad_array, dev_weight_stad_array, train_weight_mimax_array, dev_weight_mimax_array = bcolz.open(train_dev_target_weight_path)

train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/train_dev_test_sequence.npz"

npzfiles = np.load(train_dev_test_sequence_path)
train_feature_stad_group_norm_array = npzfiles['train_sequence']
dev_feature_stad_group_norm_array = npzfiles['dev_sequence']
test_feature_stad_group_norm_array = npzfiles['test_sequence']

train_dev_target_weight_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm_dir/"
train_target_array, dev_target_array, train_weight_array, dev_weight_array, train_weight_stad_array, train_weight_mimax_array, dev_weight_stad_array, dev_weight_mimax_array = bcolz.open(train_dev_target_weight_path)

print("dataset loaded")
#################################################################################


# 处理样本权重 ###########################
# train_weight_flat = None
# dev_weight_flat = None
train_weight_flat = train_weight_array.flatten() # 使用weight，但不做标准化
dev_weight_flat = dev_weight_array.flatten()
# train_weight_flat = train_weight_stad_array.flatten() # standardScaler
# dev_weight_flat = dev_weight_stad_array.flatten()
# train_weight_flat = train_weight_mimax_array.flatten() # minmaxScaler
# dev_weight_flat = dev_weight_mimax_array.flatten()

log_dir = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/logs"
model_file = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/best.h5"

# 选用哪一组处理过的特征值 ###########################
# train_set_features = train_feature_group_norm_array  # features 不标准化，group 标准化
train_set_features = train_feature_stad_group_norm_array  # features 标准化，group 标准化
train_set_target = train_target_array

# dev_set_features = dev_feature_group_norm_array  # features 不标准化，group 标准化
dev_set_features = dev_feature_stad_group_norm_array # # features 标准化，group 标准化
dev_set_target = dev_target_array


##################### load model and continue to train #########################

model_path="/Users/Natsume/Documents/AI-challenger-stocks/model_output/last.h5"

model = load_model(model_path)

model.summary()

history = model.fit(train_set_features, # x: 训练特征值
            train_set_target, # y: 训练目标值
            batch_size=1024, # 一次性使用多少个样本一起计算
            epochs=1000, # 训练次数
            verbose=1,  # 是否打印每次训练的损失值和准确度

            # validation_split=0.2, # 从训练数据集中取多少作为验证数据 0.2，就是取剩下的20%作为验证
            validation_data=(dev_set_features, dev_set_target, dev_weight_flat), # 或者另外使用独立的验证数据，None 是没有另外数据; 如果dev set 也有权重，添加在这里
            shuffle=True, # 是否每次训练前打乱样本顺序
            class_weight=None, # 目标值的权重设置
            sample_weight=train_weight_flat, # 样本的权重设置
            initial_epoch=300, # 从第几个训练开始训练
			# 是否使用其他预处理功能
            callbacks=[TensorBoard(histogram_freq=1,
                                     log_dir=log_dir), # 画图保存
                  ModelCheckpoint(filepath=model_file, save_best_only=True, mode='min')]) # 训练时保存最优秀的模型，并非最后一轮训练的模型版本


model_last_file = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/last.h5"
model.save(model_last_file)



#################### 保存不同模型和训练出来的 loss, accuracy ######################################
###############################################################################################
history.history.keys()
loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['binary_accuracy']
val_acc = history.history['val_binary_accuracy']

losses_file = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/losses.npy"
import os.path

if os.path.isfile(losses_file):
    losses_accss = np.load(losses_file).tolist() # 变成dict
else:
	losses = {}

loss_name = "my_loss" # loss_weight_orig, val_loss_orig, loss_weight_stad, val_loss_weight_stad
val_loss_name = "val_loss"
acc_name = 'my_acc'
val_acc_name = 'val_acc'

losses_accss[loss_name] = loss
losses_accss[val_loss_name] = val_loss
losses_accss[acc_name] = acc
losses_accss[val_acc_name] = val_acc
np.save(losses_file, losses_accss)

print("-----------------training model_no_weight-----------------")
## display log
# 模型1: 1 hidden 2 neurons, lr = 0.001, 训练验证集无标准化，无group, weight 无标准化
# tensorboard --logdir "/Users/Natsume/Documents/AI-challenger-stocks/model_output/logs"
