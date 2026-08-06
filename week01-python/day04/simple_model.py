class LinearModel:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict(self, x):
        return self.weight * x + self.bias


model1 = LinearModel(2, 1)
model2 = LinearModel(3, 5)

print(model1.predict(5))
print(model2.predict(5))