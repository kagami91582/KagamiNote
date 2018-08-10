class BMI:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height

    def calc(self):
        return self.weight / ((self.height / 100) ** 2)

# BMI＜18.5過輕  18.5≦BMI＜24正常  24≦BMI＜27為過重  BMI≧27為肥胖
class BMIclass(BMI):
    def __init__(self, weight, height, fitness=18.5, common=24, fatter=27):
        super().__init__(weight, height)
        self.fitness = fitness
        self.common = common
        self.fatter = fatter

    def class_set(self):
        if (BMI.calc() < self.fitness):
            return "你的體重過輕"
        elif (BMI.calc() >= self.fitness and BMI.calc() < self.common):
            return "你的體重過輕"
        elif (BMI.calc() < self.fatter and BMI.calc() >= self.common):
            return "你的體重過輕"
        elif (BMI.calc() >= self.fatter):
            return "你的體重過輕"
        else:
            raise TypeError("輸入錯誤，請再試一次")

w = float(input("請輸入體重: "))
h = float(input("請輸入身高: "))
result = BMI(w,h)
print("計算出來的結果是: "  + str(BMI.calc(result)))
print("你的BMI分類在: "  + str(BMIclass.class_set()))
