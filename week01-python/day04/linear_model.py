import json

class BaseModel:
    def __init__(self,model_name):
        self.model_name=model_name

    def show_model_name(self):
        print("模型名称：",self.model_name)

class LinearModel(BaseModel):
    def __init__(self,weight,bias):
         super().__init__("LinearModel")
         self.set_params(weight, bias)


    def set_params(self,weight,bias):
            if not isinstance(weight,(int,float)):
                raise TypeError("模型权重必须是数字！")
    
            if not isinstance(bias,(int,float)):
                raise TypeError("模型偏置必须是数字！")
    
            self._weight=weight
            self._bias=bias
            
    def predict(self,x):
        result=self._weight*x+self._bias
        return result
    
    def show_params(self):
        print("模型权重：",self._weight)
        print("模型偏置：",self._bias)

    def save(self,filename):
        model_data={
            "weight":self._weight,
            "bias":self._bias
        }

        with open(filename,"w",encoding="utf-8") as file:
            json.dump(model_data,file,ensure_ascii=False,indent=4)
        print("模型参数保存成功！")

    def load(self,filename):
        with open(filename,"r",encoding="utf-8") as file:
            model_data=json.load(file)
        self.set_params(
            model_data["weight"],
            model_data["bias"]
        )
        print("模型参数加载成功！")

    


if __name__ == "__main__":
    # ==========================================
    # 一、测试正常模型流程
    # ==========================================

    try:
        model = LinearModel(2, 1)
        model.show_model_name()
        print("原始模型参数：")
        model.show_params()

        prediction = model.predict(5)
        print("x=5，预测结果=", prediction)

        model.set_params(3, 2)

        print("\n修改后的模型参数：")
        model.show_params()

        prediction = model.predict(5)
        print("x=5，预测结果=", prediction)

        model.save("linear_model.json")

        new_model = LinearModel(0, 0)

        print("\n加载前的新模型参数：")
        new_model.show_params()

        new_model.load("linear_model.json")

        print("\n加载后的新模型参数：")
        new_model.show_params()

        prediction = new_model.predict(5)
        print("x=5，预测结果=", prediction)

    except (TypeError, ValueError) as error:
        print("模型参数错误：", error)

    except OSError as error:
        print("文件操作失败：", error)


    # ==========================================
    # 二、单独测试错误参数
    # ==========================================

    print("\n开始测试错误参数：")

    try:
        model.set_params("aaaa", 2)

    except TypeError as error:
        print("参数检查成功：", error)

