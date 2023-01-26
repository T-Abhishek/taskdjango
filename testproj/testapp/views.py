from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config={
  "databaseURL": "https://test-b3740-default-rtdb.firebaseio.com",
  "apiKey":"AIzaSyBBO7QYU97SBu-2GczBB8dZUjxZxaH18Wc",
  "authDomain": "test-b3740.firebaseapp.com",
  "projectId": "test-b3740",
  "storageBucket": "test-b3740.appspot.com",
  "messagingSenderId": "1029610828835",
  "appId": "1:1029610828835:web:9e9530f4b3747684586d96"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def test(request):
    return HttpResponse("Test Response OK, please navgiate to 'localhost:8000/home'")

def home(request):
    day = database.child('Data').child('Day').get().val()
    img1 = database.child('Data').child('img_url').get().val()
    vid1=database.child('Data').child('vd1_url').get().val()
    aud1=database.child('Data').child('aud_url').get().val()
    return render(request,"Home.html",{"day":day,"img1":img1 ,"vid1":vid1,"aud1":aud1})