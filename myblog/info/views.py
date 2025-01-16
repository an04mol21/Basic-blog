from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Data

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        try:
            user = Data.objects.get(username=username)

            # Verify password
            if check_password(password, user.password):
                # Success: Redirect to the blog/home page
                messages.success(request, "Logged in successfully!")
                return redirect('blog/')  # Replace with your blog route
            else:
                # Invalid password
                messages.error(request, "Incorrect password. Please try again.")
        except Data.DoesNotExist:
            # User does not exist
            messages.error(request, "Username does not exist. Please try again.")

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        # if password != re_password:
        #     messages.error(request, "Passwords does not match.")
        #     return redirect('signup')

        if Data.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect('signup')

        hashed_password = make_password(password)
        try:
            user = Data(username=username, password=hashed_password)
            user.save()
            print("DEBUG: User saved successfully:", user)  # Debug log
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            print("DEBUG: Error saving user:", e)  # Debug log
            messages.error(request, f"Error creating account: {e}")
            return redirect('signup')

    return render(request, "signup.html")


def blog(request):
    return render(request, "blog.html")