from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris=load_iris()

X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 创建标准化工具
scaler=StandardScaler()

# 用训练集计算平均值和标准差，并标准化训练集
X_train_scaled=scaler.fit_transform(X_train)

# 使用训练集得到的规则标准化测试集
X_test_scaled=scaler.transform(X_test)

print("标准化前第一条训练数据：")
print(X_train[0])

print("\n标准化后第一条训练数据：")
print(X_train_scaled[0])

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 模型1：使用原始数据
model_original = LogisticRegression(max_iter=200)

model_original.fit(X_train, y_train)

y_pred_original = model_original.predict(X_test)

accuracy_original = accuracy_score(y_test, y_pred_original)

print("\n原始数据准确率：")
print(f"{accuracy_original * 100:.2f}%")


# 模型2：使用标准化后的数据
model_scaled = LogisticRegression(max_iter=200)

model_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = model_scaled.predict(X_test_scaled)

accuracy_scaled = accuracy_score(y_test, y_pred_scaled)

print("\n标准化后准确率：")
print(f"{accuracy_scaled * 100:.2f}%")

print("\n===== 准确率对比 =====")

print(f"标准化前：{accuracy_original * 100:.2f}%")
print(f"标准化后：{accuracy_scaled * 100:.2f}%")



from sklearn.neighbors import KNeighborsClassifier

# 创建KNN模型
# n_neighbors=3表示寻找最近的3个邻居
knn_model=KNeighborsClassifier(n_neighbors=3)

# 使用标准化后的训练集训练KNN模型
knn_model.fit(X_train_scaled,y_train)

# 使用标准化后的测试集进行预测
knn_pred=knn_model.predict(X_test_scaled)

# 计算准确率
knn_accuracy=accuracy_score(y_test,knn_pred)

print("\n=============KNN分类结果===========")
print(f"KNN准确率：{knn_accuracy*100:.2f}%")


# ============================================================
# 查看KNN是如何预测第一条测试数据的
# ============================================================

# 取测试集中的第一朵花
test_flower = X_test_scaled[0:1]

# 找出距离它最近的3个邻居
distances, indices = knn_model.kneighbors(test_flower)

print("\n========= 第一朵测试花 =========")

print("原始数据：")
print(X_test[0])

print("\n标准化后的数据：")
print(X_test_scaled[0])

print("\n最近3个邻居的距离：")
print(distances[0])

print("\n最近3个邻居在训练集中的编号：")
print(indices[0])

print("\n最近3个邻居的真实类别编号：")
print(y_train[indices[0]])

print("\n最近3个邻居的花的种类：")
print(iris.target_names[y_train[indices[0]]])

print("\nKNN最终预测：")
print(iris.target_names[knn_model.predict(test_flower)[0]])

print("\n真实答案：")
print(iris.target_names[y_test[0]])


# ============================================================
# 比较不同K值下：训练集准确率和测试集准确率
# ============================================================

print("\n========== 不同K值的训练/测试准确率 ==========")

for k in [1, 3, 5, 7, 15, 30, 50, 100]:

    # 创建KNN模型
    model = KNeighborsClassifier(n_neighbors=k)

    # 使用标准化后的训练集训练
    model.fit(X_train_scaled, y_train)

    # 分别预测训练集和测试集
    train_pred = model.predict(X_train_scaled)
    test_pred = model.predict(X_test_scaled)

    # 分别计算准确率
    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    print(
        f"K = {k:3d}，"
        f"训练集准确率 = {train_acc * 100:6.2f}%，"
        f"测试集准确率 = {test_acc * 100:6.2f}%"
    )

import numpy as np

# 合并原来的训练集和验证集
X_train_final = np.vstack((X_train, X_val))
y_train_final = np.concatenate((y_train, y_val))

print("\n最终训练集大小：")
print(X_train_final.shape)

print("最终训练标签大小：")
print(y_train_final.shape)


# 创建最终KNN模型
final_knn = KNeighborsClassifier(n_neighbors=best_k)

# 使用最终训练数据训练
final_knn.fit(X_train_final_scaled, y_train_final)

# 对最终测试集进行预测
y_test_pred = final_knn.predict(X_test_final_scaled)

# 计算最终测试准确率
test_accuracy = accuracy_score(y_test, y_test_pred)

print("\n========== 最终测试结果 ==========")
print(f"最佳K = {best_k}")
print(f"最终测试集准确率 = {test_accuracy * 100:.2f}%")