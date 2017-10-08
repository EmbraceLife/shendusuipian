import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
from logger import Logger


# MNIST Dataset object
dataset = dsets.MNIST(root='/Users/Natsume/Desktop/data/MNIST',
                      train=True,
                      transform=transforms.ToTensor(),
                      download=False)

# Data Loader (Input Pipeline)
data_loader = torch.utils.data.DataLoader(dataset=dataset,
                                          batch_size=100,
                                          shuffle=True)

def to_np(x): # from tensor to numpy
    return x.data.cpu().numpy()

def to_var(x): # from tensor to Variable
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x)

# Neural Network Model (1 hidden layer)
class Net(nn.Module):
    def __init__(self, input_size=784, hidden_size=500, num_classes=10):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

net = Net() # 10 classes classification
if torch.cuda.is_available():
    net.cuda()

# Set the logger
logger = Logger('./logs') # dive in later

# Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.00001)

data_iter = iter(data_loader) # from loader to iterator
iter_per_epoch = len(data_loader)
total_step = 50000 # num_total_batches to be used

# Start training
for step in range(total_step):

    # shuffle: every epoch, reset the data_iter
    if (step+1) % iter_per_epoch == 0:
        data_iter = iter(data_loader)

    # Fetch the images and labels and convert them to variables
    images, labels = next(data_iter)
    images, labels = to_var(images.view(images.size(0), -1)), to_var(labels) # tensor.view == np.reshape

    # Forward, backward and optimize
    optimizer.zero_grad()  # zero the gradient buffer
    outputs = net(images)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()

    # Compute accuracy
    _, argmax = torch.max(outputs, 1) # squeeze, max, index
    accuracy = (labels == argmax.squeeze()).float().mean()

    if (step+1) % 100 == 0: # 每100batches, 打印统计
        print ('Step [%d/%d], Loss: %.4f, Acc: %.2f'
               %(step+1, total_step, loss.data[0], accuracy.data[0]))

        #============ TensorBoard logging ============#
        # (1) Log the scalar values
        info = {
            'loss': loss.data[0], # scalar
            'accuracy': accuracy.data[0] # scalar
        }

        for tag, value in info.items():
            logger.scalar_summary(tag, value, step+1)

        # (2) Log values and gradients of the parameters (histogram)
        for tag, value in net.named_parameters():
            tag = tag.replace('.', '/')
            logger.histo_summary(tag, to_np(value), step+1) # from Parameter to np.array
            logger.histo_summary(tag+'/grad', to_np(value.grad), step+1)# from Variable to np.array

        # (3) Log the images
        info = { # reshape (样本，h,w)
            'images': to_np(images.view(-1, 28, 28)[:10])
        }

        for tag, images in info.items():
            logger.image_summary(tag, images, step+1)
