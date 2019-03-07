# fastai part1 2019 中文版
[details="什么是中文版笔记"]
### 是什么

* 汇总fastai学员们的课程学习分享，进行知识点分解，梳理，并转为中文    
* 如果条件允许，未来会将笔记知识点做Notebooks, 甚至是短小精悍的中文视频


### 目标

* 力争覆盖课程全部知识点
* 保持课程知识点更新
* 根据需要进行知识点拓展

### 效果
* 知识点全面，查阅快捷方便，更新及时

### 问答
* 好提问，必回答（请在[issues](https://github.com/EmbraceLife/shendusuipian/issues/new)中提问）     
* 好提问的标准，见[how to ask for help 中文版](https://forums.fast.ai/t/fast-ai-v3-2019/39325/8?u=daniel)     
* 目前有信心必答的问题，仅限定视频理解，因此只需做到标准中的前两条即可     
* 只要是fast.ai学习问题，欢迎积极提问，共同探讨     

### 共建
* 欢迎大家在[论坛回复中](https://forums.fast.ai/t/fast-ai-v3-2019/39325)或[github issues 里](https://github.com/EmbraceLife/shendusuipian/issues/new)协助翻译，提问，回答
* 回复与issues能直接看出直接贡献者，无需为credit归属担忧
* 我会将你的内容贡献的链接植入此页面和合适位置，大家只用专心分享即可
[/details]

[details="每日必看"]
## 每日观光地
fast.ai v3 2019 [课程官网](https://course.fast.ai/) ✅     
fastai [文档官网](https://docs.fast.ai/) ✅     
fast.ai [官方论坛](https://forums.fast.ai/) ✅     
fast.ai 论坛官方[课程更新](https://forums.fast.ai/t/faq-resources-and-official-course-updates/27934) ✅    
Kaggle [官网](https://www.kaggle.com/)     
[/details]




[details="fast.ai v3 2019课程笔记源泉"]

  - @PoonamV [笔记wiki](https://forums.fast.ai/t/deep-learning-lesson-1-notes/27748)全面详尽+大家共建（英文）
  - @hiromi [github笔记](https://github.com/hiromis/notes/blob/master/Lesson1.md) 精美细致+英文transcript
  - @Daniel [bear笔记PDF](https://github.com/EmbraceLife/shendusuipian/blob/master/%E6%B7%B1%E5%BA%A6%E7%A2%8E%E7%89%87fastai%202019%20Notes.pdf) 对课程视频做视频知识点切分+要点总结（英文）
  - [fastai论坛](https://forums.fast.ai/c/part1-v3)上大家的无私分享宝贵资源   
  - 现在看到的是尝试对上述所有笔记的融合梳理（[github版本](https://github.com/EmbraceLife/shendusuipian/blob/master/fastai_v3_2019_notes_cn.md)比[forum版](https://forums.fast.ai/t/fast-ai-v3-2019/39325)更新稍快一点)
[/details]

初来匝道，快速上手，[请跳转](#beginner)

## Jeremy的课程建议（忠告）:heartpulse:
[details="引言"] 
感谢 @MadeUpMasters 分享的[post](https://forums.fast.ai/t/things-jeremy-says-to-do/36682)这里是它的中文镜像版（原文直译）

在开始学习fast.ai前，我尝试学习已毕业学员发表在网上的经验分享，尤其是他们后悔的事情。

最常见的忠告：“真的要听Jeremy的话，将时间用在他建议的地方。”
最多的懊悔：“我真应该听Jeremy的话，不要将大把时间浪费在一次性搞懂理论理解上。”

在这里我记录了每节课Jeremy给出的建议，我会照做，也希望大家跟我一起做。
[/details]

[details="第一课的建议"]

1. 不要尝试停下来理解所有的知识点 
2. 不要浪费时间：请学习JN的快捷键，一天学4-5个 
3. 请跑代码，“真的”去跑代码。不要去深入学习理论。去玩转代码，看看它们“吃进什么吐出什么”  
4. 选择一个项目，认真做好，做到超棒！
5. 跑这个Nb(lesson1-pets.ipynb)，然后用你自己的数据集跑跑，一定要做！
6. 如果你有很多类别要区分，不要选择`confusion matrix`，要用

```
interp.most_confused(min_val=n)
```
[/details]

[details="第二课的建议"]

1. 如果论坛博文太庞杂，点击博文下方的“summarize this topic总结此主题”
2. 请跟着官方的安装说明设置你的GPU，步骤简单快捷。
3. 如果感觉论坛里大家都太厉害，有太多新东西，而且感觉很难，真的没关系！选择一个点下手，比如跑几行代码，学一个概念如regular expression, 或者创建一个分类器，什么都行，关键是忘记烦恼，行动起来。建议出处视频节点 [Lesson 2: It’s okay to feel intimidated ](https://youtu.be/ccMHJeQU4Qw?t=600)
4. 如果卡壳了，不要停下来深挖，继续前行！（看下图） 视频节点: [Lesson 2: If you’re stuck, keep going ](https://youtu.be/ccMHJeQU4Qw?t=867)
5. 如果你不确定图中的哪个学习率更好，每个都试试看。
6. 当你将模型做成网页APP，你会选择用CPU做预测，除非是巨量规模的服务请求才会用到GPU。视频节点: [Lesson 2: Putting Model into Production ](https://youtu.be/ccMHJeQU4Qw?t=2308)
7. 多数公司浪费大量时间在收集更多数据上。正确做法是，用一小撮数据跑跑看，然后在看问题是否是数据不够。
8. 如果你认为自己“天生不擅长数学”， 请看看Rachel的TED演讲: [There’s no such thing as “not a math person” ](https://youtu.be/q6DGVGJ1WP4). My own input: only 6 minutes, everyone should watch it!

[![keepgoing|690x422](https://forums.fast.ai/uploads/default/optimized/3X/d/e/de73a146088bb62668b7e2d0215b398d9452177e_2_10x10.png)
keepgoing.png876×537 125 KB
](https://forums.fast.ai/uploads/default/original/3X/d/e/de73a146088bb62668b7e2d0215b398d9452177e.png)
[/details]


[details="第三课的建议"]

1. 在你使用数据集时，请务必给予数据创建者荣誉和感谢
2. 在接下来的一周里，看看你能不能找到你想解决的多标注分类问题，图片回归问题，或图片区域隔离问题等等，试试看你能否拿出解决方案。 视频节点: [Fast.ai Lesson 3 Homework ](https://youtu.be/MpZxV6DVsmM?t=7409)
3. 记住要使用pretrained模型训练时所用的均值与方差。 视频节点: [Lesson 3: Normalized data and ImageNet ](https://youtu.be/MpZxV6DVsmM?t=6413)
4. 对问题 “有理由阻止我们尝试 64x64 to 128x128 to 256x256等尺寸图片训练微调模型吗?”的回答: “是的，非常值得一试！效果不错，试试吧!” 视频节点: [Lesson 3: 64x64 vs 128x128 vs 256x256 ](https://youtu.be/MpZxV6DVsmM?t=4252)
[/details]


[details="第四课的建议"]

1. 如果做的是NLP，没有理由不用验证集参与训练。 [视频节点Lesson 4: A little NLP trick ](https://youtu.be/9YK6AnqpuEA?t=1256)
2. 在回答提问：”在怎样10%的情况下你不会使用神经网络”时，回应：“你可以都尝试，random forest和神经网络. [视频节点Lesson 4: How to know when to use neural nets ](https://youtu.be/9YK6AnqpuEA?t=2440)
3. 习惯使用这些词汇 (参数parameters, 层layers, 激活activations…etc) 并尝试准确使用。 [视频节点Lesson 4: Important vocabulary for talking about ML ](https://youtu.be/9YK6AnqpuEA?t=6015)
[/details]

[details="第五课的建议"]

1. 如果你心里有疑问：“我是否应该试试？”， 回答是：试试看吧，这是你成为优秀实践者的必修课。 [视频节点Lesson 5: Should I try *blah* ? ](https://youtu.be/CJKnDu2dxOE?t=2800)

[/details]

[details="第六课的建议"]

1. “一个潜力巨大的研究方向是各个领域数据增强研究。几乎没有关注这个方向，而我认为这是蕴藏着巨大的机会，可以帮助节省5-10倍的数据需求。” [视频节点Lesson 6: Data augmentation on inputs that aren’t images ](https://youtu.be/hkBa9pU-H48?t=3852)
2. 如果你会花时间跑整个Nb，包括 the convolution kernel 和 the heatmap部分, 尝试实验这些代码看看他们的反应。最重要的是记住: shape也就是这里说的rank或tensor维度。尝试思考：“为什么？” 回头看看模型summary, 各个层的设置，作出的各种图，想象以下背后的机制。[视频节点Lesson 6: Go through the convolution kernel and heatmap notebook ](https://youtu.be/hkBa9pU-H48?t=6486)
[/details]

[details="第七课的建议"]

1. 这节课的内容很多，目的是让你们忙起来，直到进入part2的课程。

下面内容源于这节课视频中的一段精彩演讲，强烈建议再看一遍 [Lesson 7: What to do once you’ve completed Part 1 ](https://youtu.be/9spwoDYwW_I?t=7142)

2. 回头再去看看视频，这一遍肯定有些内容理解和感悟是之前没有的。
3. 写代码并分享到github中。有多好不重要，重要的是写下来和分享出来。这样才能获得反馈帮助你进步。
4. 现在可以开始读课程中介绍过的论文了。论文里所有关于derivations/theorems/lemmas（数学公式部分）都可以忽略，因为它们无法帮助增加对深度学习的实践性理解。认真阅读关于为什么以及怎样定义和解决问题的。写下总结来帮助那些与6个月前的你的状态水平相似的人。
5. 可能最重要的是和大家一起学，这样效果往往更好。组建一个读书会，学习小组，定期聚会，动手做些项目。不需要是什么特别棒的东西，只要是能让世界更美好一点，甚至是让你的2岁大孩子开心的事情。完成一件事情，然后在进一步完善它。或者是参与到fast.ai中来帮助开发代码和完善文档。如何参与件 [Dev Projects Index ](https://forums.fast.ai/t/dev-projects-index/29849) on forums.
6. 提问：“在part 2 开始前，你建议我们做些什么呢”，回答： "就是代码，不停写代码，看看你的输入值，输出值，尝试输出一个你的mini-batch。我们覆盖的内容非常多，如果你能做到”不作弊“状态下，重建所有的notebook，你将是极少数顶级的实践者。 [视频节点：Lesson 7: What to do/learn/practice between now and Part 2 ](https://youtu.be/9spwoDYwW_I?t=7777) 

[/details]
---

## 课程Notebook 汇总    
[details="英文版Nb"]
* [官方github最新版](https://github.com/fastai/course-v3/tree/master/nbs/dl1) ✅      
* [Kaggle 版本](https://forums.fast.ai/t/platform-kaggle-kernels/32569)     
* [Colab 版本](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true) click 'Github' and search 'fastai v3'     
[/details]
[details="中文版Nb"]
Kaggle Nb [中文版](https://forums.fast.ai/t/fast-ai-v3-2019-notebook-kaggle-kernel/39722) 学习借鉴了 @init_27 @wdhorton 的 [kernel](https://forums.fast.ai/t/platform-kaggle-kernels/32569)并尽可能保持与[课程github版本Nb](https://github.com/fastai/course-v3/tree/master/nbs/dl1)同步更新。
**新增挑战**：“听写” Notebook :heartpulse:
[第零课：如何使用Jupyter Notebook](https://www.kaggle.com/danielliao/jupypter-notebook)
[第一课：你的宠物](https://www.kaggle.com/danielliao/fast-ai-v3)
[第二课：创建你的数据集和分类器](https://www.kaggle.com/danielliao/fastai-v3-lesson-2-download-cn)
[第二课：梯度下降SGD](https://www.kaggle.com/danielliao/fast-ai-v3-lesson-2-sgd)
[第三课：Camvid tiramisu 简化版](https://www.kaggle.com/danielliao/fast-ai-v3-lesson-3-camvid-tiramisu)
[第三课：Camvid 图片隔离](https://www.kaggle.com/danielliao/fastai-camvid)
[第三课：图片回归BIWI数据集](https://www.kaggle.com/danielliao/fast-ai-v3-lesson-3-head-pose)
[/details]


---

<a name="lesson1toc"></a>
## 课程笔记汇总
[details="第一课 你的宠物"]
[details="官方资源"]
[第一课  官方视频](https://course.fast.ai/videos/?lesson=1)✅    [YouTube 视频 ](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSIJb-Qd3pw0cqCbkGeS0xn) [B站视频](https://www.bilibili.com/video/av41718196/?spm_id_from=333.788.videocard.0)     
[第一课 官方资源和动态更新  ✅ ](https://forums.fast.ai/t/lesson-1-official-resources-and-updates/27936) [Part 1 (2019)](/c/part1-v3)      
[第一课 问答探讨 汇集地 ✅](https://forums.fast.ai/t/lesson-1-in-class-discussion/27332) [Part 1 (2019)](/c/part1-v3)     
[/details]

[details="笔记工地"]
### 第一课笔记工地（建设中）
@hiromi [第一课笔记汇总](https://github.com/EmbraceLife/shendusuipian/issues/70)，点击`TOC 中英文目录`，快速导航到具体知识点细节
@PoonamV 进入 [第一课笔记汇总](https://forums.fast.ai/t/deep-learning-lesson-1-notes/27748)，点击`TOC EN` 或 `TOC 中文目录`，快速导航到具体知识点细节
@Daniel [第一课笔记汇总](https://github.com/EmbraceLife/shendusuipian/issues/63)，点击`TOC 中英文目录`，快速导航到具体知识点细节
[/details]
[details="@Daniel 笔记TOC"]


[details="如何启动你的第一个GPU"]
1. Lesson 0 How to get GPU running [gpu](https://forums.fast.ai/t/fast-ai-v3-2019/39325/7?u=daniel)    
如何启动你的第一个GPU
[/details]

[details="你需要做些什么准备"]
3. [What else do you need to get started?](https://github.com/EmbraceLife/shendusuipian/issues/64)    
你需要做些什么准备？
[/details]

[details="如何最大化利用课程视频与notebook"]
5. [How to make the most out of these lesson videos and notebooks?](https://github.com/EmbraceLife/shendusuipian/issues/65)    
如何最大化利用课程视频与notebook?
[/details]

[details="你可以期望的学习成就高度与关键学习资源"]
7. what will you become and key resources? [#66](https://github.com/EmbraceLife/shendusuipian/issues/66)    
你可以期望的学习成就高度与关键学习资源
[/details]

[details="为什么我们要跟着Jeremy Howard学习"]
9. why should we learn from Jeremy Howard?  [#67](https://github.com/EmbraceLife/shendusuipian/issues/67)           
为什么我们要跟着Jeremy Howard学习？
[/details]


[details="fast.ai让人人都成为深度学习高手的策略方针"]
11. How to make DL accessible to everyone to do useful things? #68      
fast.ai让人人都成为深度学习高手的策略方针
[/details]

13. How much to invest and What I get out? #69      
需要投入多少精力，会有怎样的收获？
15. Prerequisites and False assumptions and claims on DL #71
学习深度学习的必要基础是什么，以及常见的误解与成见
17. What will you be able to do at the end of lesson 1 #72
完成第一课后你将能做些什么
19. What is fastai learning philosophy #73 
fast.ai的教学哲学是什么
21. How to use Jupyter notebook as a pro? #74
如何像专业人士一样使用jupyter notebook
23. What are Jupyter magics? #75 
什么是Jupyter magics
25. What are fastai lib and how to use it? #76
什么是fastai库以及如何使用
27. Academic vs Kaggle Datasets, CatsDogs vs Pets dataset #77 
学术和Kaggle数据，CatsDogs 与 Pets数据的异同
29. How to download dataset with fastai #78
如何下载数据包
31. How to access image folders and check filenames inside #79
如何进入图片文件夹以及查看里面的文件
33. How to get the labels of dataset? #80 
如何从文件名中获取标注
35. Why and how to pick the image size for DataBunch? #81
为什么以及如何选择图片大小规格
37. What is a DataBunch #82 
什么是DataBunch
39. What does normalize do to `DataBunch`? #83
如何normalize DataBunch
41. What to do if `size` is not 224? #84 
如果图片大小不是224会怎样
43. What does it mean to normalize images #85 
normalize 图片意味着什么
45. Why 224 not 256 as power of 2 to be image size #86
为什么图片尺寸是224而不是256
47. How to check the real images and labels #87
如何查看图片和标注
49. How to build a CNN learner/model? #88
如何构建一个CNN模型
51. Why use a pretrained model (framework and parameters) for your CNN? in other words, What is transfer learning? #89
为什么要用训练好的模型的框架与参数
53. what is overfitting? why wouldn’t the model cheating? #90 
什么是过拟合？为什么我们的模型很难过拟合？
55. How to train the model with the best technique? #91
如何用最优的技术来训练模型？
57. How to find out how good is your model? #92
如何了解模型的好坏？
59. How to get the most out of this course? #93
如何放大课程效果？
61. The popularity of fastai library and replacing Keras #94 
fastai的业界口碑以及与kera的对比
63. What students achieved with fastai and this course? #95
学员能够用fast.ai所学完成的项目
65. Why use Resnet rather than Inception? #96
为什么选择ResNet 而非Inception作为模型框架和已训练的参数
67. How to save a trained model? #97 
如何保存训练好的模型
69. how to plot top losses examples/images? #98
如何画出损失值最高的数据/图？
71. How to find out the most confused images of our model? #99
如何找出模型混淆度最高的图片？
73. How to improve our model? finetuning #100
如何用微调改进模型？
75. what is CNN actually learning and why previous full model training didn’t work #101 
CNN模型在学习些什么？以及为什么直接用全模型学习效果不佳？
77. How to train the whole model in the right way? #102
训练全模型的正确方式是什么？
79. How to improve model with more layers? #103  
如何用更大的模型来改进效果
81. Different ways to put your data into DataBunch #104
生成DataBunch的不同方式有哪些
83. How to make the most out of documents? #105 
如何最大化利用fastai文档
85. QA on fastai with multi-GPU, 3D data #106 
关于fastai与多GPU和3D数据的问题
87. An interesting and inspiring project #107 
一些有趣的项目


[/details]
[/details]
---
<a name="beginner"></a>
## 接受笔记知识点英翻中请求 

[details="初来匝道之必备“]
初次了解深度学习和fast.ai的小伙伴，想快速上手，推荐先看以下知识点


在上述三个笔记源泉（中文列表）中，如果有你迫切希望转化成中文的知识点，请 @Daniel 申请优先翻译成中文

* 如何开启你的第一个GPU [笔记](https://forums.fast.ai/t/fast-ai-v3-2019/39325/7?u=daniel)
     * 小伙伴们使用经验 [1](https://forums.fast.ai/t/fast-ai-v3-2019/39325/38?u=daniel)
* 如何更新课程notebook与fastai库 [笔记](https://forums.fast.ai/t/fast-ai-v3-2019/39325/9?u=daniel)     
* 为什么用Jupyter Notebook [笔记](https://forums.fast.ai/t/fast-ai-v3-2019/39325/10?u=daniel)     
* 如何更新notebook与fastai? [笔记](https://github.com/EmbraceLife/shendusuipian/issues/60)
* 如何使用Jupyter Notebook? 
  * (EN)原课程指南[notebook](https://www.kaggle.com/danielliao/fastai-guide-to-jupyter-notebook) 
  * (中)应用技巧更新汇总[notebook](https://www.kaggle.com/danielliao/jupypter-notebook) 
* `/([^/]+)_\d+.jpg$`是如何提取标注label的？ [笔记](https://github.com/EmbraceLife/shendusuipian/issues/62) [notebook](https://www.kaggle.com/danielliao/regexpr-label)

[/details]
