from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('login2',views.login2,name="login2"),
    path('rcomplete',views.rcomplete,name="rcomplete"),
    path('copd',views.copd,name="copd"),
    path('lungcancer',views.lungcancer,name='lungcancer'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('heart',views.heart,name="heart"),
    path('predCopd',views.predCopd,name="predCopd"),
    path('predict',views.predict,name='predict'),
    path('predicDiabetes',views.predicDiabetes,name='predicDiabetes'),
    path('predHeart',views.predHeart,name='predHeart'),
    path('datafetch',views.datafetch,name="datafetch"),
    path('copdesv',views.copdesv,name="copdesv"),
    path('lungesv',views.lungesv,name='lungesv'),
    path('heartesv',views.heartesv,name='heartesv'),
    path('diaesv',views.diaesv,name="diaesv")
]