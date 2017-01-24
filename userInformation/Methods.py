from decimal import *
from random import  randrange
import copy
class MethodRepository:
  digitcounter = 0
  def CountRepInClass(self, Data):
      DF=0
      DHF1=0
      DHF2=0
      DHF3=0

      temp=len(Data)
      increment=1
      print ('Hello Data')
      for X in Data:
        check = X

        if  check[-1]=="DF":
            DF += 1
        elif check[-1]=='DHF1':
            DHF1 += 1
        elif check[-1]=='DHF2':
            DHF2 += 1
        elif check[-1] == 'DHF3':
            DHF3 += 1

      return [DF,DHF1,DHF2,DHF3]

  def MadeChunks(self, Data):

      del Data[000]
      TrainData= []
      TestData=[]
      i=-1
      Total = len(Data)
      for X in range(1,370):
         i +=1
         Random = randrange(1,Total,3)
         Record = Data[Random]
         if(i<270):
             TrainData.append(Record)
         if(i>=270):
             TestData.append(Record)
      return TrainData,TestData

  def Findings(self, data, att_Col, Class):
      TrueList = copy.deepcopy(Class)
      FalseList = copy.deepcopy(Class)
      WList = copy.deepcopy(Class)
      AbList = copy.deepcopy(Class)
      PList = copy.deepcopy(Class)
      PPList = copy.deepcopy(Class)
      classListA = copy.deepcopy(Class)
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
      classADF = 1
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
                  i += 1
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
                      if (AbList[i] not in Class):
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
      DataRet = {"y": TrueList, "n": FalseList, "w": WList, "ab": AbList, "p": PList, "A": classListA, "B": classListB,
                 "C": classListC, "D": classListD}

      return DataRet

  def CountDifferent(self,Data, AttrCol):
      Diff_Val= []
      CopyData = copy.deepcopy(Data)
      for i in range(len(CopyData)):
          if (CopyData[i][12] not in ['A', 'B', 'C', 'D']):
              if int(CopyData[i][12]) >= 10 and int(CopyData[i][12]) <= 20:
                  CopyData[i][12] = 'A'
              elif int(CopyData[i][12]) > 20 and int(CopyData[i][12]) <= 30:
                  CopyData[i][12] = 'B'
              elif int(CopyData[i][12]) > 30:
                  CopyData[i][12] = 'C'

              if int(CopyData[i][13]) >= 0 and int(CopyData[i][13]) <= 1999:
                  CopyData[i][13] = 'A'
              elif int(CopyData[i][13]) > 1999 and int(CopyData[i][13]) <= 3500:
                  CopyData[i][13] = 'B'
              elif int(CopyData[i][13]) > 3500 and int(CopyData[i][13]) <= 10000:
                  CopyData[i][13] = 'C'

              if int(CopyData[i][14]) >= 0 and int(CopyData[i][14]) <= 30000:
                  CopyData[i][14] = 'A'
              elif int(CopyData[i][14]) > 30000 and int(CopyData[i][14]) <= 80000:
                  CopyData[i][14] = 'B'
              elif int(CopyData[i][14]) > 80000 and int(CopyData[i][14]) <= 150000:
                  CopyData[i][14] = 'C'
              elif int(CopyData[i][14]) > 150000:
                  CopyData[i][14] = 'D'
      for X in CopyData:
          if(X[AttrCol] not in Diff_Val):
              Diff_Val.append(X[AttrCol])

      return  Diff_Val


  def MakeStruc(self, Rep_att,Data,A_val):
      i=1
      Attr_Val = MethodRepository.CountDifferent(self,Data,A_val)
      length= len(Attr_Val)
      ClassVal=["Attributes","DF","DHF1","DHF2","DHF3"]
      Matrix =[]
      Matrix.append(ClassVal)
      for X in range(length):
          Matrix.append([])
          Matrix[i].append(Attr_Val[X])
          Matrix[i].append(Rep_att[Attr_Val[X]])
          i+=1
      return Matrix
  def Total(self,Data):
      Total=len(Data)-1
      return Total

  def PredictC(self, structure,Total,Differnce):
      PC=[]
      Result=0.0
      i=-1
      for I in range(4):
          i += 1
          Result=0.0
          for J in range(1,Differnce+1):
              Result+= int(structure[J][1][i])
          Result = Result/Total
          PC.append(Result)
      return PC

  def PredictX(self,structure,Total,Difference):
      i=1
      Data=[]
      Result=0.0
      XData=[]
      Total = len(Total)
      Class =""
      X={}
      for J in range(1,Difference+1):
         Data = structure[J][1]
         Class = structure[J][0]
         for K in Data:
            Result += K
         Result=Result/Total
         X={Class: Result}
         XData.append(X)
      return XData

  def PredictXC(self,Structure,Total,Differnce):
      temp=0.0
      Result=0.0
      XCData=[]
      TempArray=[]
      k=-1
      i=-1
      Increment=-1
      Filler =["DF","DHF1","DHF2","DHF3"]
      for J in range(4):
          Class=""
          TempArray = []
          i+=1
          k+=1
          t=0
          Increment+=1
          for I in range(1,Differnce+1):
              temp = Structure[I][1][i]
              Class = Structure[I][0][t]
              Result = temp/float(Total[Increment])
              TempArray.append(Class)
              TempArray.append(Result)
          XCData.append([])
          XCData[k].append({Filler[k]:[TempArray]})
      return XCData

  def PosterierP (self,C,XC,X,Attributes):
      Result =0.0
      increment =1
      c=0
      i=-1
      ListToRet =[]
      New_XC = MethodRepository.UnlockCList(self,XC)
      New_X = MethodRepository.UnlockXList(self,X,Attributes)
      AttributeName=["DF","DHF1","DHF2","DHF3"]
      TestValue = New_XC[0][1]
      for X in range(len(C)):
          increment=1
          c=0
          ListToRet.append([])
          i+=1
          ListToRet[i].append(AttributeName[X])
          for J in range(len(New_X)):
              ClassName= New_XC[X][c]
              AttrCLass =New_XC[X][increment]
              Attribute = New_X[J]
              Class = C[X]
              Result=None
              getcontext().prec=3
              Result=round(((AttrCLass*Class) /Attribute), 3)
              increment +=2
              c+=2
              ListToRet[i].append(ClassName)
              ListToRet[i].append(Result)
      return ListToRet



#have to look here
  def UnlockCList(self,Structure):
      ClasList =["DF","DHF1","DHF2","DHF3"]
      ListToRet = []
      for X in range(len(ClasList)):
          test = Structure[X]
          newVal = test[0]
          anotherNewVal = newVal[ClasList[X]]
          anAnNewVal = anotherNewVal[0]
          ListToRet.append(anAnNewVal)
      return ListToRet

  # have to look here
  def UnlockXList(self,Structure,Attributes):
      XList=["n","y"]
      ListToRet =[]
      for X in range(len(Attributes)):
         Test = Structure[X]
         NewVal = Test[Attributes[X]]
         ListToRet.append(NewVal)
      return ListToRet

  def FinalStructure(self,PosterierP, Attributes):
      FinalStruc=[]
      i=1
      k=0
      index =1
      FinalStruc.append(["Attribute","DF","DHF1","DHF2","DHF3"])
      for X in Attributes:
          FinalStruc.append([])
          FinalStruc[i].append(X)
          i+=1

      for J in PosterierP:
          index =1
          k=0
          for T in Attributes:
              k+=2
              temp = J[k]
              FinalStruc[index].append(temp)
              index+=1
      return FinalStruc

  def Filter(self, Data, Class):
      ListToReturn = {}
      keys = ["y", "n", "w", "ab", "p", "A", "B", "C", "D"]
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

  def EvolveAttP(self,FinalStruct,TestD, Total):
      increment = 0
      index = -1
      legth = len(TestD)
      EvolvingList = []
      for Test in range(len(TestD)):
          EvolvingList.append([])
          increment = 0

          index += 1
          for X in FinalStruct:
              j = 1
              temp = TestD[Test][increment]
              increment += 1
              for J in X:
                  if (j > 1):
                      if (J[0] == temp):
                          EvolvingList[index].append(J)
                  j += 1
      return EvolvingList

  def EvolveForUser(self,FinalStruct,TestD, Total):
      increment = 0
      index = -1
      legth = len(TestD)
      EvolvingList = []

      increment = 0
      EvolvingList.append([])

      index += 1
      for X in FinalStruct:
          j = 1
          temp = TestD[increment]
          increment += 1
          for J in X:
              if (j > 1):
                  if (J[0] == temp):
                      EvolvingList[index].append(J)
              j+= 1
      return EvolvingList


  def findClassP(self,Total,Findings):
      Result=[]
      temp=0.0
      t1=0.0
      t2=0.0
      for X in Findings:
          t1=float(X)
          t2=float(Total)
          temp= t1/t2
          Result.append(temp)
      return Result

  def Predict(self,Values,ClassP):
     temp=1.0
     temp1 = 1.0
     temp2 = 1.0
     temp3 = 1.0

     Final={}
     Result=[]
     i=-1
     for R in Values:
         temp = 1.0
         temp1 = 1.0
         temp2 = 1.0
         temp3 = 1.0
         Result.append([])
         i+=1
         count =0
         for A in R:
             t1=float(A[1])

             M=temp*t1
             temp=M

             t2=float(A[2])
             B=temp1*t2
             temp1=B

             t3=float(A[3])
             C=temp2*t3
             temp2=C

             t4=float(A[4])
             D=temp3*t4
             temp3=D
             count+=1



         temp=round(temp*ClassP[0],15)
         temp1 = round(temp1 * ClassP[1],15)
         temp2 = round(temp2 * ClassP[2],15)
         temp3 = round(temp3 * ClassP[3],15)
         if( temp2>0):
             print("Yes yes yes!")
         Result[i].append(temp)
         Result[i].append(temp1)
         Result[i].append(temp2)
         Result[i].append(temp3)

     return Result








  def Accuracy(self,TestD,Result):
      increment =-1
      Total = float(len(TestD))
      Count=0
      length= len(Result)
      print ('Actual     Prediction')
      for X in TestD:
          print(X[-1]+"        "+Result[increment])
          if(increment< length):
             increment += 1
             if(X[-1]==Result[increment]):
                 Count+=1

      accuracy = (Count/Total)*100
      return  accuracy

  def GivePrediction(self,Predictions):
      Classes =["DF","DHF1","DHF2","DHF3"]
      result=[]
      for predict in Predictions:
          temp = predict
          i=0
          location =0
          compare=0
          for X in predict:
               if(X>compare):
                   location=i
                   compare=X
               i+=1
          reply = Classes[location]
          result.append(reply)

      return  result
  def GivePredictionToUser(self,Prediction):
      Classes = ["DF", "DHF1", "DHF2", "DHF3"]
      result = []


      i = 0
      location = 0
      compare = 0
      for X in Prediction:
        if (X > compare):
            location = i
            compare = X
        i += 1
      reply = Classes[location]
      result.append(reply)

      return result


  def ZeroFreProblem(self, Data, Keys):

      for K in Keys:
          Lisst = Data[K]
          j=-1
          for i in Lisst:
               j+=1
               Lisst[j]+=1
      return Data

  def UniqueList(self, TraningData):
      list = []
      for X in TraningData:
          list.append(X[-1])
      listunique = set(list)
      listunique = sorted(listunique,None,None, False)
      return listunique



























