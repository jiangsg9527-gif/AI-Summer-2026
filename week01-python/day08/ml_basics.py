from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x=[
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
]

y=[0,0,0,0,0,1,1,1,1,1]

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train =", X_train)
print("X_test =", X_test)

print("y_train =", y_train)
print("y_test =", y_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("预测结果：", y_pred)
print("真实结果：", y_test)
accuracy = accuracy_score(y_test, y_pred)

# print("准确率：", accuracy*100,"%")
print(f"准确率：{accuracy*100:.2f}%")

new_students = [
    [2.5],
    [4.5],
    [6.5],
    [8.0]
]

probabilities = model.predict_proba(new_students)

print(probabilities)



#---------------------------第二个案例--------------------

from sklearn.datasets import load_iris

iris = load_iris()

print(type(iris))
print(iris.keys())

print("\n特征名称：")
print(iris.feature_names)

print("\n类别名称：")
print(iris.target_names)

print("\nX的形状：")
print(iris.data.shape)

print("\ny的形状：")
print(iris.target.shape)

print("\n前5个样本：")
print(iris.data[:5])

print("\n前5个标签：")
print(iris.target[:5])


# ============================================
# 把鸢尾花数据真正取出来
# ============================================

X = iris.data
y = iris.target

print("\nX的形状：", X.shape)
print("y的形状：", y.shape)


# ============================================
# 划分训练集和测试集
# ============================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nX_train形状：", X_train.shape)
print("X_test形状：", X_test.shape)

print("y_train形状：", y_train.shape)
print("y_test形状：", y_test.shape)

print("\n训练集前5个样本：")
print(X_train[:5])

print("\n训练集前5个标签：")
print(y_train[:5])

from sklearn.linear_model import LogisticRegression

# 创建逻辑回归模型
model = LogisticRegression(max_iter=200)

# 使用训练集训练模型
model.fit(X_train, y_train)

print("模型训练完成！")
y_pred = model.predict(X_test)

print("\n预测结果：")
print(y_pred)

print("\n真实结果：")
print(y_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print(f"\n准确率：{accuracy * 100:.2f}%")


# 取测试集中的第一朵花
one_flower = X_test[0:1]

print("\n第一朵测试花的4个特征：")
print(one_flower)

# 预测类别
prediction = model.predict(one_flower)

print("\n预测的数字类别：")
print(prediction)

# 查看对应的真实花名
print("\n预测的花名：")
print(iris.target_names[prediction[0]])

# 查看真实答案
print("\n真实的数字类别：")
print(y_test[0])

print("\n真实的花名：")
print(iris.target_names[y_test[0]])

probabilities = model.predict_proba(one_flower)

print("\n三个类别的预测概率：")
print(probabilities)


# new_flower=[[5.0,3.4,1.5,0.2]]

new_flower = [[6.0, 2.9, 4.9, 1.5]]  #不容易判断的花

#预测类别
new_prediction=model.predict(new_flower)

print("\n新花预测的数字类别：")
print(new_prediction)

#根据数字类别找到花名
new_flowers_name=iris.target_names[new_prediction[0]]
print("\n新花预测的花名：")
print(new_flowers_name)

#预测三个类别的概率
new_probabilities=model.predict_proba(new_flower)

print("\n新花属于各类别的概率：")

for name, probability in zip(iris.target_names, new_probabilities[0]):
    print(f"{name}: {probability * 100:.2f}%")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\n混淆矩阵：")
print(cm)
from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

print("\n分类报告：")
print(report)
