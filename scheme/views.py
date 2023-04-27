from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Schemesgov
from .models import Department,Modify,StateAuth
from django.contrib.auth.models import User,auth
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm



# Create your views here.
govid=0
scheme=""
def home(request):
	return render(request,'home.html')
def afterhome(request):
	myfile=request.FILES['file']
	myfile1=request.FILES['fi']
	myfile2=request.FILES['fe']
	fs = FileSystemStorage()
	name=fs.save(myfile.name,myfile)
	name1=fs.save(myfile1.name,myfile1)
	name2=fs.save(myfile2.name,myfile2)
	url=fs.url(name)
	url1=fs.url(name1)
	url2=fs.url(name2)

	print(url)
	print(url1)
	print(url2)
	return render(request,'login.html')
def login(request):
    return render(request,'login.html')

def showscheme(request):
	schemeName=[]
	data=Schemesgov.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	for i in schemeName:
		if i in request.GET:
			scheme=i
	result=Schemesgov.objects.filter(scheme=scheme)
	return render(request,"showscheme.html",{"result":result})

def afterlogin(request):
	global govid
	userid=""
	password=""
	res=[]
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
		domainid=t%10
		govid=t//10	
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name

		result=Schemesgov.objects.filter(ministry=ministry)
		for i in result:
			if i.central_status=="approved" or i.state_status=="approved":
				res.append(i)
		
		if govid==1:
			if domainid==1:
				return render(request,"Centralauthority.html",{"result":res})
			elif domainid==2:	
				return render(request,"Centralindex.html",{"result":res})
		elif  govid==2:
			if domainid==1:
				return render(request,"Stateauthority.html",{"result":res})
			elif domainid==2:
				return render(request,"Stateindex.html",{"result":res})
		elif govid==0:
				return redirect(newemployee)		
    	
	else:	
		userid= request.POST["userid"]
		password= request.POST["password"]

		userint=int(userid)
		print(userint)

		empid=(userint % 1000000000000)
		t=userint // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			print(t)
			t=t//100
			print(t)
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
		domainid=t%10
		govid=t//10	

		print(empid)
		print(ministryid)
		print(domainid)
		print(govid)	



		print(userid)
		print(password)

		user=auth.authenticate(username=userid,password=password)
		if govid==0:
			return redirect(newemployee)	
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name

		result=Schemesgov.objects.filter(ministry=ministry)
		for i in result:
			if i.central_status=="approved" or i.state_status=="approved":
				res.append(i)

		if user is not None:
			auth.login(request,user)
			if govid==1:
				if domainid==1:
					return render(request,"Centralauthority.html",{"result":res})
				elif domainid==2:	
					return render(request,"Centralindex.html",{"result":res})
			elif  govid==2:
				if domainid==1:
					return render(request,"Stateauthority.html",{"result":res})
				elif domainid==2:
					return render(request,"Stateindex.html",{"result":res})
		elif user is None:
			return redirect(login)
		return redirect(login)		


def logout(request):
    auth.logout(request)
    return redirect(login)


def requestScheme(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
		domainid=t%10
		govid=t//10	

		res=Department.objects.filter(code=ministryid)
		for i in res:
			ministry=i.dept_name
	return render(request,'requestScheme.html',{"ministry":ministry})




	
def central(request):
	return render(request,'central.html')

def newPage(request):
	sch=""
	mini=""
	sec=""
	pro=""
	fund=0
	install=0


	sch = request.POST["scheme"]
	mini = request.POST["ministry"]
	#date1 = request.POST.get("date2")

	sec = request.POST["sector"]
	pro = request.POST["provisions"]
	fund = request.POST["funds"]
	install=request.POST['inst']
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
		domainid=t%10
		govid=t//10	

		if govid==1:
			o_ref = Schemesgov(scheme=sch , ministry=mini  , central_status="requested" , state_status="pending",sector=sec , provisions=pro,funds=fund,reminstall=install,install=install)
			o_ref.save()
			return render(request , 'Centralindex.html', {"message":"Scheme registered !!!"})
		elif govid==2:
				o_ref = Schemesgov(scheme=sch , ministry=mini  , state_status="requested" , central_status="pending",sector=sec , provisions=pro,funds=fund,reminstall=install,install=install)
				o_ref.save()	

				return render(request , 'Stateindex.html', {"message":"Scheme registered !!!"})


# def centralPage(request):
# 	c_sch = request.POST.get("scheme")
# 	c_min = request.POST.get("min1")
# 	c_state = request.Post.get("State")
# 	#date1 = request.POST.get("date2")
# 	c_sta = request.POST.get("sta1")
# 	c_sec = request.POST.get("sec1")
# 	c_pro = request.POST.get("pro1")


# 	o_ref = Schemesgov(c_scheme="sch" , c_ministry="min"  , c_state="state" , c_status="sta" , c_sector="sec" , c_provisions="pro")
# 	o_ref.save()

# 	return render(request , 'index.html', {"message":"registered !!!"})

def requested(request):
	global govid

	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	result=Schemesgov.objects.filter(state_status="requested" , central_status='pending',ministry=ministry)
		


	return render(request ,"RequestedScheme.html",{"result":result})

def newSchemeFromCentral(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
		domainid=t%10
		govid=t//10	
		res=Department.objects.filter(code=ministryid)
		for i in res:
			ministry=i.dept_name
	result=Schemesgov.objects.filter(state_status="pending" , central_status='requested',ministry=ministry)
	return render(request ,"newSchemeFromCentral.html",{"result":result})

def schemeDetails(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()

	for i in data:
		schemeName.append(i.scheme)
	
	
	for i in schemeName:
		if i in request.POST:
			scheme=i


	result=Schemesgov.objects.filter(scheme=scheme)

	for i in result:
		if i.central_status=="requested":

			print('result is')
			print(i)

			return render(request,"StateschemeDetails.html",{"result":result})
		elif i.central_status=="pending":
			print('result is')
			print(result)

			return render(request,"CentralschemeDetails.html",{"result":result})	

def staterejectionreason(request):
	global scheme
	return render(request,"staterejection.html")

def stateafterreject(request):
	global scheme
	
	Schemesgov.objects.filter(scheme=scheme).update(state_status="rejected", rejreason=request.POST["reason"])
	return redirect(afterlogin)			

def modifyscheme(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	result=Schemesgov.objects.filter(ministry=ministry)
	return render(request,"modifyscheme.html",{"result":result})

def modification(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	for i in schemeName:
		if i in request.POST:
			scheme=i	
		
	result=Schemesgov.objects.filter(scheme=scheme)
	return render(request,"centralschememodification.html",{"result":result})

def aftermodify(request):
	global scheme
	# schemeName=[]
	# data=Schemesgov.objects.all()

	# for i in data:
	# 	schemeName.append(i.scheme)
	# 
	# for i in schemeName:
	# 	if i in request.POST:
	# 		scheme=i

	result=Schemesgov.objects.filter(scheme=scheme)
	for i in result:
		ministry=i.ministry
		sector=i.sector
	ref=Modify(scheme=request.POST["scheme"] , funds=int(request.POST["funds"]) ,provisions=request.POST["provisions"],central_status='requested',state_status='pending',ministry=ministry,sector=sector)
	ref.save()

	return render(request,"Centralindex.html")



def CentralchooseAction(request):
	global scheme
	if "approve" in request.POST:
		Schemesgov.objects.filter(scheme=scheme).update(central_status="approved",centralminfundstatus="pending" ,stateminfundstatus="pending",stateauthfundstatus="pending",centralauthfundstatus="pending" ,docs="pending")
		return redirect(afterlogin)
	else:
		return redirect(rejectionreason)	

def rejectionreason(request):
	return render(request,"rejection.html")

def afterreject(request):
	global scheme
	
	Schemesgov.objects.filter(scheme=scheme).update(central_status="rejected", rejreason=request.POST["reason"])
	return redirect(afterlogin)

def requestmodifyscheme(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		
		res=Department.objects.filter(code=ministryid)
		for i in res:
			ministry=i.dept_name

	result=Schemesgov.objects.filter(ministry=ministry)
	return render(request,"Requestmodifyscheme.html",{"result":result})

def requestmodification(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	for i in schemeName:
		if i in request.POST:
			scheme=i	
		
	result=Schemesgov.objects.filter(scheme=scheme,)
	return render(request,"stateschememodification.html",{"result":result})

def statemodification(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	print(request.POST)	
	for i in schemeName:
		if i in request.POST:
			scheme=i	
	if 'approve' in request.POST:
		result=Schemesgov.objects.filter(scheme=scheme).update(state_status="approved",centralminfundstatus="pending" ,stateminfundstatus="pending",stateauthfundstatus="pending",centralauthfundstatus="pending" ,docs="pending")
		return redirect(afterlogin)
	elif 'modify' in request.POST:		
		# result=Schemesgov.objects.filter(scheme=scheme)
		# return render(request,"centralschememodification.html",{"result":result})
		return redirect(requestmodification)
	elif 'reject' in request.POST:
		return redirect(staterejectionreason)	

def aftermodificationrequest(request):
	result=Schemesgov.objects.filter(scheme=request.POST["scheme"])
	for i in result:
		ministry=i.ministry
		sector=i.sector

	o_ref = Modify(scheme=request.POST["scheme"],provisions=request.POST["provisions"],funds=int(request.POST['funds']),ministry=ministry,sector=sector,central_status="pending",state_status="requested")
	o_ref.save()
	return render(request,"Stateindex.html")

def viewrequest(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
		print(ministry)	
	result=Modify.objects.filter(central_status="pending",ministry=ministry)
	return render(request,"viewrequest.html",{"result":result})

def viewrequestdetails(request):
	global scheme
	schemeName=[]
	data=Modify.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	for i in schemeName:
		if i in request.POST:
			scheme=i	
		
			result=Modify.objects.filter(scheme=scheme)
	
	return render(request,"viewrequestdetails.html",{"result":result})

def afterviewrequestdetails(request):
	global scheme
	if "approve" in request.POST:
		print(request.POST)
		Schemesgov.objects.filter(scheme=scheme).update(scheme=request.POST['scheme'],ministry=request.POST['ministry'],sector=request.POST['sector'],provisions=request.POST['provisions'],funds=int(request.POST['funds']),central_status="approved",centralminfundstatus="pending" ,stateminfundstatus="pending",stateauthfundstatus="pending",centralauthfundstatus="pending" ,docs="pending")
		res=Modify.objects.filter(scheme=scheme)
		res.delete()
		return render(request,"Centralindex.html")
	else:
		return render(request,"requestrejection.html")

def afterreqreject(request):
	global scheme
	Modify.objects.filter(scheme=scheme).update(central_status="rejected",rejreason=request.POST['reason'])

	return redirect(afterlogin)

#def statependingverification(request):

def providefund(request):
	res=[]
	ministry=""
	result=Schemesgov.objects.all()
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
		print(ministry)	

	for i in result:
		if i.central_status=="approved" or i.state_status=="approved" and i.reminstall>0:
			if i.centralminfundstatus=="pending" and i.stateminfundstatus=="pending" and i.stateauthfundstatus=="pending" and i.centralauthfundstatus=="pending" and i.docs=="pending"  and i.ministry==ministry:
				res.append(i) 
				print(i)


	print(res)
	
	return render(request,"providefunds.html",{"result":res})

def afterprovide(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	

	for i in data:
		schemeName.append(i.scheme)
	for i in schemeName:
	
		if i in request.POST:
			scheme=i	
			print(scheme)	
	result=Schemesgov.objects.filter(scheme=scheme)
	
	for i in result:
		rem=i.reminstall - 1
	Schemesgov.objects.filter(scheme=scheme).update(centralminfundstatus="pass",reminstall=rem)	
	return redirect(afterlogin)

def receivedfunds(request):
	res=[]
	result=Schemesgov.objects.all()
	

	for i in result:
		if i.central_status=="approved" or i.state_status=="approved" and i.reminstall>0:
			if i.centralminfundstatus=="pass" and i.stateminfundstatus=="pending" and i.stateauthfundstatus=="pending" and i.centralauthfundstatus=="pending" and i.docs=="pending":
				res.append(i) 
				print(i)


	print(res)
	print("helo")

	return render(request,"receivedfunds.html",{"result":res})

def uploadreport(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	

	for i in data:
		schemeName.append(i.scheme)
	print (request.POST)	
	for i in schemeName:
	
		if i in request.POST :
			scheme=i	
			print(scheme)
	form=UploadFileForm(request.POST, request.FILES)
	# if form.is_valid():
	myfile=request.FILES['file']
	fs = FileSystemStorage()
	name=fs.save(myfile.name,myfile)
	url=fs.url(name)

	result=Schemesgov.objects.filter(scheme=scheme).update(docs=url,stateminfundstatus="pass")		
	return redirect(afterlogin)	




def statependingauth(request):
	res=[]
	result=Schemesgov.objects.all()
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	

	for i in result:
		if i.central_status=="approved" or i.state_status=="approved" and i.reminstall>0 and i.ministry==ministry:
			if i.centralminfundstatus=="pass" and i.stateminfundstatus=="pass" and i.stateauthfundstatus=="pending" and i.centralauthfundstatus=="pending" and i.docs!="pending":
				res.append(i) 
				print(i)
	print(res)			
	return render(request,"statependingauth.html",{"result":res})

def state_autho_rep(request):
	global scheme
	mini=""
	schemeName=[]
	data=Schemesgov.objects.all()
	

	for i in data:
		schemeName.append(i.scheme)
	print(schemeName)	
	for i in schemeName:
		if i+"submit" in request.POST:
			scheme=i	
			print(request.POST)
			print(scheme)	
			result=Schemesgov.objects.filter(scheme=scheme)
			for i in result:
				mini=i.ministry
				print(i.ministry)
			print(mini)	
			return render(request,'state_autho_rep.html',{"ministry":mini,"scheme":scheme})
		

def submitstateauth(request):
	myfile=request.FILES['file']
	fs = FileSystemStorage()
	name=fs.save(myfile.name,myfile)
	url=fs.url(name)

	ref=StateAuth(scheme=request.POST["scheme"],ministry=request.POST["ministry"],efficiency=request.POST["efficiency"],repcan=request.POST["repcan"]
	,suggestion=request.POST["report"],remark=request.POST["remark"],docs=url)
	ref.save()

	Schemesgov.objects.filter(scheme=request.POST["scheme"]).update(stateauthfundstatus="pass")
	return redirect(afterlogin)		

def centralpendingauth(request):
	res=[]
	result=Schemesgov.objects.all()
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	

	for i in result:
		if i.central_status=="approved" or i.state_status=="approved" and i.reminstall>0 and i.ministry==ministry:
			if i.centralminfundstatus=="pass" and i.stateminfundstatus=="pass" and i.stateauthfundstatus=="pass" and i.centralauthfundstatus=="pending" and i.docs!="pending":
				res.append(i) 
				print(i)
					
	print(res)			
	return render(request,"centralpendingauth.html",{"result":res})

def viewauthrep(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	

	for i in data:
		schemeName.append(i.scheme)
	print(schemeName)	
	for i in schemeName:
		if i in request.POST:
			scheme=i
	result=StateAuth.objects.filter(scheme=scheme)			
	return render(request,"centralauthreport.html",{"result":result})

def approveauth(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	

	for i in data:
		schemeName.append(i.scheme)
	print(schemeName)	
	for i in schemeName:
		if i in request.POST:
			scheme=i
	result=StateAuth.objects.filter(scheme=scheme)
	result.delete()

	Schemesgov.objects.filter(scheme=scheme).update(centralminfundstatus="pending" ,stateminfundstatus="pending",stateauthfundstatus="pending",centralauthfundstatus="pending" ,docs="pending")


	return redirect(afterlogin)

def newemployee(request):
	dept=[]
	res=Department.objects.all()

	for i in res:
		dept.append(i.dept_name)
	
	return render(request,"addemp.html",{"dept":dept})

def proceedemp(request):
	firstname=""
	lastname=""
	email=""
	gov=""
	domain=""
	ministry=""
	domain=""
	adhaar=""
	password=""
	cnfpassword=""

	firstname=request.POST['fname']
	lastname=request.POST['lname']
	email=request.POST['email']
	gov=request.POST['gov']
	domain=request.POST['domain']
	ministry=request.POST['ministry']
	adhaar=request.POST['adhaar']
	password=request.POST['password']
	cnfpassword=request.POST['cnfpassword']

	print(firstname)
	print(lastname)
	print(email)

	if password == cnfpassword:
		
		res=Department.objects.filter(dept_name=ministry)
		for i in res:
			minid=i.code
		if gov=="Central":
			govid=1
		elif gov=="State" :
			govid=2
		if domain=="Authority":
			domainid=1
		elif domain=="Ministry":
			domainid=2
		userid=str(govid)+str(domainid)+str(minid)+str(adhaar)
		print(userid)

		user=User.objects.create_user(username=userid,password=password,email=email,first_name=firstname,last_name=lastname).save()
			
		return render(request,"showid.html",{'userid':userid})					

def modificationreqfromcentral(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	result=Modify.objects.filter(state_status='pending',ministry=ministry)
	
	return render(request,'modificationreqfromcentral.html',{"result":result})

def modificationreqfromcentralDetails(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()

	for i in data:
		schemeName.append(i.scheme)
	
	
	for i in schemeName:
		if i in request.POST:
			scheme=i


	result=Modify.objects.filter(scheme=scheme)

	for i in result:
		if i.state_status=="pending":

			print('result is')
			print(i)

			return render(request,"modificationreqfromcentralDetails.html",{"result":result})

def modificationreqfromcentralaction(request):
	global scheme
	schemeName=[]
	data=Schemesgov.objects.all()
	print(request.POST)	

	for i in data:
		schemeName.append(i.scheme)
	print(request.POST)	
	for i in schemeName:
		if i in request.POST:
			scheme=i	
	if 'approve' in request.POST:
		Modify.objects.filter(scheme=scheme).update(state_status="approved",central_status='approved')
		result=Schemesgov.objects.filter(scheme=scheme)
		# for i in result:
		# 	central_status=i.central_status
		# 	state_status=i.state_status
		# 	statemin=i.stateminfundstatus
		# 	stateauth=i.stateauthfundstatus
		# 	centralmin=i.centralminfundstatus
		# 	centralauth=i.centralauthfundstatus
		# 	docs=i.docs
		# 	reminstall=i.reminstall
		Schemesgov.objects.filter(scheme=scheme).update(funds=request.POST['funds'],ministry=request.POST['ministry'],state_status="approved",centralminfundstatus="pending" ,stateminfundstatus="pending",stateauthfundstatus="pending",centralauthfundstatus="pending" ,docs="pending")
		return redirect(afterlogin)
	elif 'reject' in request.POST:
		return redirect(statemodifyrejectionreason)	

def statemodifyrejectionreason(request):
	global scheme
	return render(request,"statemodifyrejection.html")

def stateaftermodifyreject(request):
	global scheme
	
	Modify.objects.filter(scheme=scheme).update(state_status="rejected", rejreason=request.POST["reason"])
	return redirect(afterlogin)	

# def showstaterejectedscheme(request):
# 	res=Modify.objects.filter(state_status="rejected")
def rejectedschemesstate(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	result=Schemesgov.objects.filter(state_status="rejected",ministry=ministry)
	res=Schemesgov.objects.filter(central_status="rejected",ministry=ministry)
	ress=Modify.objects.filter(state_status="rejected",ministry=ministry)
	resss=Modify.objects.filter(central_status="rejected",ministry=ministry)
	return render(request,'rejectedscheme.html',{"result":result,"res":res,'ress':ress,'resss':resss})


def rejectedschemescentral(request):
	if request.user.is_authenticated:
		ui= int(request.user.username)
		empid=(ui % 1000000000000)
		t=ui // 1000000000000

		if len(str(t))==4:
			ministryid=t%100
			t=t//100
		else:
			ministryid=t%10
			t=t//10

		
		print(t)
			
		res1=Department.objects.filter(code=ministryid)
		for i in res1:
			ministry=i.dept_name
	result=Schemesgov.objects.filter(state_status="rejected",ministry=ministry)
	res=Schemesgov.objects.filter(central_status="rejected",ministry=ministry)
	ress=Modify.objects.filter(state_status="rejected",ministry=ministry)
	resss=Modify.objects.filter(central_status="rejected",ministry=ministry)
	return render(request,'rejectedschemecentral.html',{"result":result,"res":res,'ress':ress,'resss':resss})
	