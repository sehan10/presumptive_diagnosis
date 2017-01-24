import  Execute
Instance = Execute.Execution()

Accuracy,FinalList=Instance.excute()
Result=Instance.FindUsers(['n', 'n', 'y', 'n', 'y', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'B', 'B', 'A'],FinalList)
print (Result)