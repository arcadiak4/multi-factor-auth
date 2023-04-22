from . import forms
import os

def SignInUser(request):
    form = forms.SignInForm()
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(
                request, "multifactor/signin_success.html", {"username": form.cleaned_data['username']}
            )
    return render(
        request, 'multifactor/signin.html', context={'form': form}
    )

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

def LoginUser(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # check user identifiers in the database
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            # check if user is in the database
            if user is not None:
                # attach authenticated user to the current session
                login(request, user)
                # if the user has activated the MFA
                current_user = request.user
                if str(User.objects.filter(username=current_user).values("mfa_key").first()['mfa_key']) != '':
                    # print("User has activated MFA and must enter the OTP.")
                    # render the MFA page
                    return render(request, 'multifactor/mfa.html')
                # the login has succeed
                return render(request, 'multifactor/login_success.html', {"username": form.cleaned_data['username']})
            
            else:
                form.add_error("username", 'Wrong username and/or password')

    return render(request, 'multifactor/login.html', context={'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
@login_required
def LogOutUser(request):
    # print(request.user.is_authenticated)
    logout(request)
    # print(request.user.is_authenticated)
    return redirect('login')

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import pyotp
from .models import User

def qrcode_gen(request):
    # generate the secret common key
    secret_key = pyotp.random_base32()
    # print("Secret key:", secret_key)
    
    # save secret key in plaintext in the database
    current_user = request.user
    # print ("Current user:", current_user.username)
   
    # generate TOTP
    totp_auth = pyotp.TOTP(secret_key).provisioning_uri(name='multi-factor-auth',issuer_name='Groupe_7')
    # print(totp_auth)

    # generate the corresponding QR Code
    qrcode = make(totp_auth)

    # save the QR Code generated image in the root folder named /media
    qrcode.save(os.path.join(settings.MEDIA_ROOT, "qr_auth.png"))

    # print the current OTP
    # shared_secret = pyotp.TOTP(secret_key)
    # print("Shared secret:", shared_secret.now())
    
    return render(request, 'multifactor/qrcode.html', {'img_name': 'qr_auth.png', 'secret_key': secret_key})

def qrcode_check(request):
    current_user = request.user
    User.objects.filter(username=current_user).update(mfa_key=request.POST.get('secret_key'))

    return render(request, 'multifactor/qrcode_check.html', {})

def check_mfa(request):
    if request.method == 'POST':
        totp_input = request.POST.get('totp_input')
        
        # retrieve the current OTP from the current User
        current_user = request.user
        mfa_key = User.objects.filter(username=current_user).values("mfa_key").first()['mfa_key']

        # test the validity of the OTP (client OTP and the server OTP)
        shared_secret = pyotp.TOTP(mfa_key)
        if str(totp_input) == str(shared_secret.now()):
            return render(request, 'multifactor/login_success.html', {"username": current_user.username})
    
    return render(request, 'multifactor/mfa_failed.html')
