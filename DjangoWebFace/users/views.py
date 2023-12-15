from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
        # Nếu biểu mẫu UserRegisterForm là hợp lệ (is_valid() trả về True), thì người dùng đã cung cấp thông tin đăng ký đúng.
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})



# sử dụng để xử lý trang cá nhân của người dùng, cho phép họ cập nhật thông tin người dùng và hình ảnh đại diện của mình
@login_required
# Đây là decorator của Django (@login_required) được sử dụng để đảm bảo rằng chỉ người dùng đã đăng nhập mới có thể truy cập trang cá nhân. Nếu người dùng chưa đăng nhập, họ sẽ được chuyển hướng đến trang đăng nhập.

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
