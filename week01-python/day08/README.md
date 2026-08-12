
# Day 8：机器学习分类基础

## 1. Iris 鸢尾花数据集

今天使用的是 `sklearn` 自带的 Iris 数据集：

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

查看数据集基本信息：

```python
print(iris.feature_names)
print(iris.target_names)
print(iris.data.shape)
print(iris.target.shape)
```

Iris 数据集中一共有：

```text
150 个样本
4 个特征
3 个类别
```

4 个特征分别是：

```text
sepal length    萼片长度
sepal width     萼片宽度
petal length    花瓣长度
petal width     花瓣宽度
```

3 个类别：

```text
0 → setosa
1 → versicolor
2 → virginica
```

---

# 2. X 和 y

机器学习中通常写：

```python
X = iris.data
y = iris.target
```

其中：

```text
X → 特征
y → 标签 / 目标值 / 真实类别
```

例如一朵花：

```python
[6.1, 2.8, 4.7, 1.2]
```

就是一个样本的 4 个特征。

对应：

```text
[萼片长度, 萼片宽度, 花瓣长度, 花瓣宽度]
```

如果：

```python
y = 1
```

就代表：

```text
versicolor
```

---

# 3. 划分训练集和测试集

使用：

```python
from sklearn.model_selection import train_test_split
```

代码：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

作用：

```text
原始数据
   ↓
train_test_split()
   ↓
训练集 + 测试集
```

训练集：

```text
X_train
y_train
```

用于让模型学习。

测试集：

```text
X_test
y_test
```

用于检验模型的预测效果。

本次：

```text
总样本：150

训练集：120
测试集：30
```

---

# 4. LogisticRegression 逻辑回归分类模型

导入：

```python
from sklearn.linear_model import LogisticRegression
```

创建模型：

```python
model = LogisticRegression(max_iter=200)
```

训练模型：

```python
model.fit(X_train, y_train)
```

这里的：

```python
fit()
```

可以理解成：

> 使用训练数据让模型学习特征与类别之间的关系。

---

# 5. predict()

训练完成之后：

```python
y_pred = model.predict(X_test)
```

`predict()` 的作用：

> 根据训练好的模型，对数据进行分类预测。

例如：

```python
prediction = model.predict(one_flower)
```

返回：

```text
[1]
```

说明模型最终判断：

```text
1 → versicolor
```

因此：

```text
predict()
↓
直接给最终类别
```

---

# 6. predict_proba()

使用：

```python
probabilities = model.predict_proba(one_flower)
```

它不会只告诉我们最终类别，而会给出：

> 属于每一个类别的预测概率。

例如：

```text
setosa:      0.38%
versicolor: 82.77%
virginica:  16.85%
```

因此模型最终选择：

```text
versicolor
```

因为：

```text
82.77%
```

最大。

所以一定要区分：

```text
predict()
→ 最终预测类别

predict_proba()
→ 每个类别的预测概率
```

---

# 7. 模型也会“犹豫”

第一朵新花：

```python
new_flower = [[5.0, 3.4, 1.5, 0.2]]
```

得到：

```text
setosa:      97.02%
versicolor:   2.98%
virginica:    0.00%
```

模型明显倾向：

```text
setosa
```

第二朵：

```python
new_flower = [[6.0, 2.9, 4.9, 1.5]]
```

得到：

```text
setosa:       0.19%
versicolor:  56.10%
virginica:   43.71%
```

虽然最终仍然预测：

```text
versicolor
```

但是：

```text
56.10% vs 43.71%
```

已经非常接近。

说明模型对于这个样本并不是特别确定。

所以：

> 不能永远只看最终预测类别，有时概率也非常重要。

---

# 8. 新样本必须保持相同特征数量

Iris 的模型使用：

```text
4 个特征
```

训练。

所以新的样本也必须是：

```python
[[5.0, 3.4, 1.5, 0.2]]
```

即：

```text
1 个样本 × 4 个特征
```

不能写成：

```python
[[5.0, 3.4, 1, 5, 0.2]]
```

因为这样 Python 会认为有：

```text
5 个特征
```

这里今天出现过一个很典型的错误：

```python
1,5
```

和：

```python
1.5
```

完全不同。

---

# 9. 为什么一个样本也要写成双层中括号？

正确：

```python
new_flower = [[5.0, 3.4, 1.5, 0.2]]
```

它的含义是：

```text
[
    [一个样本的4个特征]
]
```

模型通常要求二维数据：

```text
样本数 × 特征数
```

所以：

```python
X_test[0:1]
```

保留二维结构。

而：

```python
X_test[0]
```

通常得到一维数据。

这个区别以后还会经常碰到。

---

# 10. accuracy_score()

导入：

```python
from sklearn.metrics import accuracy_score
```

使用：

```python
accuracy = accuracy_score(y_test, y_pred)
```

作用：

> 计算所有测试样本中预测正确的比例。

公式：

[
Accuracy=
\frac{\text{预测正确数量}}
{\text{总样本数量}}
]

本次：

```text
30 个测试样本
30 个全部预测正确
```

因此：

```text
Accuracy = 100%
```

需要注意：

> 测试集准确率为 100%，不代表模型在所有数据上永远都是 100%。

---

# 11. 混淆矩阵 confusion_matrix

导入：

```python
from sklearn.metrics import confusion_matrix
```

使用：

```python
cm = confusion_matrix(y_test, y_pred)

print(cm)
```

本次得到：

```text
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

最重要的记忆：

```text
行 → 真实类别
列 → 预测类别
```

因此：

```text
             预测

            0   1   2
真实 0     10   0   0
真实 1      0   9   0
真实 2      0   0  11
```

对角线上的数字：

```text
10
  9
    11
```

代表：

> 预测正确的样本数量。

非对角线上的数字代表：

> 错误分类。

---

# 12. TP、TN、FP、FN

二分类中有四个非常重要的概念：

```text
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
```

记忆：

```text
真实  预测

1      1 → TP
0      0 → TN

0      1 → FP
1      0 → FN
```

也可以理解成：

```text
TP：真的正，预测也是正
TN：真的负，预测也是负

FP：本来是负，却说成正
FN：本来是正，却说成负
```

---

# 13. Precision 精确率

公式：

[
Precision=
\frac{TP}{TP+FP}
]

Precision 问：

> “模型预测为正的那些样本里面，有多少真的属于正类？”

所以：

````text
真的属于正类？”

所以：

```text
Precision 更关心 FP
````

记忆：

> **Precision 怕报错。**

或者：

> 我说你是正类的时候，最好别说错。

---

# 14. Recall 召回率

公式：

[
Recall=
\frac{TP}{TP+FN}
]

Recall 问：

> “所有真正属于正类的样本中，我成功找出了多少？”

所以：

```text
Recall 更关心 FN
```

记忆：

> **Recall 怕漏掉。**

或者：

> 你明明是正类，我最好别把你漏掉。

因此今天最重要的一组记忆：

```text
Precision → FP → 怕报错
Recall    → FN → 怕漏掉
```

---

# 15. F1-score

公式：

[
F1=
\frac{2\times Precision\times Recall}
{Precision+Recall}
]

F1 不是普通平均值。

普通平均：

[
\frac{Precision+Recall}{2}
]

F1 使用的是：

> **调和平均。**

它的特点：

> Precision 和 Recall 中如果有一个特别低，F1 会被明显拉低。

例如：

```text
Precision = 0.90
Recall    = 0.50
```

普通平均：

```text
0.70
```

而 F1：

```text
≈ 0.64
```

所以 F1 的思想是：

> Precision 和 Recall 两方面都应该比较好，不能严重偏科。

今天自己的理解可以记成：

```text
F1-score 更在意两者中较低的一项。
```

这句话作为直觉理解完全可以。

---

# 16. 今天实际算过的例子

人为设置：

```python
y_true = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

y_pred = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
```

得到：

```text
TP = 3
FN = 2
FP = 1
TN = 4
```

因此：

[
Precision=
\frac{3}{3+1}
=0.75
]

[
Recall=
\frac{3}{3+2}
=0.60
]

[
F1\approx0.67
]

---

# 17. 今天容易写错的地方

### 大小写不同

Python 区分大小写：

```python
X
```

和：

```python
x
```

不是同一个变量。

---

### target_names 后面有 s

正确：

```python
iris.target_names
```

错误：

```python
iris.target_name
```

---

### 小数点不能写成逗号

正确：

```python
1.5
```

错误：

```python
1,5
```

后者会被认为是：

```text
1 和 5 两个数字
```

---

### 新样本需要双层中括号

正确：

```python
[[5.0, 3.4, 1.5, 0.2]]
```

不要写：

```python
[5.0, 3.4, 1.5, 0.2]
```

尤其是在直接传给 sklearn 模型时。

---

# 18. 今天完整的机器学习流程

今天已经完成了一套完整的监督学习分类基本流程：

```text
加载数据
    ↓
X = 特征
y = 标签
    ↓
train_test_split()
划分训练集和测试集
    ↓
创建模型
LogisticRegression()
    ↓
model.fit()
训练模型
    ↓
model.predict()
预测类别
    ↓
model.predict_proba()
预测概率
    ↓
accuracy_score()
总体准确率
    ↓
confusion_matrix()
分析具体分类错误
    ↓
Precision
Recall
F1-score
进一步评价分类模型
```

---

# 19. 今天需要真正记住的函数

```python
load_iris()

train_test_split()

LogisticRegression()

model.fit()

model.predict()

model.predict_proba()

accuracy_score()

confusion_matrix()

precision_score()

recall_score()

f1_score()
```

不用现在死记参数。

现阶段最重要的是：

> 看到函数名字，知道它大概是干什么的。

---

# 20. 今日一句话总结

今天从原来的简单二分类进一步进入了：

> **真实多分类数据集 → 模型训练 → 新数据预测 → 概率判断 → 模型评价。**

现在已经不只是会写：

```python
fit()
predict()
```

而是开始知道：

> **模型预测得“对不对”、错在哪里、有没有把正类漏掉、有没有误报，以及 Precision 和 Recall 是否平衡。**

下一次接着学习：

```text
classification_report()
↓
StandardScaler 数据标准化
↓
为什么不同特征尺度会影响模型
↓
进一步理解 Logistic Regression
```
