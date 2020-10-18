from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm)
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from users.tokens import account_activation_token
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login
from django.http import HttpResponse
from django import forms
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
       
        if form.is_valid():
            user = form.save()
            
            user.refresh_from_db()

            user.profile.category=form.cleaned_data.get('category')
            user.profile.age=form.cleaned_data.get('age')
            user.profile.email=form.cleaned_data.get('email')
            user.profile.qualification=form.cleaned_data.get('qualification')
            user.profile.occupation=form.cleaned_data.get('occupation')
            user.profile.expertise=form.cleaned_data.get('expertise')
            user.profile.Current_Projects=form.cleaned_data.get('Current_Projects')
            user.profile.duration=form.cleaned_data.get('duration')
            user.profile.sponsorship=form.cleaned_data.get('sponsorship')
            user.profile.Completed_project=form.cleaned_data.get('Completed_project')
            user.profile.Year_of_Completion=form.cleaned_data.get('Year_of_Completion')
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Scienteract Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
         
    else:
        form = UserRegisterForm()
       
    context = {
        'form': form,
        
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'users/model_form_upload.html', {
        'form': form
    })

def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        messages.success(request, 'Your account has been created! You are now able to log in')
        return render(request, 'users/account_activation_invalid.html')
    else:
        messages.success(request, 'Your account has been created! You are now able to log in')
        return redirect('login')

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)
        
