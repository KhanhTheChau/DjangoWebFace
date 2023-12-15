from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.staticfiles.views import serve

from django.db.models import Q


def home(request):
    # Tạo một context chứa dữ liệu cần truyền tới template
    context = {
        'posts': Post.objects.all()
    }
    
    # Sử dụng hàm render để trả về một HttpResponse, render template 'blog/home.html' với dữ liệu trong context
    return render(request, 'blog/home.html', context)

def search(request):
    # Xác định template được sử dụng cho trang kết quả tìm kiếm
    template = 'blog/home.html'

    # Lấy giá trị của tham số 'q' từ query string trong URL
    query = request.GET.get('q')

    # Sử dụng model 'Post' để tìm kiếm các bài đăng có tiêu đề, tác giả, hoặc nội dung chứa từ khóa 'query'
    result = Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))

    # Số lượng bài đăng hiển thị trên mỗi trang kết quả
    paginate_by = 2

    # Tạo context chứa kết quả tìm kiếm để truyền tới template
    context = {'posts': result}

    # Sử dụng hàm render để trả về một HttpResponse, render template 'blog/home.html' với dữ liệu trong context
    return render(request, template, context)

   


# def getfile(request):
#    return serve(request, 'File')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #Xác định tên của biến context được truyền tới template. Trong template, danh sách bài đăng sẽ được truy cập thông qua biến posts.
    ordering = ['-date_posted'] #Sắp xếp danh sách các bài đăng theo thời gian đăng, theo thứ tự giảm dần (từ mới đến cũ). Thuộc tính này chỉ định trường date_posted trong model Post để thực hiện sắp xếp.
    paginate_by = 2 #Xác định số lượng bài đăng hiển thị trên mỗi trang


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self): #Đây là một phương thức được ghi đè từ lớp cha ListView, dùng để xác định queryset (tập dữ liệu) sẽ được sử dụng để hiển thị danh sách. Trong trường hợp này, nó được sử dụng để lấy danh sách bài đăng của một người dùng cụ thể.
        user = get_object_or_404(User, username=self.kwargs.get('username')) #Sử dụng hàm get_object_or_404 để lấy đối tượng người dùng (User) dựa trên tên người dùng (username). Nếu không tìm thấy, sẽ trả về trang 404.
        return Post.objects.filter(author=user).order_by('-date_posted') # Trả về queryset gồm các bài đăng của người dùng đã được xác định ở trên, được sắp xếp theo thời gian đăng giảm dần (từ mới đến cũ).


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Lớp PostCreateView này được thiết kế để hiển thị form tạo mới bài đăng và xử lý quá trình lưu bài đăng mới vào database khi người dùng điền thông tin vào form.
class PostCreateView(LoginRequiredMixin, CreateView):
    # LoginRequiredMixin: Lớp mixin này được sử dụng để yêu cầu người dùng phải đăng nhập trước khi có thể tạo mới một bài đăng. Nếu người dùng chưa đăng nhập, họ sẽ được chuyển hướng đến trang đăng nhập.
    # CreateView: Lớp cơ sở cho việc tạo mới một đối tượng trong database. Nó cung cấp một view chung để xử lý quá trình tạo mới đối tượng.
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file'] # Xác định các trường của form mà người dùng có thể điền thông tin khi tạo mới bài đăng

    def form_valid(self, form):
        # Phương thức này được ghi đè từ lớp cha CreateView và được gọi khi form hợp lệ (tức là không có lỗi)
        form.instance.author = self.request.user # Gán tác giả của bài đăng là người dùng hiện tại (self.request.user). Điều này đảm bảo rằng bài đăng được tạo ra sẽ có tác giả là người dùng đang đăng nhập.
        return super().form_valid(form) # Gọi phương thức form_valid của lớp cha để hoàn thành quá trình lưu bài đăng vào database.


# PostUpdateView là một lớp view trong Django được thiết kế để xử lý quá trình cập nhật bài đăng
# là một view linh hoạt và an toàn, đảm bảo rằng chỉ người dùng đã đăng nhập và là tác giả của bài đăng mới có thể truy cập và cập nhật thông tin của bài đăng.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # LoginRequiredMixin: Lớp mixin yêu cầu người dùng đăng nhập để truy cập view. Nếu người dùng chưa đăng nhập, họ sẽ được chuyển hướng đến trang đăng nhập
    # UserPassesTestMixin: Lớp mixin này cho phép bạn kiểm tra điều kiện bất kỳ trước khi cho phép người dùng truy cập view. Trong trường hợp này, test_func là một phương thức được gọi để kiểm tra xem người dùng có quyền cập nhật bài đăng không.
    # UpdateView: Lớp cơ sở cho việc cập nhật một đối tượng trong database. Nó cung cấp một view chung để xử lý quá trình cập nhật đối tượng.
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Phương thức này kiểm tra xem người dùng có quyền cập nhật bài đăng hay không. Nó lấy đối tượng bài đăng hiện tại thông qua 
    def test_func(self):
        post = self.get_object()
        # self.get_object(), và sau đó kiểm tra xem người dùng hiện tại có phải là tác giả của bài đăng hay không. Nếu là tác giả, phương thức trả về True, cho phép người dùng cập nhật. Nếu không phải, phương thức trả về False, ngăn chặn quyền truy cập.
        if self.request.user == post.author:
            return True
        return False

# PostDeleteView là một lớp view trong Django được sử dụng để xử lý quá trình xóa bài đăng.
# Lớp PostDeleteView này giúp đảm bảo rằng chỉ người dùng đã đăng nhập và là tác giả của bài đăng mới có thể truy cập và xóa bài đăng. Sau khi xóa, họ sẽ được chuyển hướng đến một URL được xác định trong success_url.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    # test_func(self): Phương thức này kiểm tra xem người dùng có quyền xóa bài đăng hay không. Nếu người dùng hiện tại là tác giả của bài đăng, phương thức trả về True, người dùng có quyền xóa. Nếu không phải, phương thức trả về False.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Đây là hàm view chính cho trang "About" của ứng dụng blog. Hàm này nhận một đối tượng request làm tham số, đại diện cho yêu cầu HTTP từ người dùng.
# render một trang "About" và truyền tiêu đề 'About' tới template để hiển thị trên trang đó.
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# python manage.py shell

# from django.contrib.auth.models import User
# from blog.models import Post  

# # Hiển thị tất cả người dùng trong cơ sở dữ liệu
# all_users = User.objects.all()
# print(all_users)

# # Hiển thị tất cả bài đăng trong cơ sở dữ liệu
# all_posts = Post.objects.all()
# print(all_posts)

# # Tìm hoặc tạo một người dùng mới
# user, created = User.objects.get_or_create(username='your_username', defaults={'password': 'your_password'})
# print(f"User created: {created}")

# # Tạo bản ghi mới
# post = Post(
#     title='Your Post Title',
#     file='path/to/your/file.txt',
#     content='Your post content.',
#     author=user
# )

# # Lưu bản ghi vào cơ sở dữ liệu
# post.save()

# # Hiển thị lại tất cả người dùng và bài đăng sau khi thêm vào
# print(User.objects.all())
# print(Post.objects.all())
