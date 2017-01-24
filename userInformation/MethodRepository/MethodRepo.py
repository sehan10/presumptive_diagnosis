#import Execute
# RandomForest #
#import Exe
# ID3#
from userInformation import ID3,Read
from userInformation import Execute
#import Read


class MethodCalling:
    def Extract(self, request):
        Result = []
        Attributes = []
        Result.append(Attributes)
        Attributes.append(request.POST['headache'])
        Attributes.append(request.POST['ROPain'])
        Attributes.append(request.POST['JPain'])
        Attributes.append(request.POST['MPain'])
        Attributes.append(request.POST['Rash'])
        Attributes.append(request.POST['Pulse'])
        Attributes.append(request.POST['BP'])
        Attributes.append(request.POST['HM'])
        Attributes.append(request.POST['Igg'])
        Attributes.append(request.POST['ChestXray'])
        Attributes.append(request.POST['Ultrasound'])
        Attributes.append(request.POST['Bleeding'])
        Attributes.append(request.POST['Tourniquet'])
        Attributes.append(request.POST['WBC'])
        Attributes.append(request.POST['Platelet'])

        return Attributes

        # Remove brackets from list #

    def removeBrackets(self, prediction):
        checklist = [['DF'], ['DHF1'], ['DHF2'], ['DHF3']]
        classes = ['DF', 'DHF1', 'DHF2', 'DHF3']
        i = 0
        for x in checklist:
            if (x == prediction):
                return classes[i]

            i += 1


    # Doing Naive Bayes Thing #
    def response_NaiveBaye(self, request):
        attribute = self.Extract(request)
        Instance = Execute.Execution()
        Accuracy, FinalStruct = Instance.excute()
        while (Accuracy < 80):
            Accuracy, FinalStruct = Instance.excute()
        # prediction = Instance.FindUsers(['n', 'n', 'y', 'n', 'y', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'B', 'B', 'A'],FinalStruct)

        prediction = Instance.FindUsers(attribute, FinalStruct)
        prediction = self.removeBrackets(prediction)
        return Accuracy, prediction






    '''
    #Extract the attributes from request #
    def Extract(self,request):
        Result = []
        Attributes = []
        Result.append(Attributes)
        Attributes.append(request.POST['headache'])
        Attributes.append(request.POST['ROPain'])
        Attributes.append(request.POST['JPain'])
        Attributes.append(request.POST['MPain'])
        Attributes.append(request.POST['Rash'])
        Attributes.append(request.POST['Pulse'])
        Attributes.append(request.POST['BP'])
        Attributes.append(request.POST['HM'])
        Attributes.append(request.POST['Igg'])
        Attributes.append(request.POST['ChestXray'])
        Attributes.append(request.POST['Ultrasound'])
        Attributes.append(request.POST['Bleeding'])

        return Attributes
'''



    # Doing Random Forest thing #

  #  def response_RandomForest(self, request):
   #      attribute = self.Extract(request)
    #     instance = Exe.RandomForest()
     #    attribute = self.convertToNumber(attribute)
      #   accuracy, prediction = instance.PlayRandom(attribute)
       #  prediction = self.convertToString(prediction)
        # return accuracy, prediction

    # Convert To string attributes to number attributes #

    def convertToNumber(self, attributes):
        newlist = []
        for x in attributes:
            if (x == 'y' or x == 'w' or x == 'ab' or x == 'p'):
                x = 1
                newlist.append(x)
            if (x == 'n'):
                x = 0
                newlist.append(x)
            if (x == 'A'):
                x = 0
                newlist.append(x)
            if (x == 'B'):
                x = 1
                newlist.append(x)
            if (x == 'C'):
                x = 2
                newlist.append(x)
            if (x == 'D'):
                x = 3
                newlist.append(x)

        return newlist

    # Convert back to string #
    def convertToString(self, prediction):
        checklist = [['0'], ['1'], ['2'], ['3']]
        classes = ['DF', 'DHF1', 'DHF2', 'DHF3']
        i = 0
        for x in checklist:
            if (x == prediction):
                return classes[i]
            i += 1

    # Doing ID3 thing #
    def response_ID3(self, request):
        instance = ID3.DecisionTree()
        attributes = self.Extract(request)
        # test = ['y','y','y','y','y','n','n','n','p','n','p','y']
        instance = ID3.DecisionTree()
        accuracy, prediction = instance.execute(attributes)
        while accuracy < 85:
            Reader = Read.File()
            lisst = Reader.FileRead()
            TraininD = lisst[0]
            TestD = lisst[1]
            AttributesName = lisst[2]
            accuracy, Predict = instance.execute(attributes)
        return accuracy, prediction

    # def respone_Combo(self, request):
    #     accuracy, outputs = self.CallingAll(request)
    #     add = 0
    #     dividen = 0
    #     for x in accuracy:
    #         add += x
    #         dividen += 1
    #     accuracy = add / dividen
    #     # attributes = self.Extract(request)
    #     # outputs = ['DF', 'DHF2', 'DHF2', 'DHF1']
    #     classes = ['DF', 'DHF1', 'DHF2', 'DHF3']
    #     counter = []
    #
    #     for iterator1 in classes:
    #         count = 0
    #         # Get the count for each memeber of class #
    #         for iterator2 in outputs:
    #             if (iterator1 == iterator2):
    #                 count += 1
    #                 # Append Append Append #
    #         counter.append(count)
    #
    #     Capture = self.VoteOut(counter)
    #     return accuracy, classes[Capture]
    #
    # def VoteOut(self, counter):
    #     # Lets get the highest number of the list #
    #     capture = 0
    #     for x, y in enumerate(counter):
    #         # shrink my list on behalf of what i have already taken #
    #         for trial in range(len(counter) - (x + 1)):
    #             next = counter[x + (trial + 1)]
    #             # Compare and capture the position #
    #             if (y < next):
    #                 capture = x + 1
    #
    #     return capture
    #
    # def CallingAll(self, request):
    #     accu_nb, pre_nb = self.response_NaiveBaye(request)
    #    # accu_rf, pre_rf = self.response_RandomForest(request)
    #     accu_dt ,pre_dt= self.response_ID3(request)
    #     predictions = []
    #     accuracy = []
    #     predictions.append(pre_nb)
    #    # predictions.append(pre_rf)
    #     accuracy.append(accu_nb)
    #    # accuracy.append(accu_rf)
    #     return accuracy, predictions
