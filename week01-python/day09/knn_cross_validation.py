from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ============================================================
# 1. 加载 Iris 数据
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target


# ============================================================
# 2. 留出20%作为最终测试集
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("交叉验证使用的数据：", X_train.shape)
print("最终测试集：", X_test.shape)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=7)
)

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score


# ============================================================
# 3. 创建“标准化 + KNN”模型
# ============================================================

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=7)
)


# ============================================================
# 4. 设置5折交叉验证
# ============================================================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# ============================================================
# 5. 进行5折交叉验证
# ============================================================

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)


# ============================================================
# 6. 输出每一折的准确率
# ============================================================

print("\n========== 5折交叉验证 ==========")

for i, score in enumerate(scores, start=1):
    print(f"第{i}折准确率：{score * 100:.2f}%")


print("\n平均准确率：")
print(f"{scores.mean() * 100:.2f}%")

# ============================================================
# 7. 使用5折交叉验证比较不同的K
# ============================================================

print("\n========== 不同K值的5折交叉验证结果 ==========")

best_k = 0
best_score = 0

for k in [1, 3, 5, 7, 9, 11, 13, 15]:

    # 创建“标准化 + KNN”的完整流程
    model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k)
    )

    # 对当前K进行5折交叉验证
    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )

    # 计算5次验证的平均准确率
    mean_score = scores.mean()

    print(
        f"K = {k:2d}，"
        f"5折平均准确率 = {mean_score * 100:.2f}%"
    )

    # 如果当前K的平均成绩更高，就更新最佳K
    if mean_score > best_score:
        best_score = mean_score
        best_k = k


print("\n========== 交叉验证选择结果 ==========")
print(f"最佳K = {best_k}")
print(f"最高5折平均准确率 = {best_score * 100:.2f}%")

# ============================================================
# 8. 使用交叉验证选出的最佳K训练最终模型
# ============================================================

final_model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=best_k)
)


# 使用全部120个训练数据训练最终模型
final_model.fit(X_train, y_train)


# ============================================================
# 9. 对最终测试集进行预测
# ============================================================

y_test_pred = final_model.predict(X_test)


# 计算最终测试准确率
test_accuracy = accuracy_score(y_test, y_test_pred)


print("\n========== 最终测试结果 ==========")

print(f"交叉验证选出的最佳K = {best_k}")
print(f"5折平均验证准确率 = {best_score * 100:.2f}%")
print(f"最终测试集准确率 = {test_accuracy * 100:.2f}%")