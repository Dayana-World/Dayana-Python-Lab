from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserEditForm

# Create your userLogin view 
def user_login(request):
    if request.user.is_authenticated == True :
        return redirect('home:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username')) # Save new object
            login(request, user)
            return redirect("home:home")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form})
# Create your userRegister view 
def user_register(request):
    context = {'errors': []} # Dic of errors

    if request.user.is_authenticated == True :
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2: # Check error
            context['errors'].append('passwords are not same') # Error
            return render(request, "account/register.html", context)

        user = User.objects.create(username= username, email= email, password=password1) # Create & save new user
        login(request, user)
        return redirect('home:home')
    return render(request, 'account/register.html', {})

def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user) #baraye namayesh etelaate az ghabl zakhire shode dakhele input ha
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)  # (instance=user) : Displays the user's saved information
        if form.is_valid(): # Save your edit user's detail
            form.save()

    return render(request, 'account/edit.html', {'form': form})

# Create your userLogout view 
def user_logout(request):
    logout(request)
    return redirect('home:home')