# Day 9 - StandardScaler、KNN 与交叉验证

## 1. StandardScaler 数据标准化

StandardScaler 用于统一不同特征的尺度。

标准化后的数据通常满足：

- 平均值接近 0
- 标准差接近 1

核心思想：

- 训练集：fit + transform
- 验证集：只 transform
- 测试集：只 transform

代码：

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)
```

其中：

- `fit`：学习训练集每个特征的平均值和标准差
- `transform`：使用已经学习到的规则进行转换
- `fit_transform`：`fit + transform`

测试集不能重新 `fit`，否则可能造成 Data Leakage（数据泄漏）。

---

## 2. KNN

KNN 全称：**K-Nearest Neighbors**，中文为 **K 近邻算法**。

核心思想：对于一个新的样本，先计算它与训练样本之间的距离，找到最近的 K 个邻居，再查看这些邻居的类别，通过投票确定最终类别。

例如：

```text
K = 3

最近三个邻居：
versicolor
versicolor
virginica

最终预测：
versicolor
```

---

## 3. K 的影响

K 是 KNN 的超参数。

### K 太小

- 更关注局部数据
- 对噪声比较敏感
- 过拟合风险较高

### K 太大

- 考虑过多远处样本
- 局部规律可能被冲淡
- 容易欠拟合

因此 K 不是越大越好，也不是越小越好。

---

## 4. 参数与超参数

### Parameter

模型通过训练数据自己学习得到。例如 Logistic Regression 的系数和截距。

### Hyperparameter

训练前人为设置，或者通过验证过程选择。例如：

```python
KNeighborsClassifier(n_neighbors=3)
```

这里 `K = 3` 就是超参数。

---

## 5. Train / Validation / Test

- **Train**：用于训练模型，让模型学习参数。
- **Validation**：用于选择超参数，例如 KNN 中的 K。
- **Test**：用于最后独立评价模型的泛化能力。

基本流程：

```text
Train
↓
训练模型

Validation
↓
选择超参数

Test
↓
最终考试
```

测试集不能用来反复选择模型参数。

---

## 6. 交叉验证 Cross Validation

只使用一次固定 Validation，结果可能受到数据划分的影响，因此可以使用 **K-Fold Cross Validation**。

例如 5-Fold Cross Validation：把训练数据分为 5 份，每次 4 份训练、1 份验证，一共进行 5 次，最后计算 5 次验证准确率的平均值。

注意：KNN 中的 K 和 K-Fold 中的 K 不是同一个概念。

```text
KNN：K = 3
5-Fold：K = 5
```

分别表示：

- KNN 的 K：最近邻数量
- K-Fold 的 K：把数据分成几份

---

## 7. Pipeline

Pipeline 可以把数据预处理和模型组合起来。

```python
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=3)
)
```

流程：

```text
原始数据
↓
StandardScaler
↓
KNN
↓
预测
```

使用 Pipeline 可以减少标准化过程中发生数据泄漏的风险。

在交叉验证中，Pipeline 会保证：

```text
当前折训练数据
→ fit StandardScaler

当前折验证数据
→ 只 transform
```

---

## 8. 固定验证集选择 K

第一次使用：

```text
Train：90
Validation：30
Test：30
```

不同 K 的验证集准确率：

```text
K =  1 → 90.00%
K =  3 → 93.33%
K =  5 → 93.33%
K =  7 → 96.67%
K =  9 → 96.67%
K = 11 → 96.67%
K = 13 → 96.67%
K = 15 → 96.67%
```

程序选出的：

```text
最佳 K = 7
最佳验证集准确率 = 96.67%
```

其中 K=7、9、11、13、15 的准确率相同。程序保留 K=7，是因为代码使用：

```python
if val_accuracy > best_accuracy:
```

只有严格更高时才更新，因此会保留第一个达到最高准确率的 K。

最终测试结果：

```text
最佳 K = 7
最终测试集准确率 = 96.67%
```

---

## 9. 5 折交叉验证

随后使用 120 个训练数据进行 5 折交叉验证。

固定：

```text
KNN：K = 7
```

得到：

```text
第1折准确率：91.67%
第2折准确率：95.83%
第3折准确率：91.67%
第4折准确率：95.83%
第5折准确率：91.67%

平均准确率：93.33%
```

说明同一个模型面对不同验证数据时，准确率可能不同。因此相比只看一次验证结果，交叉验证更加稳定。

---

## 10. 使用 5 折交叉验证选择 K

不同 K 的 5 折平均准确率：

```text
K =  1 → 94.17%
K =  3 → 96.67%
K =  5 → 95.83%
K =  7 → 93.33%
K =  9 → 95.83%
K = 11 → 95.00%
K = 13 → 95.00%
K = 15 → 92.50%
```

因此：

```text
最佳 K = 3
最高5折平均准确率 = 96.67%
```

可以看到：

```text
固定验证集选出的最佳K = 7
5折交叉验证选出的最佳K = 3
```

原因是固定验证集只使用一批验证数据，而 5 折交叉验证让不同数据轮流作为验证数据，再比较平均成绩，因此结果通常更稳定。

---

## 11. 最终 KNN 模型结果

使用交叉验证选出的：

```text
最佳 K = 3
```

再使用全部 120 个训练样本训练最终模型。

最终独立测试结果：

```text
交叉验证选出的最佳K = 3
5折平均验证准确率 = 96.67%
最终测试集准确率 = 93.33%
```

最终测试集有 30 个样本：

```text
28 / 30 = 93.33%
```

说明最终模型预测正确 28 个，预测错误 2 个。

---

## 12. 为什么验证准确率和测试准确率不同？

交叉验证准确率 `96.67%` 是对训练数据进行多次轮流验证后得到的平均结果。

最终测试准确率 `93.33%` 来自之前没有参与选 K 的独立测试数据。

两者面对的数据不同，所以不要求完全一致。

如果别人问“最终模型在独立测试集上的准确率是多少？”，应该回答：

```text
93.33%
```

因为测试集成绩才是最终独立评价结果。

---

## 13. 今天最重要的完整机器学习流程

```text
Iris：150个样本
        ↓
Train：120      Test：30
   ↓                ↓
5折交叉验证       暂时不用
   ↓
比较不同K
   ↓
最佳 K = 3
   ↓
使用全部120个训练
   ↓
最终测试30个
   ↓
Accuracy = 93.33%
```

更完整地写：

```text
原始数据
↓
划分 Train / Test
↓
使用 Train 做交叉验证
↓
Pipeline 中进行 StandardScaler
↓
不同 K 分别进行 5 折交叉验证
↓
比较平均准确率
↓
选择最佳超参数 K
↓
使用全部 Train 训练最终模型
↓
最后使用 Test
↓
评价最终模型
```

---

## 14. 今天需要记住的关键词

```text
fit
= 学习

transform
= 使用已经学习的转换规则

fit_transform
= 学规则 + 使用规则

predict
= 预测

StandardScaler
= 标准化

KNN
= 找最近的K个邻居投票

K太小
= 模型更敏感，过拟合风险较高

K太大
= 模型过于粗糙，容易欠拟合

Train
= 训练模型

Validation
= 选择超参数

Test
= 最终独立评价

Hyperparameter
= 训练前人为设置或通过验证选择的参数

Cross Validation
= 多次轮流验证再取平均

Pipeline
= 把数据预处理和模型组合起来
```

---

## 15. Day 9 最终结果

```text
最佳 KNN 超参数：
K = 3

5折平均验证准确率：
96.67%

最终独立测试准确率：
93.33%
```
