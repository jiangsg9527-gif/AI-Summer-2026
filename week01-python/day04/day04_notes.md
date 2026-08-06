# Day 4 学习笔记：面向对象编程与 LinearModel

## 一、今天学习了什么

今天主要学习了 Python 面向对象编程中的以下内容：

- 类与对象
- `__init__()` 构造函数
- `self`
- 属性与方法
- 简单封装
- 参数检查
- JSON 文件保存与加载
- 继承
- `super()`

今天不要求完全默写所有形式，重点是能够看懂程序结构，并知道每一部分大概负责什么。

## 二、类和对象

### 1. 类

类可以理解为一张设计图或模板。

```python
class Student:
    pass
```

这里定义了一个名为 `Student` 的类。

### 2. 对象

对象是根据类创建出来的具体实例。

```python
student1 = Student()
student2 = Student()
```

`student1` 和 `student2` 是两个不同的对象。

可以理解为：

```text
类：学生模板
对象：小明、小红
```

## 三、`__init__()` 构造函数

`__init__()` 会在创建对象时自动执行，用来设置对象的初始数据。

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
```

创建对象：

```python
student1 = Student("小明", 20, 85)
```

可以理解为：

```text
student1.name = "小明"
student1.age = 20
student1.score = 85
```

## 四、`self` 是什么

`self` 表示当前正在操作的对象。

```python
class Student:
    def introduce(self):
        print(self.name)
```

调用：

```python
student1.introduce()
```

此时：

```text
self 代表 student1
```

可以记住：

```text
self = 当前对象
```

## 五、属性和方法

属性是对象保存的数据：

```python
self.name
self.age
self.score
```

方法是类中的函数，表示对象能够执行的操作：

```python
def introduce(self):
    ...

def get_level(self):
    ...

def update_score(self, new_score):
    ...
```

## 六、Student 类练习

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print(
            f"我叫{self.name}，"
            f"年龄是{self.age}，"
            f"成绩是{self.score}。"
        )

    def get_level(self):
        if self.score >= 90:
            return "优秀"
        elif self.score >= 80:
            return "良好"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def update_score(self, new_score):
        if not 0 <= new_score <= 100:
            raise ValueError("成绩必须在0～100之间！")

        self.score = new_score
```

## 七、LinearModel 类

线性模型公式：

```text
y = weight × x + bias
```

基础版本：

```python
class LinearModel:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict(self, x):
        result = self.weight * x + self.bias
        return result

    def show_params(self):
        print("模型权重：", self.weight)
        print("模型偏置：", self.bias)
```

创建对象：

```python
model = LinearModel(2, 1)
```

表示：

```text
y = 2x + 1
```

预测：

```python
prediction = model.predict(5)
```

计算过程：

```text
2 × 5 + 1 = 11
```

## 八、简单封装

为了避免外部随意把参数改成错误类型，可以使用内部属性：

```python
self._weight
self._bias
```

单下划线表示：

```text
这是类内部使用的属性，外部不应该随意直接修改。
```

推荐通过方法修改参数：

```python
def set_params(self, weight, bias):
    if not isinstance(weight, (int, float)):
        raise TypeError("模型权重必须是数字！")

    if not isinstance(bias, (int, float)):
        raise TypeError("模型偏置必须是数字！")

    self._weight = weight
    self._bias = bias
```

推荐：

```python
model.set_params(3, 2)
```

不推荐：

```python
model._weight = "abc"
```

## 九、为什么在 `__init__()` 中调用 `set_params()`

```python
def __init__(self, weight, bias):
    self.set_params(weight, bias)
```

这样创建对象时，参数也会先经过检查。

例如：

```python
model = LinearModel("abc", 1)
```

会抛出：

```text
模型权重必须是数字！
```

## 十、JSON 文件的作用

对象中的参数保存在内存中，程序结束后会消失。

JSON 文件可以把参数保存到硬盘。

### 保存参数

```python
def save(self, filename):
    model_data = {
        "weight": self._weight,
        "bias": self._bias
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            model_data,
            file,
            ensure_ascii=False,
            indent=4
        )
```

生成的文件内容：

```json
{
    "weight": 3,
    "bias": 2
}
```

### 加载参数

```python
def load(self, filename):
    with open(filename, "r", encoding="utf-8") as file:
        model_data = json.load(file)

    self.set_params(
        model_data["weight"],
        model_data["bias"]
    )
```

## 十一、保存和加载流程

```text
创建模型
    ↓
修改参数
    ↓
保存到 linear_model.json
    ↓
程序结束后文件仍然存在
    ↓
创建一个新模型
    ↓
从 JSON 文件加载参数
    ↓
恢复原来的模型参数
```

## 十二、继承

继承表示：

```text
子类可以直接拥有父类已有的属性和方法。
```

父类：

```python
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def show_model_name(self):
        print("模型名称：", self.model_name)
```

子类：

```python
class LinearModel(BaseModel):
    ...
```

括号里的 `BaseModel` 表示：

```text
LinearModel 继承 BaseModel
```

## 十三、`super()` 的作用

```python
super().__init__("LinearModel")
```

表示：

```text
执行父类的 __init__() 初始化方法。
```

可以近似理解为：

```python
BaseModel.__init__(self, "LinearModel")
```

常见继承模板：

```python
class 子类(父类):
    def __init__(self, 参数):
        super().__init__(父类需要的参数)
        self.子类属性 = 参数
```

在本练习中：

```python
class LinearModel(BaseModel):
    def __init__(self, weight, bias):
        super().__init__("LinearModel")
        self.set_params(weight, bias)
```

创建：

```python
model = LinearModel(2, 1)
```

执行过程：

```text
1. 创建 LinearModel 对象
2. 执行 LinearModel 的 __init__()
3. super().__init__("LinearModel")
4. 父类保存 model_name
5. self.set_params(2, 1)
6. 子类保存 weight 和 bias
```

最终对象中拥有：

```text
来自父类：
model_name
show_model_name()

来自子类：
_weight
_bias
set_params()
predict()
show_params()
save()
load()
```

## 十四、主程序入口

```python
if __name__ == "__main__":
```

表示：

```text
只有直接运行当前文件时，才执行下面的测试代码。
```

## 十五、今天的重点总结

```text
类是模板，对象是根据模板创建的具体实例。

__init__() 在创建对象时自动执行。

self 表示当前正在操作的对象。

属性是对象保存的数据。

方法是对象能够执行的功能。

封装通过方法检查和修改内部数据。

JSON 用于保存和恢复模型参数。

继承让子类拥有父类已有的功能。

super().__init__() 用于执行父类的初始化。
```

## 十六、当前阶段的学习要求

目前不要求完全默写所有代码。

达到下面三个目标即可：

1. 看见类和对象代码时，知道它们在做什么；
2. 看见 `class LinearModel(BaseModel)` 时，知道这是继承；
3. 看见 `super().__init__()` 时，知道它在执行父类初始化。

后续通过多次练习，语法会逐渐熟悉。
