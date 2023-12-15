from django.contrib import admin

# Register your models here.

# sử dụng trong file admin.py của ứng dụng Django để đăng ký model Profile với trang quản trị. Khi bạn đăng ký một model, nó sẽ xuất hiện trong giao diện quản trị Django, giúp bạn quản lý và xem nhanh các bản ghi của model đó.
from .models import Profile

admin.site.register(Profile)

# Trong trang quản trị, bạn sẽ có thể thêm, sửa đổi và xóa các bản ghi của model Profile, cũng như xem thông tin chi tiết về từng bản ghi.