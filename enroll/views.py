from django.shortcuts import render, HttpResponseRedirect
from .forms import TaskInfo, LoginForm, SignupForm, EditUserProfile, PCForm
from .models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# This function is for Add data and Show Data for todo app
def add_show(request):
    if request.user.is_authenticated: 
        user = request.user 
        print(user)
        if request.method == 'POST':
            fm = TaskInfo(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.user = user
                instance.save()
                fm = TaskInfo()
        else:
            fm = TaskInfo()

        # To retrieve/show data
        shows = Task.objects.filter(user=user)
        return render(request, 'enroll/addandshow.html', {'form':fm, 'show':shows})


# This function is for Edit/Update
def update_task(request, id):
    # On click of Update button the 'if' part will get executed
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        fm = TaskInfo(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Task updated successfully!')
            
    # On click of EDIT button (GET method) 'else' part will get executed 
    else:
        pi = Task.objects.get(pk=id)
        fm = TaskInfo(instance=pi)
    return render(request, 'enroll/updatetask.html', {'id':id, 'form':fm})

# This function is for Delete
def delete_task(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignupForm()
            messages.success(request, 'Congratulations! Registration successful.')
    else:
        form = SignupForm()
    return render(request, 'enroll/signup.html',{'form':form})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in sucessfully!')
                    return HttpResponseRedirect('/addandshow/')
        else:
            form = LoginForm()
        return render(request, 'enroll/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/addandshow/')

# Profile View Function
def user_profile(request):
    if request.user.is_authenticated:
        # For editing and save data in profile page
        if request.method == 'POST':
            form = EditUserProfile(instance=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request, 'Profile Updated!')
                form.save()
        else:
            form = EditUserProfile(instance=request.user)
        return render(request, 'enroll/profile.html', {'name':request.user, 'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Change Password
def user_change_pass(request):
    if request.user.is_authenticated: # If user is logged in execute below line code, if not then go to else part
        if request.method == 'POST':
            form = PCForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Changed Successfully!')
                update_session_auth_hash(request, form.user) # This is for user session redirect to profile (below line code)
                return HttpResponseRedirect('/profile/') # After saving password user will be redirected to profile page.
        else:
            form = PCForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

