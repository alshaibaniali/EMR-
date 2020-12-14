from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PatientReg
from doctor.models import copd
from doctor.models import lungreport
from doctor.models import diabetesreport
from doctor.models import Heartreport
import sqlite3
from django.contrib.auth.models import auth
from django.contrib import messages
loginUser = ""
loginFlag = False

# Create your views here.
def home(request):
    return render(request,'patient/home.html')
def register(request):
    return render(request,'patient/patientRegister.html')
def login2(request):
    return render(request,'patient/home.html')

def pregister(request):
    if request.method == 'POST':
        full_name = request.POST['fname']
        pemail2 = request.POST['pemail']
        ppassword = request.POST['Ppassword']
        phoneno = request.POST['phone']
        address = request.POST['address']
        #report1 = "COPD.pdf"
        #reportof1 = "Copd"
        #doctornm1 = "kaisher"
        new_reg = PatientReg(pname=full_name,pemail=pemail2,pphone=phoneno,password=ppassword,paddress=address)
        new_reg.save()
        '''a = PatientReg.objects.get(pemail=pemail2)
        a.report = report1
        a.reportof = reportof1
        a.doctornm = doctornm1
        a.save()'''
        
        
        print("user created") 
        return render(request,'patient/rcomplete.html')
        
    else :
        
        return render(request,'patient/patientRegister.html')
def copdreport(request):
    email = request.POST['pemail']
    copdr=copd.objects.get(patientemail = email)
    doctornm = copdr.docname
    patemail = copdr.patientemail
    reportof1 = copdr.reportof
    lipcol = copdr.lipcolor
    fev11 = copdr.FEV
    smkint = copdr.Smkintensity
    temp = copdr.temp
    risk = copdr.riskvalue
    dwn = copdr.reportnm
    return render(request,'patient/copdReport.html',{"docname1":doctornm,"pemail1":patemail,"reportof":reportof1,"lipcolor":lipcol,
                                                      "FEV1":fev11,"smoking_intensity":smkint,"temperature":temp,"data3":risk,"download":dwn  })
def Heartreports(request):
    email = request.POST['pemail']
    heartr = Heartreport.objects.get(patientemail = email)
    docnm = heartr.docname
    reportof1 = heartr.reportof
    reportnm1 = heartr.reportnm
    cp1 = heartr.cp
    trestbps1 = heartr.trestbps
    chol1 = heartr.chol
    fbs1 = heartr.fbs
    exang1 = heartr.exang
    ca1 = heartr.ca
    riskvalue1 = heartr.riskvalue
    return render(request,'patient/heartreport.html',{"docname1":docnm,"reportof":reportof1,"download":reportnm1,"cp":cp1,
                                                    "trestbps":trestbps1,"chol":chol1,"fbs":fbs1,"exang":exang1,"ca":ca1,"data2":riskvalue1,"pemail1":email})
def LunCancerreport(request):
    email = request.POST['pemail']
    lungr = lungreport.objects.get(patientemail = email)
    docname1 = lungr.docname
    reportof1= lungr.reportof
    reportnm1 = lungr.reportnm
    Genetic_Risk1 = lungr.Genetic_Risk
    Occupational_hazard1 = lungr.Occupational_hazard
    chest_pain1 = lungr.chest_pain
    chronic_lung_cancer1 = lungr.chronic_lung_cancer
    clubbing_of_finger_nail1 = lungr.clubbing_of_finger_nail
    coughing_of_blood1 = lungr.coughing_of_blood
    dry_cough1 = lungr.dry_cough
    fatigue1 = lungr.fatigue
    passive_smoker1 = lungr.passive_smoker
    smocking1 = lungr.smocking
    weight_loss1 = lungr.weight_loss
    riskvalue1 = lungr.riskvalue
    

    return render(request,'patient/lungreport.html',{"docname1":docname1,"reportof":reportof1,"download":reportnm1,"a1":Genetic_Risk1,
                                                    "b1":Occupational_hazard1,"c1":chest_pain1,"d1":chronic_lung_cancer1,
                                                    "e1":clubbing_of_finger_nail1,"f1":coughing_of_blood1,"g1":dry_cough1,"h1":fatigue1,"i1":passive_smoker1,"j1":smocking1,"k1":weight_loss1,"data":riskvalue1,"pemail1":email})
def Diabetesreport(request):
    email = request.POST['pemail']
    diar = diabetesreport.objects.get(patientemail = email)
    docname1 = diar.docname
    reportof1 = diar.reportof
    reportnm1 = diar.reportnm
    glucose1 = diar.glucose
    bloodpressure1 = diar.bloodpressure
    insulin1 = diar.insulin
    bmi1 = diar.bmi
    diapedgree1 = diar.diapedgree
    riskvalue1 = diar.riskvalue
    return render(request,'patient/diabetsreport.html',{"docname1":docname1,"reportof":reportof1,"download":reportnm1,"glucose":glucose1,"Blood_Pressure":bloodpressure1,
                                                        "Insulin":insulin1,"BMI":bmi1,"dpedgree":diapedgree1,"data22":riskvalue1,"pemail1":email})


    


def login(request):
    #email = request.POST['email']
    #password = request.POST['password']
    
    '''preg =PatientReg.objects.all()
    if(preg.pemail == email and preg.password == password):

        return render(request,'patient/test.html')
    else:
        return render(request,'patient/home.html')'''
    global loginFlag,loginUser
    if request.method == 'POST':
        username = request.POST['email']
        password2 = request.POST['password']

        print(username,password2)
        message = ""

        if len(PatientReg.objects.filter(pemail=username)) == 1 and len(PatientReg.objects.filter(pemail=username))  == 1:
            message = message + "Login successful"
            #mail = username
            #a= PatientReg.objects.exclude(pemail = "username")
            #mail = a.pname
            a=PatientReg.objects.get(pemail = username)
            fname = a.pname
            email = a.pemail

            flag = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
             
            if len(copd.objects.filter(patientemail=username)) == 1:
                
                    flag = 1
                
            else:
                flag = 0
            
            if len(lungreport.objects.filter(patientemail=username)) == 1:
                
                    flag2 = 1
                
            else:
                flag2 = 0
            if len(diabetesreport.objects.filter(patientemail=username)) == 1:
                
                    flag3 = 1
                
            else:
                flag3 = 0
            if len(Heartreport.objects.filter(patientemail=username)) == 1:
                
                    flag4 = 1
                
            else:
                flag4 = 0
            #copd1 = copd.objects.get(patientemail=username)
            #report = copd1.reportnm

            return render(request,'patient/reportpage.html',{"b":fname,"flag":flag,"flaglung":flag2,"flagdia":flag3,"flagheart":flag4,"email":email})
        else:
            #pass_hash = str(PatientReg.objects.filter(pemail=username)[0]).split(";")[4]
            #decrypt_text = pass_hash
            #message = message + "Wrong Password Entered"
            messages.info(request,'invalid crenditials')
            return render(request,"patient/home.html")
                

        print(message)
        context = {"message":message}
        #return render(request,'RTO/login.html',context)
        return render(request,'patient/home.html',context)

    else:
         return render(request,'patient/home.html')



    
