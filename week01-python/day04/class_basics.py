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


student1 = Student("小明", 20, 85)

student1.introduce()
print("成绩等级：", student1.get_level())

try:
    student1.update_score(95)
    student1.introduce()
    print("新的成绩等级：", student1.get_level())

except ValueError as error:
    print("修改失败：", error)