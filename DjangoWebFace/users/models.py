from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Sử dụng để lưu trữ thông tin cá nhân của người dùng, bao gồm hình ảnh đại diện
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Trường OneToOneField tương ứng với một người dùng (User). Mỗi Profile được liên kết với một và chỉ một người dùng
    # on_delete=models.CASCADE đặt quy tắc xóa: khi người dùng bị xóa, Profile của họ cũng sẽ bị xóa.
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Trường ImageField để lưu trữ hình ảnh đại diện của người dùng. Nó sử dụng thư mục profile_pics để lưu trữ hình ảnh và mặc định là default.jpg nếu người dùng chưa có hình ảnh.
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        # đảm bảo rằng hình ảnh đại diện của người dùng không quá lớn, điều này có thể hữu ích để tối ưu hóa kích thước và tốc độ tải trang.