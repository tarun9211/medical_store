from django.shortcuts import render, redirect
from login.models import Customer
# Create your views here.

def signup_form_view(request):
    if request.method == 'POST':
        first_name = request.data.first_name
        last_name = request.data.last_name
        phone_no = request.data.phone_no
        gender = request.data.gender
        role = request.data.role
        email_id = request.data.email_id
        username = request.data.username
        password = request.data.password

        ## write a function to hash a password given by this form and then save it.
        password_hashed = ()

        Customer.objects.create(first_name=first_name,
                                last_name=last_name,
                                phone_number=phone_no,
                                gender=gender,
                                role=role,
                                email_id=email_id,
                                username=username,
                                password=password_hashed)
        return redirect('signin-url')
    

def sign_in_view(request):
    if request.method == 'POST':
        username = request.data.username
        password = request.data.password

        ## query DB username => aadmi hai kya??
        ## agar nahi hai toh return user not exist
        ## agar hai toh match password
        ## first hash the password you got from request then match it with DB
