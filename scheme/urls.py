from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from scheme.views import *


urlpatterns = [
    path('home',views.home),
	path('afterhome',views.afterhome),
	path('requestScheme',views.requestScheme),
	path('central',views.central),
	path('newPage', views.newPage,name='newPage'),
	path('showscheme',views.showscheme),
	path('state_autho_rep',views.state_autho_rep),
	path('',views.login),
	path('logout',views.logout),
	path('afterlogin',views.afterlogin),
	path('requested',views.requested),
	path('newSchemeFromCentral',views.newSchemeFromCentral),
	path('schemeDetails',views.schemeDetails),
	path('modifyscheme',views.modifyscheme),
	path('modification',views.modification),
	path('aftermodify',views.aftermodify),
	path('CentralchooseAction',views.CentralchooseAction),
	path('rejectionreason',views.rejectionreason),
	path('afterreject',views.afterreject),
	path('requestmodifyscheme',views.requestmodifyscheme),
	path('requestmodification',views.requestmodification),
	path('aftermodificationrequest',views.aftermodificationrequest),
	path('viewrequest',views.viewrequest),
	path('viewrequestdetails',views.viewrequestdetails),
	path('afterviewrequestdetails',views.afterviewrequestdetails),
	path('afterreqreject',views.afterreqreject),
	path('providefund',views.providefund),
	path('afterprovide',views.afterprovide),
	path('receivedfunds',views.receivedfunds),
	path('uploadreport',views.uploadreport),
	path('statependingauth',views.statependingauth),
	path('submitstateauth',views.submitstateauth),
	path('centralpendingauth',views.centralpendingauth),
	path('viewauthrep',views.viewauthrep),
	path('approveauth',views.approveauth),
	path('newemployee',views.newemployee),
	path('proceedemp',views.proceedemp),
	path('statemodification',views.statemodification),
	path('modificationreqfromcentralaction',views.modificationreqfromcentralaction),
	path('staterejectionreason',views.staterejectionreason),
	path('stateafterreject',views.stateafterreject),
	path('modificationreqfromcentral',views.modificationreqfromcentral),
	path('modificationreqfromcentralDetails',views.modificationreqfromcentralDetails),
	path('stateaftermodifyreject',views.stateaftermodifyreject),
	path('statemodifyrejectionreason',views.statemodifyrejectionreason),
	path('rejectedschemesstate',views.rejectedschemesstate),
	path('rejectedschemescentral',views.rejectedschemescentral)

]

urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)