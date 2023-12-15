from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# định nghĩa hai hàm sử dụng tín hiệu (signals) của Django để tự động tạo và lưu trữ Profile khi một User được tạo hoặc cập nhật
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# Hàm này được gắn kết với tín hiệu post_save và sẽ được gọi khi một User được lưu.
# Nếu người dùng được tạo mới (created là True), hàm này tạo một Profile mới liên kết với người dùng vừa được tạo.

@receiver(post_save, sender=User)
def save_profile(sender, instance,created, **kwargs):
    instance.profile.save()
    
# Hàm này cũng được gắn kết với tín hiệu post_save và sẽ được gọi khi một User được lưu.
# Nếu người dùng được tạo mới (created là True), hàm này lưu trữ Profile liên kết với người dùng vừa được tạo.


# Trong hàm save_profile, instance.profile sẽ tự động tạo một Profile nếu nó chưa tồn tại, nhờ vào quan hệ OneToOneField giữa User và Profile.