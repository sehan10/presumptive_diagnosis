from decimal import *

import Read
import ID3Method

FinalList = []
Instance = ID3Method.MethodRepository()
File = Read.File()
lisst = File.FileRead()
TraininD = lisst[0]
TestD = lisst[1]
AttributesName= lisst[2]
TestSet = TestD
TrainSet = TraininD
InfoGain= []
Test = Decimal(1)
Data = []
TestResult=[]
T=[]

class DecisionTree:
    def execute(self,TestData):
        Class = Instance.UniqueList(TraininD)
        DecsionTree = Instance.MakedecisionTree(TraininD, AttributesName, Class)
        Predict = Instance.Testing(DecsionTree, TestData, AttributesName)
        Result=[]
        for i in range(len(TestD)):
            if (TestD[i][12] not in ['A','B','C','D']):
                if int(TestD[i][12]) >= 10 and int(TestD[i][12]) <= 20:
                    TestD[i][12] = 'A'
                elif int(TestD[i][12]) > 20 and int(TestD[i][12]) <= 30:
                    TestD[i][12] = 'B'
                elif int(TestD[i][12]) > 30:
                    TestD[i][12] = 'C'

                if int(TestD[i][13]) >= 0 and int(TestD[i][13]) <= 1999:
                    TestD[i][13] = 'A'
                elif int(TestD[i][13]) > 1999 and int(TestD[i][13]) <= 3500:
                    TestD[i][13] = 'B'
                elif int(TestD[i][13]) > 3500 and int(TestD[i][13]) <= 10000:
                    TestD[i][13] = 'C'

                if int(TestD[i][14]) >= 0 and int(TestD[i][14]) <= 30000:
                    TestD[i][14] = 'A'
                elif int(TestD[i][14]) > 30000 and int(TestD[i][14]) <= 80000:
                    TestD[i][14] = 'B'
                elif int(TestD[i][14]) > 80000 and int(TestD[i][14]) <= 150000:
                    TestD[i][14] = 'C'
                elif int(TestD[i][14]) > 150000:
                    TestD[i][14] = 'D'

                    
            Result.append(Instance.Testing(DecsionTree, TestD[i], AttributesName))
        Accuracy = Instance.Accuracy(TestD, Result)
        return Accuracy,Predict
'''
Inst=ID3()
Accuracy,Predict=Inst.execute(['n', 'n', 'y', 'n', 'y', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'B', 'B', 'A'])
while Accuracy<85:
    lisst = File.FileRead()
    TraininD = lisst[0]
    TestD = lisst[1]
    AttributesName = lisst[2]
    Accuracy, Predict = Inst.execute(['n', 'n', 'y', 'n', 'y', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'B', 'B', 'A'])
print(Predict)
print(Accuracy)
'''




