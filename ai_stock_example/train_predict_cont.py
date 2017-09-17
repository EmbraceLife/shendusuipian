from keras.layers import Dense, LSTM, Activation, BatchNormalization, Dropout, SimpleRNN, Input
# from renormalization import BatchRenormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential
from keras.optimizers import SGD, RMSprop, Adam
from keras.models import load_model
from keras.callbacks import TensorBoard, ModelCheckpoint
import bcolz
import numpy as np

############## load 不同处理方式生成的 2-d 数据 ##########################################
######################################################################################
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
train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/train_dev_test_sequence.npz"

npzfiles = np.load(train_dev_test_sequence_path)
train_feature_stad_group_norm_array = npzfiles['train_sequence']
dev_feature_stad_group_norm_array = npzfiles['dev_sequence']
test_feature_stad_group_norm_array = npzfiles['test_sequence']

train_dev_target_weight_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm_dir/"
train_target_array, dev_target_array, train_weight_array, dev_weight_array, train_weight_stad_array, train_weight_mimax_array, dev_weight_stad_array, dev_weight_mimax_array = bcolz.open(train_dev_target_weight_path)

print("dataset loaded")
############################################################################################################


############## 将 2-d 数据 转化为 3-d 数据， 周期为1 ##########################################
###########################################################################################
# train_feature_group_norm_array = train_feature_group_norm_array.reshape((-1, 1, 89))
# dev_feature_group_norm_array = dev_feature_group_norm_array.reshape((-1, 1, 89))
# train_feature_stad_group_norm_array = train_feature_stad_group_norm_array.reshape((-1, 1, 89))
# dev_feature_stad_group_norm_array = dev_feature_stad_group_norm_array.reshape((-1, 1, 89))
###########################################################################################


############## load 3-d 数据， 周期为5 ######################################################
###########################################################################################
# train_dev_test_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/features_stad_group_stad/"
# train_feature_stad_group_norm_array, dev_feature_stad_group_norm_array, test_feature_stad_group_norm_array = bcolz.open(train_dev_test_sequence_path)
#
# train_dev_target_weight_sequence_path = "/Users/Natsume/Documents/AI-challenger-stocks/prepared_dataset/target_weight_norm/"
# train_target_array, dev_target_array, train_weight_array, dev_weight_array = bcolz.open(train_dev_target_weight_sequence_path)
##########################################################################################


############## 调超参数 ###########
##################################
n_neurons = 2
# n_neurons2 = 4
# n_neurons3 = 3
lr = 0.001 # 0.01 # 0.1
# rate_dropout = 0.7
##################################




############## 构建模型 ######################################################
#############################################################################
model = Sequential()

# 在输入层后增加抛弃层 dropout
# model.add(Dropout(rate=rate_dropout, input_shape=(89,)))

# 增加一个简单的RNN层
# model.add(SimpleRNN(    # simple RNN
#     # for batch_input_shape, if using tensorflow as the backend, we have to put None for the batch_size.
#     # Otherwise, model.evaluate() will get error.
#     batch_input_shape=(None, 1, 89),       # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
#     output_dim=10,
#     unroll=True,
# ))

# 在输入层后增加简单的 dense 层
# 需要对 输入层 做说明 input_shape = (88,), 如果训练数据维度是（样本数，88特征值）, 88 是因为没有加上‘group’
model.add(Dense(n_neurons, input_shape=(88,))) # 89

# 为该 dense层 选用不同的 激励函数
# model.add(Activation('relu'))
# model.add(LeakyReLU(alpha=0.3))
model.add(Activation('tanh'))

# 对输入层做 抛弃层 处理，针对训练数据 维度 （样本，5， 89）， 时间周期 5， 特征数 89
# model.add(Dropout(rate=rate_dropout, input_shape=(5, 89)))

# 在输入层后面，增加一个LSTM 层
# model.add(LSTM(2,  # 本层神经元个数
#             input_shape=(1, 89), # 处理输入层的输出个数
#             return_sequences=False, # 每个time_step（共30个time_step周期）都要产生一个输出值
#             activation='tanh', # 针对LSTM； 这些默认值都是认为普适性最强的值
#             recurrent_activation='hard_sigmoid', # 针对recurrent
#             kernel_initializer='glorot_uniform',
#             recurrent_initializer='orthogonal',
#             bias_initializer='zeros',
#             dropout=rate_dropout, # 针对LSTM层，扔掉输入层神经元个数
#             recurrent_dropout=rate_dropout # 针对recurrent 扔掉循环层神经元个数
# 				)) # 上述都只有字面理解，真正里面发生了什么，至少需要上完吴恩达RNN课程（类似功课）
# 对每一个训练值模块进行标准化

# 增加第二隐藏层，以及激励函数
# model.add(Dense(n_neurons2))
# model.add(Activation('relu'))
# model.add(LeakyReLU(alpha=0.3))
# model.add(Activation('tanh'))

# 增加第三隐藏层
# model.add(Dense(n_neurons3))
# model.add(Activation('relu'))
# model.add(LeakyReLU(alpha=0.3))
# model.add(Activation('tanh'))

# 增加输出层，和激励函数
model.add(Dense(1))
model.add(Activation('sigmoid'))
##################################################################


###################### 设置优化算法，损失函数，metric######################
#######################################################################
# learning_rate, lr, 首选 0.001 默认值
opt = Adam(lr=lr)
# metrics 这里选用 accuracy 或者 binary_accuracy
model.compile(optimizer=opt,
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

# 打印模型结构
model.summary()
#######################################################################


####################### 模型训练 以及重要数据保存 ##############################
############################################################################

# 选用不同处理的 样本权重
train_weight_flat = None
dev_weight_flat = None
# train_weight_flat = train_weight_array.flatten() # 使用weight，但不做标准化
# dev_weight_flat = dev_weight_array.flatten()
# train_weight_flat = train_weight_stad_array.flatten() # standardScaler
# dev_weight_flat = dev_weight_stad_array.flatten()
# train_weight_flat = train_weight_mimax_array.flatten() # minmaxScaler
# dev_weight_flat = dev_weight_mimax_array.flatten()

# 储存可视化文件， 最优模型参数文件 的地址
log_dir = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/logs"
model_file = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/best.h5"

# 选用不同处理方式的 特征值， 目标值
# train_set_features = train_feature_array
# train_set_features = train_feature_group_norm_array  # features 不标准化，group 标准化
train_set_features = train_feature_stad_group_norm_array  # features 标准化，group 标准化
train_set_target = train_target_array
# dev_set_features = dev_feature_array
# dev_set_features = dev_feature_group_norm_array  # features 不标准化，group 标准化
dev_set_features = dev_feature_stad_group_norm_array # # features 标准化，group 标准化
dev_set_target = dev_target_array

# 开始训练，
# history = model.fit(...) 训练完毕后，将loss 和 accuracy 保存下来
history = model.fit(train_set_features, # x: 训练特征值
            train_set_target, # y: 训练目标值
            batch_size=1024, # 一次性使用多少个样本一起计算
            epochs=10, # 训练次数
            verbose=1,  # 是否打印每次训练的损失值和准确度

            # validation_split=0.2, # 从训练数据集中取多少作为验证数据 0.2，就是取剩下的20%作为验证
            validation_data=(dev_set_features, dev_set_target, dev_weight_flat), # 或者另外使用独立的验证数据，None 是没有另外数据; 如果dev set 也有权重，添加在这里
            shuffle=True, # 是否每次训练前打乱样本顺序
            class_weight=None, # 目标值的权重设置
            sample_weight=train_weight_flat, # 样本的权重设置，必须是1-d的维度
            initial_epoch=0, # 从第几个训练开始训练
			# 是否使用其他预处理功能
            callbacks=[TensorBoard(histogram_freq=1,
                                     log_dir=log_dir), # 画图保存
                  ModelCheckpoint(filepath=model_file, save_best_only=True, mode='min')]) # 训练时保存最优秀的模型，并非最后一轮训练的模型版本

# 将最后一次训练的模型保存下来
model_last_file = "/Users/Natsume/Documents/AI-challenger-stocks/model_output/last.h5"
model.save(model_last_file)
###############################################################################################


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
