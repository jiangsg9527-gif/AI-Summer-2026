from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# ============================================================
# 1. 加载 Iris 数据
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target


# ============================================================
# 2. 第一次划分
#    先留下20%作为最终测试集
# ============================================================

X_temp, X_test, y_temp, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# 3. 第二次划分
#    把剩余80%再分成训练集和验证集
# ============================================================

X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=0.25,
    random_state=42,
    stratify=y_temp
)


# ============================================================
# 4. 查看三个数据集大小
# ============================================================

print("全部数据：", X.shape)

print("\n训练集：")
print(X_train.shape)

print("\n验证集：")
print(X_val.shape)

print("\n测试集：")
print(X_test.shape)

from sklearn.preprocessing import StandardScaler

# 创建标准化工具
scaler = StandardScaler()

# 训练集：学习标准化规则 + 使用规则
X_train_scaled = scaler.fit_transform(X_train)

# 验证集：只使用训练集制定好的规则
X_val_scaled = scaler.transform(X_val)

# 测试集：也只使用训练集制定好的规则
X_test_scaled = scaler.transform(X_test)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

print("\n标准化完成")
print("训练集：", X_train_scaled.shape)
print("验证集：", X_val_scaled.shape)
print("测试集：", X_test_scaled.shape)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# 使用验证集选择最佳K
# ============================================================

print("\n========== 不同K值的验证集准确率 ==========")

best_k = 0
best_accuracy = 0

for k in [1, 3, 5, 7, 9, 11, 13, 15]:

    # 创建KNN模型
    knn = KNeighborsClassifier(n_neighbors=k)

    # 只使用训练集训练模型
    knn.fit(X_train_scaled, y_train)

    # 使用验证集进行预测
    y_val_pred = knn.predict(X_val_scaled)

    # 计算验证集准确率
    val_accuracy = accuracy_score(y_val, y_val_pred)

    print(f"K = {k:2d}，验证集准确率 = {val_accuracy * 100:.2f}%")

    # 如果当前准确率更高，就记录当前K
    if val_accuracy > best_accuracy:
        best_accuracy = val_accuracy
        best_k = k


print("\n========== 最佳K ==========")
print(f"最佳K = {best_k}")
print(f"最佳验证集准确率 = {best_accuracy * 100:.2f}%")


# ============================================================
# 使用最佳K训练最终模型
# ============================================================

import numpy as np


# 1. 合并“原始”的训练集和验证集
X_train_final = np.vstack((X_train, X_val))
y_train_final = np.concatenate((y_train, y_val))

print("\n最终训练集大小：")
print(X_train_final.shape)

print("最终训练标签大小：")
print(y_train_final.shape)


# 2. 根据最终的120个训练样本重新制定标准化规则
final_scaler = StandardScaler()

X_train_final_scaled = final_scaler.fit_transform(X_train_final)

# 测试集仍然只能使用训练数据制定的规则
X_test_final_scaled = final_scaler.transform(X_test)


# 3. 创建最终KNN模型
final_knn = KNeighborsClassifier(n_neighbors=best_k)


# 4. 使用120个最终训练样本训练模型
final_knn.fit(X_train_final_scaled, y_train_final)


# 5. 对最终测试集进行预测
y_test_pred = final_knn.predict(X_test_final_scaled)


# 6. 计算最终测试准确率
test_accuracy = accuracy_score(y_test, y_test_pred)


print("\n========== 最终测试结果 ==========")
print(f"最佳K = {best_k}")
print(f"最终测试集准确率 = {test_accuracy * 100:.2f}%")