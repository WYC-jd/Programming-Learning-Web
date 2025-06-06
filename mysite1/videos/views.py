from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest
from .forms import SignUpForm

def home(request):
    videos = Video.objects.all().order_by('uploaded_at')[:5]
    return render(request, 'home.html', {'videos': videos})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            # 验证用户
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                # 用户验证成功，登录
                login(request, user)
                return redirect('video_list')  # 登录成功后重定向到视频列表
            else:
                # 用户名或密码错误
                return HttpResponse('无效的凭据')
        else:
            return HttpResponseBadRequest('请提供用户名和密码')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)  # 注销用户
    return redirect('login')  # 重定向到登录页面


from django.contrib.auth.decorators import login_required
from .models import Video, Like, Comment
from .forms import VideoForm

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

@login_required
def video_list(request):
    categories = Video.CATEGORY_CHOICES  # 获取所有分类
    category_filter = request.GET.get('category', '')  # 获取选择的分类
    search_query = request.GET.get('search', '')  # 获取搜索关键字

    
    # 根据分类和搜索过滤视频
    if category_filter:
        # 如果选择了分类，筛选该分类的视频
        title = "视频列表：" + category_filter
        videos = Video.objects.filter(category=category_filter)
    else:
        # 如果没有选择分类，显示所有视频
        title = "主页"
        videos = Video.objects.all()

    if search_query:
        # 如果有搜索关键字，进一步筛选标题包含搜索内容的视频
        videos = videos.filter(title__icontains=search_query)
    

    return render(request, 'video_list.html', {
    'videos': videos,
    'categories': categories,
    'category': category_filter,
    'search_query': search_query,
    'title': title
})

@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    like, created = Like.objects.get_or_create(video=video, user=request.user) 

    if not created:
        # 用户已经点赞过，删除点赞
        like.delete()

    # 获取分类参数
    category = request.POST.get('category', '') 

    if category[:1] == 'C':
        return redirect(f'/videos/video_list/?category=C%2B%2B') 
    # 重定向回当前分类页面，保留分类参数
    else:
        return redirect(f'/videos/video_list/?category={category}')

@login_required
def comment_video(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(video=video, user=request.user, content=content)
    return redirect('video_list')  # 或重定向到视频详情页
    
@login_required
def announcement(request):
    return render(request, 'announcement.html')