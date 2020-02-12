from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from photo.models import Photo
from tagging.views import TaggedObjectList
from django.http import JsonResponse
from django.views.decorators.http import require_POST


class PostTOL(TaggedObjectList):
    model = Photo
    template_name = 'photo/taglist.html'

@login_required
def photo_list(request):
    photos_list = Photo.objects.all()

    paginator = Paginator(photos_list, 5)
    page = request.POST.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    if request.is_ajax():  # Ajax request 여부 확인
        return render(request, 'photo/post_list_ajax.html', {
            'photos': photos
        })

    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('photo:tagged_object_list', tag)

    return render(request, 'photo/list.html', {'photos': photos})

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text', 'tag']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/photo')
        else:
            return self.render_to_response({'form': form})

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/detail.html'

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/photo'
    template_name = 'photo/delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text', 'tag']
    template_name = 'photo/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

@login_required
@require_POST
def post_like(request):

    pk = request.POST.get('pk', None)
    post = get_object_or_404(Photo, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    return JsonResponse(data={'like_count': post.like_count, 'message': message,
                              }, json_dumps_params={'ensure_ascii': True}, safe=False)