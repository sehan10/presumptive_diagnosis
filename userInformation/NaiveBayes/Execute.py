from decimal import *

import  FileReader
import  Methods


class Execution:
    Tset=[]
    T=0
    D=0
    #For Machine to calculate
    def excute(self):
        FinalList =[]
        Instance = Methods.MethodRepository()
        File = FileReader.File()
        lisst = File.FileRead()
        TraininD=lisst[0]
        TestD=lisst[1]
        TestSet = TestD
        TrainSet = TraininD
        self.Tset=TrainSet
        x = len(TraininD[0])
        Test=Decimal(1)
        Data=[]
        Class = Instance.UniqueList(TraininD)
        for increment in range(x - 1):
            #Spilting Data i.e in training and testing

            #Count repetition of attribute per class
            Data=Instance.CountRepInClass(TraininD)
            self.D=Data
            AttributeList=Instance.Findings(TraininD,increment,Class)
            AttributeList = Instance.Filter(AttributeList,Class)

            Difference = Instance.CountDifferent(TraininD, increment)
            AttributeList=Instance.ZeroFreProblem(AttributeList,Difference)
            Total=Instance.Total(TraininD)
            self.T=Total
            Structure =Instance.MakeStruc(AttributeList,TraininD,increment)
            Difference = Instance.CountDifferent(TraininD,increment)
            Attributes=Difference
            Difference = len(Difference)
            C=Instance.PredictC(Structure,Total,Difference)
            X=Instance.PredictX(Structure,TraininD,Difference)
            XC = Instance.PredictXC(Structure,Data,Difference)
            PosterierP = Instance.PosterierP(C,XC,X,Attributes)
            FinalStruc = Instance.FinalStructure(PosterierP,Attributes)
            FinalList.append(FinalStruc)
           # print(AttributeList)
            #have to look here
        EvolveRes=Instance.EvolveAttP(FinalList,TestSet,Total)
        Total=len(TrainSet)-1
        POfClasses=Instance.findClassP(Total,Data)
        #ZeroFrequency =Instance.ZeroFreProblem(EvolveRes)
        Prediction=Instance.Predict(EvolveRes,POfClasses)
        Result = Instance.GivePrediction(Prediction)
        Accuracy = Instance.Accuracy(TestD,Result)
        #print ("Accuray:%s " %Accuracy)
        return Accuracy,FinalList

    #For User From Website
    def FindUsers(self, UserData, finallist):
        instance= Methods.MethodRepository()
        EvolveRes = instance.EvolveForUser(finallist, UserData, self.T)
        Total = len(self.Tset) - 1
        POfClasses = instance.findClassP(Total, self.D)
        # ZeroFrequency =Instance.ZeroFreProblem(EvolveRes)
        Prediction = instance.Predict(EvolveRes, POfClasses)
        Result = instance.GivePrediction(Prediction)
        return Result



