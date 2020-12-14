from django.contrib import messages

from .models import copd
from django.views.generic.detail import DetailView
from patient.models import PatientReg
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image,Spacer
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
#creating the CNN library from here
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import GRU, Input, Dense, TimeDistributed, Activation, RepeatVector, Bidirectional
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy
import datetime
#new tensorflow


from keras import layers
import tensorflow
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from sklearn import preprocessing
from keras.models import Sequential

#random forest importing for the heart
from sklearn.ensemble import RandomForestClassifier
#importing the smtp
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
# Create your views here.
def home(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
     
    else :        

        return render(request,"doctor/home.html")    
    return render(request,'doctor/home.html')

def login(request):
    
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
    
    else :        

        return render(request,"doctor/home.html")    
    #return render(request,'doctor/home.html')
#def register(request):
#    return render(request,'doctor/register.html')

def login2(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
    
    else :        

        return render(request,"doctor/home.html")    
    return render(request,'doctor/home.html')
def predCopd(request):
    lipcolor = request.POST['lipcolor']
    FEV1 = request.POST['FEV1']
    smoking_intensity = request.POST['smoking_intensity']
    temperature = request.POST['temperature']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']

    lists = [lipcolor,FEV1,smoking_intensity,temperature]
    dataset = pd.read_csv(r"static/database/copd.csv")
    X = dataset[[ 'lipcolor','FEV1','smoking intensity','temperature' ]]
    y = dataset[['label']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)


    new_input3 =np.array([[lipcolor, FEV1, smoking_intensity,temperature]])

    y_pred = classifier.predict(new_input3)
    return render(request,'doctor/predCopd.html',{"data3":y_pred,"lipcolor":lipcolor,"FEV1":FEV1,"smoking_intensity":smoking_intensity,"temperature":temperature,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email1=request.POST['email']
        email2=request.POST['email2']
        password1=request.POST['password']
        password2=request.POST['password2']
        if password1 == password2 and email1 == email2:
            if User.objects.filter(username=email1):
                #print("Username is taken")
                messages.info(request,'Username is taken')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username=email1, password = password1, email = email1, first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            #print("Password not matching or email is not matching")
            messages.info(request,'Password not matching or email is not matching')
            return redirect('register')
        #return HttpResponse("<script>alert('User created')</script>")
        return render(request,'doctor/registerComplet.html')
    
    else :
        
        return render(request,'doctor/register.html')

def rcomplete(request):
    return render(request,'doctor/registerComplet.html')


def copd(request):
    return render(request,'doctor/copdReport.html')


def lungcancer(request):
    return render(request, 'doctor/patientReport.html')

def diabetes(request):
    return render(request,'doctor/diabetesReport.html')

def heart(request):
    return render(request,'doctor/heartReport.html')


def predict(request):
    a = request.POST['Genetic_Risk']
    b = request.POST['Occupational_hazard']
    c = request.POST['chest_pain']
    d = request.POST['chronic_lung_cancer']
    e = request.POST['clubbing_of_finger_nail']
    f = request.POST['coughing_of_blood']
    g = request.POST['dry_cough']
    h = request.POST['fatigue']
    i = request.POST['passive_smoker']
    j = request.POST['smocking']
    k = request.POST['weight_loss']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']
    
    lists =[a,b,c,d,e,f,g,h,i,j,k]
    df = pd.read_csv(r"static/database/lungcancer.csv")
    X_train = df[['Genetic Risk','OccuPational Hazards','Chest Pain','chronic Lung Disease','Clubbing of Finger Nails','Coughing of Blood','Dry Cough','Fatigue','Passive Smoker','Smoking','Weight Loss']]
    
    Y_train = df[['Level']]
    tree = DecisionTreeClassifier(max_leaf_nodes=6, random_state=0)

    tree.fit(X_train, Y_train)
    prediction = tree.predict([[a,b,c,d,e,f,g,h,i,j,k]])
    
    return render(request,'doctor/predict.html',{"data":prediction,"lists":lists,"a1":a,"b1":b,"c1":c,"d1":d,"e1":e,"f1":f,"g1":g,"h1":h,"i1":i,"j1":j,"k1":k,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})

def predicDiabetes(request):
    glucose = request.POST['Glucose']
    Blood_Pressure = request.POST['Blood_Pressure']
    Insulin = request.POST['Insulin']
    BMI = request.POST['BMI']
    dpedgree=request.POST['DiabetesPedigreeFunction']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']

    df1 = pd.read_csv(r"static/database/diabetes.csv")
    X = df1[['Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction']]

    Y = df1[['Outcome']]
    min_max_scaler = preprocessing.MinMaxScaler()
    X_scale = min_max_scaler.fit_transform(X)
 

    X_train, X_test, y_train, y_test = train_test_split(X_scale, Y, test_size=0.2, random_state = 4)
    
    model = Sequential()
    model.add(Dense(12, input_dim=5, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, Y, epochs=150, batch_size=10)
    #new_input3 =np.array([[85, 66, 0, 26.6,0.351]])
    new_input2 =np.array([[glucose, Blood_Pressure, Insulin, BMI,dpedgree]])
    predictions2 = model.predict_classes(new_input2)
    
    return render(request,'doctor/diaPred.html',{"data22":predictions2,"glucose":glucose,"Blood_Pressure":Blood_Pressure,"Insulin":Insulin,"BMI":BMI,"dpedgree":dpedgree,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})


def predHeart(request):
    cp = request.POST['cp']
    trestbps = request.POST['trestbps']
    chol = request.POST['chol']
    fbs = request.POST['fbs']
    exang = request.POST['exang']
    ca = request.POST['ca']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']
    
    df2 = pd.read_csv(r"static/database/heart.csv")
    X = df2[['cp', 'trestbps', 'chol', 'fbs','exang','ca']]

    Y = df2[['target']]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 1)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 1)
    forest.fit(X_train, Y_train)

    model = forest
    model.score(X_train, Y_train)
    new_input2 =np.array([[cp, trestbps, chol, fbs, exang,ca]])


    pred = model.predict(new_input2)
    return render(request,'doctor/heartpred.html',{"data2":pred,"cp":cp,"trestbps":trestbps,"chol":chol,"fbs":fbs,"exang":exang,"ca":ca,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})


def datafetch(request):
    d = PatientReg.objects.all()
    return render(request,'doctor/datafetch.html',{"data6":d})

def copdesv(request):
    #importing reportlab
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    #end of reportlab
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof1 = request.POST['reportof']
    lipcolor1 = request.POST['lipcolor']
    FEV1 = request.POST['FEV1']
    smoking_intensity = request.POST['smoking_intensity']
    temperature = request.POST['temperature']
    data3 = request.POST['data3']
    
    #importing the package in realtime.
    from .models import copd
    from patient.models import PatientReg
    #importing reportlab
    
    """a = copd.objects.get(patientemail = pemail1)
    a.riskvalue=data3
    a.save()"""
    #Genrating the report here
    a=PatientReg.objects.get(pemail = pemail1)
    fname = a.pname
    basename = "copdReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"



    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]
    
    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    """ptext = '<font size="12">%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))"""       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear <b> %s </b>:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of<b> %s </b>, we found the your risk of <b> %s </b> is \
                        =<b> %s </b>, we recommend you to care for your health, because your this health will\
                        help you to live the happy life. We are attaching the report here</font>' % (reportof1,reportof1,data3)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
        -----------------------------------------------------------------------------------------------------------------\
        <b>Patient name</b> = %s    || <b>Doctor name</b>=%s                    \
        </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Report of</b> = %s                   \
    </font>' % (reportof1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Lip color</b>= %s     ||<b> FEV1</b>= %s   ||   <b> smoking_intensity</b>=%s             \
    </font>' % (lipcolor1,FEV1,smoking_intensity)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>temperature</b>= %s                 \
    </font>' % (temperature)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the <b>%s</b>= <b>%s </b>                \
    </font>' % (reportof1 , data3)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' %(docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)
    #applying the smtp server here
    fromaddr = "techcitiforyou@gmail.com"
    toaddr = pemail1
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 


    msg['To'] = toaddr 
    msg['Subject'] = "This is your report"
    body = "Kindly check the attachment"
    msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    attachment = open(loc, "rb")
    p = MIMEBase('application', 'octet-stream') 


    p.set_payload((attachment).read()) 

 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

 
    s = smtplib.SMTP('smtp.gmail.com', 587) 


    s.starttls() 

 
    s.login(fromaddr, "techcititech@123") 


    text = msg.as_string() 

 
    s.sendmail(fromaddr, toaddr, text) 

    print("Msg sent successful")
    s.quit()

    #saving the data
    if len(copd.objects.filter(patientemail=pemail1)) == 1:
        a = copd.objects.get(patientemail = pemail1)
        a.docname=docname1
        a.reportof=reportof1
        a.reportnm=filename
        a.lipcolor=lipcolor1
        a.FEV=FEV1
        a.Smkintensity=smoking_intensity
        a.temp=temperature
        a.riskvalue=data3
        a.save()
    else:
        

        d = copd(patientemail=pemail1,docname=docname1,reportof=reportof1,reportnm=filename,lipcolor=lipcolor1,FEV=FEV1,Smkintensity=smoking_intensity,temp=temperature,riskvalue=data3)
        d.save()
    

    return render(request,'doctor/sendSuccess.html',{"pemail1":pemail1,"docname1":docname1,"reportof1":reportof1,
                                                      "lipcolor1":lipcolor1,"FEV1":FEV1,"smoking_intensity":smoking_intensity,"temperature":temperature,"data3":data3  })



def lungesv(request):
    a1 = request.POST['Genetic_Risk']
    b = request.POST['Occupational_hazard']
    c = request.POST['chest_pain']
    d1 = request.POST['chronic_lung_cancer']
    e = request.POST['clubbing_of_finger_nail']
    f = request.POST['coughing_of_blood']
    g = request.POST['dry_cough']
    h = request.POST['fatigue']
    i = request.POST['passive_smoker']
    j = request.POST['smocking']
    k = request.POST['weight_loss']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof1 = request.POST['reportof']
    detail = request.POST['data']
     #importing the package in realtime.
    from .models import lungreport
    from patient.models import PatientReg
    #importing reportlab
    
    #Genrating the report here
    basename = "lungReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"

    b3 = PatientReg.objects.get(pemail=pemail1)
   
    fname = b3.pname

    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"

    #giving all body of report
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size="12"></font>' 
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of <b> %s</b>, we found the your risk of %s is \
        =<b>%s</b>, we recommend you to care for your health, because your this health will\
        help you to live the happy life. We are attaching the report here</font>' % (reportof1,reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Patient email = %s    || Doctor name=%s                    \
    </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Report of = <b>%s  </b>                 \
    </font>' % (reportof1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Genetic_Risk</b>= %s     || <b>Occupational_hazard</b>= %s   ||    <b>chest_pain</b>=%s             \
    </font>' % (a1,b,c)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>chronic_lung_cancer</b>= %s     || <b>clubbing_of_finger_nail</b>= %s   ||    <b>coughing_of_blood</b>=%s             \
    </font>' % (d1,e,f)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))



    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>dry_cough</b>= %s     || <b>fatigue</b>= %s   ||   <b> passive_smoker</b>=%s             \
    </font>' % (g,h,i)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>smocking</b>= %s     || <b>weight_loss</b>= %s                \
    </font>' % (j,k)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))




    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the<b> %s</b>=<b> %s</b>                 \
    </font>' % (reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' % (docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)
    #applying the smtp server here
    fromaddr = "techcitiforyou@gmail.com"
    toaddr = pemail1
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 


    msg['To'] = toaddr 
    msg['Subject'] = "This is your report"
    body = "Kindly check the attachment"
    msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    attachment = open(loc, "rb")
    p = MIMEBase('application', 'octet-stream') 


    p.set_payload((attachment).read()) 

 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

 
    s = smtplib.SMTP('smtp.gmail.com', 587) 


    s.starttls() 

 
    s.login(fromaddr, "techcititech@123") 


    text = msg.as_string() 

 
    s.sendmail(fromaddr, toaddr, text) 

    print("Msg sent successful")
    s.quit()
    #saving the data

    if len(lungreport.objects.filter(patientemail=pemail1)) == 1:
        a = lungreport.objects.get(patientemail = pemail1)
        a.docname = docname1
        a.reportof = reportof1
        a.reportnm = filename
        a.Genetic_Risk = a1
        a.Occupational_hazard = b
        a.chest_pain = c
        a.chronic_lung_cancer = d1
        a.clubbing_of_finger_nail = e
        a.coughing_of_blood = f
        a.dry_cough = g
        a.fatigue = h
        a.passive_smoker = i
        a.smocking = j 
        a.weight_loss = k
        a.riskvalue = detail
        a.save()
    else:
        

        d = lungreport(patientemail=pemail1,docname=docname1,reportof=reportof1,reportnm=filename,Genetic_Risk=a1,Occupational_hazard=b,chest_pain=c,chronic_lung_cancer=d1,clubbing_of_finger_nail=e,coughing_of_blood=f,dry_cough=g,fatigue=h,passive_smoker=i,smocking=j,weight_loss=k,riskvalue=detail)
        d.save()





    return render(request,'doctor/sendSuccess.html')


def heartesv(request):
    cp = request.POST['cp']
    trestbps = request.POST['trestbps']
    chol = request.POST['chol']
    fbs = request.POST['fbs']
    exang = request.POST['exang']
    ca = request.POST['ca']
    pemail1 = request.POST['pemail1']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']
    detail = request.POST['data2']
    #importing the heart model
    from .models import Heartreport
    from patient.models import PatientReg
    #complete importing
    
    #Genrating the report here
    basename = "HeartReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"
    b3 = PatientReg.objects.get(pemail=pemail1)
   
    fname = b3.pname


    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"

    #giving all body of report
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size="12"></font>' 
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of <b> %s</b>, we found the your risk of %s is \
        =<b>%s</b>, we recommend you to care for your health, because your this health will\
        help you to live the happy life. We are attaching the report here</font>' % (reportof,reportof,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Patient email = %s    || Doctor name=%s                    \
    </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Report of = <b>%s  </b>                 \
    </font>' % (reportof)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>cp</b>= %s     || <b>trestbps</b>= %s   ||    <b>chol</b>=%s             \
    </font>' % (cp,trestbps,chol)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>fbs</b>= %s     || <b>exang</b>= %s   ||    <b>ca</b>=%s             \
    </font>' % (fbs,exang,ca)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))



   

    




    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the<b> %s</b>=<b> %s</b>                 \
    </font>' % (reportof,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' % (docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)

    #applying the smtp server here
    fromaddr = "techcitiforyou@gmail.com"
    toaddr = pemail1
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 


    msg['To'] = toaddr 
    msg['Subject'] = "This is your report"
    body = "Kindly check the attachment"
    msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    attachment = open(loc, "rb")
    p = MIMEBase('application', 'octet-stream') 


    p.set_payload((attachment).read()) 

 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

 
    s = smtplib.SMTP('smtp.gmail.com', 587) 


    s.starttls() 

 
    s.login(fromaddr, "techcititech@123") 


    text = msg.as_string() 

 
    s.sendmail(fromaddr, toaddr, text) 

    print("Msg sent successful")
    s.quit()

    #saving the data
    if len(Heartreport.objects.filter(patientemail=pemail1)) == 1:
        a = Heartreport.objects.get(patientemail = pemail1)
        a.docname = docname1
        a.reportof = reportof
        a.reportnm=filename
        a.cp = cp
        a.trestbps = trestbps
        a.chol = chol
        a.fbs = fbs
        a.exang = exang
        a.ca = ca
        a.riskvalue = detail
        
        a.save()
    else:
        

        d = Heartreport(patientemail=pemail1,docname=docname1,reportnm=filename,cp=cp,trestbps=trestbps,chol=chol,fbs=fbs,exang=exang,ca=ca,riskvalue=detail)
        d.save()





    return render(request,'doctor/sendSuccess.html')

def diaesv(request):
    glucose1 = request.POST['Glucose1']
    Blood_Pressure = request.POST['Blood_Pressure']
    Insulin = request.POST['Insulin']
    BMI = request.POST['BMI']
    dpedgree=request.POST['DiabetesPedigreeFunction']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']
    result = request.POST['data2']
    #importing the heart model
    from .models import diabetesreport
    from patient.models import PatientReg
    #complete importing
    
    
    #Genrating the report here
    basename = "DiabetsReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"

    b3 = PatientReg.objects.get(pemail=pemail1)
   
    fname = b3.pname

    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"

    #giving all body of report
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size="12"></font>' 
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of <b> %s</b>, we found the your risk of %s is \
        =<b>%s</b>, we recommend you to care for your health, because your this health will\
        help you to live the happy life. We are attaching the report here</font>' % (reportof,reportof,result)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Patient email = %s    || Doctor name=%s                    \
    </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Report of = <b>%s  </b>                 \
    </font>' % (reportof)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Glucose</b>= %s     || <b>Blood_Pressure</b>= %s   ||    <b>Insulin</b>=%s             \
    </font>' % (glucose1,Blood_Pressure,Insulin)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>BMI</b>= %s     || <b>DiabetesPedigreeFunction</b>= %s            \
    </font>' % (BMI,dpedgree)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))



   

    




    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the<b> %s</b>=<b> %s</b>                 \
    </font>' % (reportof,result)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' % (docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)

    #applying the smtp server here
    fromaddr = "techcitiforyou@gmail.com"
    toaddr = pemail1
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 


    msg['To'] = toaddr 
    msg['Subject'] = "This is your report"
    body = "Kindly check the attachment"
    msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    attachment = open(loc, "rb")
    p = MIMEBase('application', 'octet-stream') 


    p.set_payload((attachment).read()) 

 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

 
    s = smtplib.SMTP('smtp.gmail.com', 587) 


    s.starttls() 

 
    s.login(fromaddr, "techcititech@123") 


    text = msg.as_string() 

 
    s.sendmail(fromaddr, toaddr, text) 

    print("Msg sent successful")
    s.quit()

    #saving the data
    if len(diabetesreport.objects.filter(patientemail=pemail1)) == 1:
        a = diabetesreport.objects.get(patientemail = pemail1)
        a.docname = docname1
        a.reportof = reportof
        a.reportnm = filename
        a.glucose = glucose1
        a.bloodpressure = Blood_Pressure
        a.insulin = Insulin
        a.bmi = BMI
        a.diapedgree = dpedgree
        a.riskvalue = result
        
        
        a.save()
    else:
        

        d = diabetesreport(patientemail=pemail1,docname=docname1,reportof=reportof,reportnm=filename,glucose=glucose1,bloodpressure=Blood_Pressure,insulin=Insulin,bmi=BMI,diapedgree=dpedgree,riskvalue=result)
        d.save()


    return render(request,'doctor/sendSuccess.html')