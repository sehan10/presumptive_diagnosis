from decimal import *
from random import  randrange
import math
import copy

class MethodRepository:
    Class = []
    entropySys = 0.0
    singleTon = True
    DescionTree = []
    IterationNo = ""
    Layer = "0"
    Data = []
    digitcounter=0

    def MakedecisionTree(self,TraininD,AttributesName,Class):
        InfoGain = []
        Class = self.UniqueList(TraininD)
        Data = self.CountRepInClass(TraininD)
        ClassEntropy=self.EntropyClass(Data)
        x = len(TraininD[0])
        self.digitcounter=0
        for increment in range(x - 1):
            # Spilting Data i.e in training and testing
            # Count repetition of attribute per class

            AttributeList = self.Findings(TraininD, increment, Class)
            AttributeList = self.Filter(AttributeList, Class)
            EntropyAttribute = self.EntropyAttribute(AttributeList)
            IG = self.Informationgain(ClassEntropy, EntropyAttribute)
            InfoGain.append(AttributesName[increment])
            InfoGain.append(AttributeList)
            InfoGain.append(IG)

        Attribute, AttList = self.MaxInfoGain(InfoGain)
        DecsionTree = self.GenrateTree(Attribute, AttList, Class)
        #temp=copy.deepcopy(AttributesName)
        for x in AttList:
            count = 0
            totalClass = len(AttList[x])
            for y in AttList[x]:
                if (y == 0):
                    count += 1
            if (count != totalClass - 1):
                TempTraininD = self.CuttingOffTraningD(TraininD, Attribute, x, AttributesName)
                TempAttributesName = self.CuttingOffAttributeName(AttributesName, Attribute)
                self.MakedecisionTree(TempTraininD,TempAttributesName,Class)

        return DecsionTree


    def CountDifferent(self,Data,AttrCol):
        Diff_Val = []
        for X in Data:
            if (X[AttrCol] not in Diff_Val):
                Diff_Val.append(X[AttrCol])

        return Diff_Val

    def MakeStruc(self, Rep_att, Data, A_val):
        i = 1
        Attr_Val = MethodRepository.CountDifferent(self, Data, A_val)
        length = len(Attr_Val)
        ClassVal = ["Attributes", "DF", "DHF1", "DHF2", "DHF3"]
        Matrix = []
        Matrix.append(ClassVal)
        for X in range(length):
            Matrix.append([])
            Matrix[i].append(Attr_Val[X])
            Matrix[i].append(Rep_att[Attr_Val[X]])
            i += 1
        return Matrix

    def CountRepInClass(self, Data):
        DF = 0
        DHF1 = 0
        DHF2 = 0
        DHF3 = 0
        temp = len(Data)
        increment = 1
        for X in Data:
            check = X

            if check[-1] == "DF":
                DF += 1
            elif check[-1] == 'DHF1':
                DHF1 += 1
            elif check[-1] == 'DHF2':
                DHF2 += 1
            elif check[-1] == 'DHF3':
                DHF3 += 1

        return [DF, DHF1, DHF2, DHF3]

    def Findings(self, data, att_Col,Class):
        TrueList = copy.deepcopy(Class)
        FalseList = copy.deepcopy(Class)
        WList = copy.deepcopy(Class)
        AbList = copy.deepcopy(Class)
        PList = copy.deepcopy(Class)
        PPList = copy.deepcopy(Class)
        classListA= copy.deepcopy(Class)
        classListB = copy.deepcopy(Class)
        classListC = copy.deepcopy(Class)
        classListD = copy.deepcopy(Class)
        PDF = 1
        PDHF1 = 1
        PDHF2 = 1
        PDHF3 = 1
        NDF = 1
        NDHF1 = 1
        NDHF2 = 1
        NDHF3 = 1
        WDF = 1
        WDHF1 = 1
        WDHF2 = 1
        WDHF3 = 1
        AbDF = 1
        AbDHF1 = 1
        AbDHF2 = 1
        AbDHF3 = 1
        DF = 1
        DHF1 = 1
        DHF2 = 1
        DHF3 = 1
        classADF=1
        for X in data:
            if X[att_Col].isdigit() and self.digitcounter == 0:
                if int(X[att_Col]) >= 10 and int(X[att_Col]) <= 20:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListA[i] not in Class):
                                classADF = copy.deepcopy(classListA[i])
                                classADF += 1
                                classListA[i] = classADF
                            else:
                                classListA[i] = 1
                        i += 1
                elif int(X[att_Col]) > 20 and int(X[att_Col]) <= 30:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListB[i] not in Class):
                                classBDF = copy.deepcopy(classListB[i])
                                classBDF += 1
                                classListB[i] = classBDF
                            else:
                                classListB[i] = 1
                        i += 1
                elif int(X[att_Col]) > 30:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListC[i] not in Class):
                                classCDF = copy.deepcopy(classListC[i])
                                classCDF += 1
                                classListC[i] = classCDF
                            else:
                                classListC[i] = 1
                        i += 1

            elif X[att_Col].isdigit() and self.digitcounter == 1:
                if int(X[att_Col]) >= 0 and int(X[att_Col]) <= 1999:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListA[i] not in Class):
                                classADF = copy.deepcopy(classListA[i])
                                classADF += 1
                                classListA[i] = classADF
                            else:
                                classListA[i] = 1
                        i += 1
                elif int(X[att_Col]) > 1999 and int(X[att_Col]) <= 3500:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListB[i] not in Class):
                                classBDF = copy.deepcopy(classListB[i])
                                classBDF += 1
                                classListB[i] = classBDF
                            else:
                                classListB[i] = 1
                        i += 1
                elif int(X[att_Col]) > 3500 and int(X[att_Col]) <= 10000:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListC[i] not in Class):
                                classCDF = copy.deepcopy(classListC[i])
                                classCDF += 1
                                classListC[i] = classCDF
                            else:
                                classListC[i] = 1
                        i += 1

            elif X[att_Col].isdigit() and self.digitcounter == 2:
                if int(X[att_Col]) > 0 and int(X[att_Col]) <= 30000:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListA[i] not in Class):
                                classADF = copy.deepcopy(classListA[i])
                                classADF += 1
                                classListA[i] = classADF
                            else:
                                classListA[i] = 1
                        i += 1
                elif int(X[att_Col]) > 30000 and int(X[att_Col]) <= 80000:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListB[i] not in Class):
                                classBDF = copy.deepcopy(classListB[i])
                                classBDF += 1
                                classListB[i] = classBDF
                            else:
                                classListB[i] = 1
                        i += 1
                elif int(X[att_Col]) > 80000 and int(X[att_Col]) <= 150000:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListC[i] not in Class):
                                classCDF = copy.deepcopy(classListC[i])
                                classCDF += 1
                                classListC[i] = classCDF
                            else:
                                classListC[i] = 1
                        i += 1
                elif int(X[att_Col]) > 150000:
                    i = 0
                    for m in Class:
                        if (X[-1] == m):
                            if (classListD[i] not in Class):
                                classDDF = copy.deepcopy(classListD[i])
                                classDDF += 1
                                classListD[i] = classDDF
                            else:
                                classListD[i] = 1
                        i += 1

            elif X[att_Col] == 'y' and X[-1] in Class:
                i = 0
                for m in Class:
                    if (X[-1] == m):
                        if (TrueList[i] not in Class):
                            PDF = copy.deepcopy(TrueList[i])
                            PDF += 1
                            TrueList[i] = PDF
                        else:
                            TrueList[i] = 1
                    i+=1
                '''
                if (X[-1] == 'DF'):
                    TrueList[0] = PDF
                    PDF += 1
                elif (X[-1] == 'DHF1'):
                    TrueList[1] = PDHF1
                    PDHF1 += 1
                elif (X[-1] == 'DHF2'):
                    TrueList[2] = PDHF2
                    PDHF2 += 1
                elif (X[-1] == 'DHF3'):
                    TrueList[3] = PDHF3
                    PDHF3 += 1
                    '''
            elif (X[att_Col] == 'n' and X[-1] in Class):
                i = 0
                for m in Class:
                    if (X[-1] == m):
                        if (FalseList[i] not in Class):
                            NDF = copy.deepcopy(FalseList[i])
                            NDF += 1
                            FalseList[i] = NDF
                        else:
                            FalseList[i] = 1
                    i += 1
                '''
                if (X[-1] == 'DF'):
                    FalseList[0] = NDF
                    NDF += 1
                elif (X[-1] == 'DHF1'):
                    FalseList[1] = NDHF1
                    NDHF1 += 1
                elif (X[-1] == 'DHF2'):
                    FalseList[2] = NDHF2
                    NDHF2 += 1
                elif (X[-1] == 'DHF3'):
                    FalseList[3] = NDHF3
                    NDHF3 += 1
                '''
            elif (X[att_Col] == 'w' and X[-1] in Class):
                i = 0
                for m in Class:
                    if (X[-1] == m):
                        if (WList[i] not in Class):
                            WDF = copy.deepcopy(WList[i])
                            WDF += 1
                            WList[i] = WDF
                        else:
                            WList[i] = 1
                    i += 1
                '''
                if (X[-1] == 'DF'):
                    WList[0] = WDF
                    WDF += 1
                elif (X[-1] == 'DHF1'):
                    WList[1] = WDHF1
                    WDHF1 += 1
                elif (X[-1] == 'DHF2'):
                    WList[2] = WDHF2
                    WDHF2 += 1
                elif (X[-1] == 'DHF3'):
                    WList[3] = WDHF3
                    WDHF3 += 1
                '''
            elif (X[att_Col] == 'ab' and X[-1] in Class):
                i = 0
                for m in Class:
                    if (X[-1] == m):
                        if(AbList[i] not in Class):
                            AbDF = copy.deepcopy(AbList[i])
                            AbDF += 1
                            AbList[i] = AbDF
                        else:
                            AbList[i] = 1
                    i += 1
                '''
                if (X[-1] == 'DF'):
                    AbList[0] = AbDF
                    AbDF += 1
                elif (X[-1] == 'DHF1'):
                    AbList[1] = AbDHF1
                    AbDHF1 += 1
                elif (X[-1] == 'DHF2'):
                    AbList[2] = AbDHF2
                    AbDHF2 += 1
                elif (X[-1] == 'DHF3'):
                    AbList[3] = AbDHF3
                    AbDHF3 += 1
                '''
            elif (X[att_Col] == 'p' and X[-1] in Class):
                i = 0
                for m in Class:
                    if (X[-1] == m):
                        if (PList[i] not in Class):
                            DF = copy.deepcopy(PList[i])
                            DF += 1
                            PList[i] = DF
                        else:
                            PList[i] = 1
                    i += 1
                '''
                if (X[-1] == 'DF'):
                    PList[0] = DF
                    DF += 1
                elif (X[-1] == 'DHF1'):
                    PList[1] = DHF1
                    DHF1 += 1
                elif (X[-1] == 'DHF2'):
                    PList[2] = DHF2
                    DHF2 += 1
                elif (X[-1] == 'DHF3'):
                    PList[3] = DHF3
                    DHF3 += 1
                '''
        if X[att_Col].isdigit():
            self.digitcounter += 1
        DataRet = {}
        DataRet = {"y": TrueList, "n": FalseList, "w": WList, "ab": AbList, "p": PList, "A": classListA, "B": classListB, "C": classListC, "D": classListD}

        return DataRet

    def Filter(self, Data,Class):
        ListToReturn = {}
        keys = ["y", "n", "w", "ab", "p","A","B","C","D"]
        increment = -1
        for J in keys:
            increment = -1
            temp = Data[J]
            if (temp != Class):
                for final in temp:
                    increment += 1
                    if (final in Class):
                        temp[increment] = 0

                ListToReturn[J] = temp

        return ListToReturn

    def EntropyClass(self, Data):
        Entropy = 0.0
        TotalData = 0.0
        x = 0.0
        for y in Data:
            TotalData += y
        for x in Data:
            p = x/TotalData
            if(p!=0.0):
                Entropy += -((p)*math.log(p,2))
            else:
                Entropy += 0.0
        return Entropy

    def EntropyAttribute(self,Attribute):
        Entropy=0.0
        TotalDataAtt=0.0
        TotalData=0.0
       # keys = ["y", "n", "w", "ab", "p"]
        for K in Attribute:
            temp = Attribute[K]
            for x in temp:
                TotalData += x
        for J in Attribute:
            temp = Attribute[J]
            for y in temp:
                TotalDataAtt += y
            Entropy += (TotalDataAtt/TotalData)*self.EntropyClass(temp)
            TotalDataAtt=0.0


        return  Entropy

    def Informationgain(self,EntropyClass,EntropyAttr):
        IG = EntropyClass-EntropyAttr
        return IG

    def MaxInfoGain(self,InfoGain):
        AttributeValue=InfoGain[2]
        AttributeList=InfoGain[1]
        AttributeName=InfoGain[0]
        for x in range(5,len(InfoGain),3):
            if(InfoGain[x] > AttributeValue):
                AttributeValue=InfoGain[x]
                AttributeList=InfoGain[x-1]
                AttributeName = InfoGain[x-2]


        return AttributeName,AttributeList

    def GenrateTree(self,AttributeName,AttributeList,Class):
        q = 0
        c=1
        r=0
        DT = []
        Leaf=""
        count = 0
        if(self.singleTon):
            str = "R"
            DT.append(str)
            self.DescionTree.append(DT)
            DT=[]
            #self.Layer +=1
            DT.append(AttributeName)
            self.DescionTree.append(DT)
            self.singleTon = False
        else:
            check=False
            for Dlist in self.DescionTree:
                w = 0
                for Xlist in Dlist:
                    if(Xlist=="?"):
                        c=copy.deepcopy(q)
                        r=copy.deepcopy(w)
                        #self.DescionTree[q][w]=AttributeName
                        #check=True
                        break
                    w += 1
                q+=1
                #if(check):
                    #break
            self.DescionTree[c][r] = AttributeName
            if (c+1 != self.DescionTree.__len__()):
                for x in AttributeList:
                    self.DescionTree[c+2].append(x)
                c += 2
                DT = []
                # self.Layer += 1
                for x in AttributeList:
                    totalClass = len(AttributeList[x])
                    i = 0
                    count = 0
                    for y in AttributeList[x]:
                        if (y == 0):
                            count += 1
                        else:
                            Leaf = Class[i]
                        i += 1

                    if (count == totalClass - 1):
                        self.DescionTree[c + 2].append("Leaf:" + Leaf)
                    else:
                        self.DescionTree[c + 2].append("?")

                DT = []



        if(c+1 == self.DescionTree.__len__()):
            DT = []
            str = "L"
            DT.append(str)
            self.DescionTree.append(DT)
            DT = []
            for x in AttributeList:
                DT.append(x)
            self.DescionTree.append(DT)
            DT = []
            DT.append("L")
            self.DescionTree.append(DT)
            DT = []
            # self.Layer += 1
            for x in AttributeList:
                totalClass = len(AttributeList[x])
                i = 0
                count = 0
                for y in AttributeList[x]:
                    if (y == 0):
                        count += 1
                    else:
                        Leaf = Class[i]
                    i += 1

                if (count == totalClass - 1):
                    DT.append("Leaf:" + Leaf)
                else:
                    DT.append("?")
            self.DescionTree.append(DT)
            DT = []



        return self.DescionTree

    def UniqueList(self,TraningData):
        list=[]
        for X in TraningData:
            list.append(X[-1])
        listunique = set(list)
        listunique =sorted(listunique,None,None,False)
        return listunique

    def CuttingOffTraningD(self,TrainingData,Attribute,x,AttributesName):
        tempTraningData=[]
        category=''
        Index=AttributesName.index(Attribute)
        for z in TrainingData:
            if z[Index].isdigit():
                if Attribute=='Tourniquet test':
                   if int(z[Index])>=10 and int(z[Index])<=20:
                       category='A'
                   elif int(z[Index]) > 20 and int(z[Index]) <= 30:
                       category = 'B'
                   elif int(z[Index]) > 30:
                       category = 'C'

                   if category == x:
                       c = list(z)
                       del c[Index]
                       tempTraningData.append(c)

                elif Attribute == 'WBC':
                    if int(z[Index]) >= 0 and int(z[Index]) <= 1999:
                        category = 'A'
                    elif int(z[Index]) > 1999 and int(z[Index]) <= 3500:
                        category = 'B'
                    elif int(z[Index]) > 3500 and int(z[Index]) <= 10000:
                        category = 'C'

                    if category == x:
                        c = list(z)
                        del c[Index]
                        tempTraningData.append(c)

                elif Attribute == 'Platelet':
                    if int(z[Index]) >= 0 and int(z[Index]) <= 30000:
                        category = 'A'
                    elif int(z[Index]) > 30000 and int(z[Index]) <= 80000:
                        category = 'B'
                    elif int(z[Index]) > 80000 and int(z[Index]) <= 150000:
                        category = 'C'
                    elif int(z[Index]) > 150000:
                        category = 'D'

                    if category == x:
                        c = list(z)
                        del c[Index]
                        tempTraningData.append(c)
            elif (z[Index]==x):
                c=list(z)
                del c[Index]
                tempTraningData.append(c)
        return tempTraningData

    def CuttingOffAttributeName(self,AttributesName,Attribute):
        AN=copy.deepcopy(AttributesName)
        Index = AN.index(Attribute)
        del AN[Index]
        return AN


    def Testing(self,DescionTree,TestinData,Attributes):
        Result = ""
        Index = 0
        Index1 = 0
        check = False
        value = ""
        for Level in range(1, len(DescionTree), 2):
            check = False
            DT = DescionTree[Level]

            for Y in Attributes:
                if Index1 < len(DT) and Y == DT[Index1]:
                    Index = Attributes.index(Y)
                    value=TestinData[Index]
                    check = True
                    break
            if check:
                continue
            if len(DT) == 4:

                DT1=DescionTree[Level-2]
                if any("Leaf:" in s for s in DT1):
                    matching = [s for s in DT1 if "Leaf:" in s]
                    if len(matching) == 2:
                        if "Leaf:" in DT1[Index1]:
                            Index1 = 1
                        else:
                            Index1 = 0

                if Index1 == 0:
                    if any(value == s for s in DT):
                        Index1 = DT.index(value)
                        continue
                elif Index1==1:
                    DTCopy= []
                    DTCopy.append(copy.deepcopy(DT[2]))
                    DTCopy.append(copy.deepcopy(DT[3]))
                    if any(value == s for s in DT):
                        Index1 = DT.index(value)
                        if Index1==0:
                            Index1=2
                        elif Index1 == 1:
                            Index1=3
                        continue

            if any(value == s for s in DT):
                Index1 = DT.index(value)
                continue
            if any("Leaf:" in s for s in DT):
                Result=DT[Index1]
                break

        return Result[5:]

    def Accuracy(self, TestD, Result):
        increment = -1
        Total = float(len(TestD))
        Count = 0
        length = len(Result)
        for X in TestD:
            if (increment < length):
                increment += 1
                if (X[-1] == Result[increment]):
                    Count += 1

        accuracy = (Count / Total) * 100
        return accuracy

    def MadeChunks(self, Data):
        heading = Data[000]
        del Data[000]
        TrainData = []
        TestData = []
        i = -1
        Total = len(Data)
        for X in range(1, 370):
            i += 1
            Random = randrange(1, Total, 3)
            Record = Data[Random]
            if (i < 340):
                TrainData.append(Record)
            if (i >= 340):
                TestData.append(Record)
        return TrainData, TestData, heading

