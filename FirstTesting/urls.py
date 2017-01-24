"""FirstTesting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import Webapp.views
import userInformation.views
#from Webapp.views import contactus
#from Webapp.views import aboutus	

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^Webapp/', include('Webapp.urls')),
   #url(r'^userInformation/', include('userInformation.urls')),
    url(r'^$',Webapp.views.home),
	url(r'^Home',Webapp.views.home ),
	url(r'^AboutUs',Webapp.views.aboutus ),
    url(r'^ContactUs',Webapp.views.contactus),
	#Show Naive Bayes Page #
	url(r'^NaiveBayes', userInformation.views.naiveBayes),
	#Show Random Forest Page #
	url(r'^RandomForest',userInformation.views.randomForest),
	#Show Decision Tree Page #
	url(r'^DecisionTree/Prediction', userInformation.views.responseTodt, name='responseToDecisionTree'),
    url(r'^DecisionTree', userInformation.views.decisionTree),
	#Show Combo Page #
	url(r'^Combo', userInformation.views.Combo),
	#url(r'^NaiveBayes/Prediction', views.responseToNb, name='response'),
    # url(r'^RandomForest/Prediction', views.responseTorf, name='responsetorf'),
    #url(r'^DecisionTree/Prediction', userInformation.views.responseTodt, name='responseToDecisionTree'),
    # url(r'^Combo/Prediction', views.response_combo, name='responseToCombo'),
    
]
