from django.db import models

class PatientReg(models.Model):
    pname = models.CharField(max_length=100)
    pemail = models.CharField(max_length=100)
    pphone = models.CharField(max_length=100)
    paddress = models.TextField()
    password = models.CharField(max_length=100)


class DoctorReg(models.Model):
    pname = models.CharField(max_length=100)
    pemail = models.CharField(max_length=100)
    pphone = models.CharField(max_length=100)
    paddress = models.TextField()
    password = models.CharField(max_length=100)

class ReportPredict(models.Model):
    Occupational_hazard = models.IntegerField()
    Genetic_Risk = models.IntegerField()
    chronic_lung_cancer = models.IntegerField()
    smocking = models.IntegerField()
    passive_smoker = models.IntegerField()
    chest_pain = models.IntegerField()
    coughing_of_blood = models.IntegerField()
    fatigue = models.IntegerField()
    weight_loss = models.IntegerField()
    dry_cough = models.IntegerField()
    clubbing_of_finger_nail = models.IntegerField()

class Heartreport(models.Model):
    patientemail = models.CharField(max_length=100)
    docname = models.CharField(max_length=100)
    reportof = models.CharField(max_length=100)
    reportnm = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    trestbps = models.CharField(max_length=100)
    chol = models.CharField(max_length=100)
    fbs = models.CharField(max_length=100)
    exang = models.CharField(max_length=100)
    ca = models.CharField(max_length=100)
    riskvalue = models.CharField(max_length=100)

class diabetesreport(models.Model):
    patientemail = models.CharField(max_length=100)
    docname = models.CharField(max_length=100)
    reportof = models.CharField(max_length=100)
    reportnm = models.CharField(max_length=100)
    glucose = models.CharField(max_length=100)
    bloodpressure = models.CharField(max_length=100)
    insulin = models.CharField(max_length=100)
    bmi = models.CharField(max_length=100)
    diapedgree = models.CharField(max_length=100)
    riskvalue = models.CharField(max_length=100)

class lungreport(models.Model):
    patientemail = models.CharField(max_length=100)
    docname = models.CharField(max_length=100)
    reportof = models.CharField(max_length=100)
    reportnm = models.CharField(max_length=100)
    Genetic_Risk = models.CharField(max_length=100)
    Occupational_hazard = models.CharField(max_length=100)
    chest_pain = models.CharField(max_length=100)
    chronic_lung_cancer = models.CharField(max_length=100)
    clubbing_of_finger_nail = models.CharField(max_length=100)
    coughing_of_blood = models.CharField(max_length=100)
    dry_cough = models.CharField(max_length=100)
    fatigue = models.CharField(max_length=100)
    passive_smoker = models.CharField(max_length=100)
    smocking = models.CharField(max_length=100)
    weight_loss = models.CharField(max_length=100)
    riskvalue = models.CharField(max_length=100)


class copd(models.Model):
    patientemail = models.CharField(max_length=100)
    docname = models.CharField(max_length=100)
    reportof = models.CharField(max_length=100)
    reportnm = models.CharField(max_length=100)
    lipcolor = models.CharField(max_length=100)
    FEV = models.CharField(max_length=100)
    Smkintensity = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    riskvalue = models.CharField(max_length=100)
