from django.shortcuts import render
from django.http import  HttpResponse
import MethodRepository.MethodRepo


#Show Naive Bayes Form #
def naiveBayes(request):
     return render(request,'UserInformation/NaiveBayes.html')
#
# #Show Naive Bayes Result #
# def responseToNb(request):
#    instance = MethodRepository.MethodRepo.MethodCalling()
#    accuracy, prediction=instance.response_NaiveBaye(request)
#    return render(request,'UserInformation/Response.html',{ 'accuracy':accuracy, 'prediction':prediction })
#
#
#
# #Show RandomForest form #
def randomForest(request):
     return render(request,'UserInformation/RandomForest.html')
#
# #Show Random Forest Result #
# def responseTorf(request):
#     instance = MethodRepository.MethodRepo.MethodCalling()
#     accuracy,prediction=instance.response_RandomForest(request)
#     return  render(request, 'UserInformation/Response.html', {'accuracy':accuracy, 'prediction':prediction})
# #Show Decision tree form #
def decisionTree(request):
    return render(request,'UserInformation/DecisionTree.html')
# #Show response to DT #
def responseTodt(request):
     instance = MethodRepository.MethodRepo.MethodCalling()
     accuracy,prediction = instance.response_ID3(request)
     return render(request, 'UserInformation/Response.html', {'accuracy':accuracy, 'prediction':prediction})
# #Show combo Form #
def Combo(request):
    return render(request,'UserInformation/Combo.Html')

#Show Combo response#
# def response_combo(request):
#     instance = MethodRepository.MethodRepo.MethodCalling()
#     accuracy,prediction = instance.respone_Combo(request)
#     return  render(request, 'UserInformation/Response.html', {'accuracy':accuracy, 'prediction':prediction})


