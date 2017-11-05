# What CNN needs?

Convolution layer 需要哪些函数？
  - Zero Padding
  - Convolve window
  - Convolution forward
  - Convolution backward (optional)

Pooling layer 需要哪些函数？
  - Pooling forward
  - Create mask
  - Distribute value
  - Pooling backward (optional)

每一个参与到正向传递中的函数，都必须有一个对应的反向函数参与反向传递（帮助求参数的导数）
