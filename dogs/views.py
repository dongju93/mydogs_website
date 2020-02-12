from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from dogs.models import *
from django.contrib.auth.decorators import login_required
from tagging.views import TaggedObjectList
from django.db.models import Sum, Avg, Count, Subquery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, AccessMixin

@login_required
def info_list(request):
    # mydog 에서 objects 필터를, owner 필드를 request 받은 user 로 적용.
    # 로그인 한 이용자의 mydogs object 만 return
    infos = mydogs.objects.filter(owner=request.user)

    return render(request, 'dogs/infolist.html', {'infos': infos})


class infoCreate(LoginRequiredMixin, CreateView):
    model = mydogs
    fields = ['names', 'dogpic', 'birth', 'weight', 'species', 'gender', 'neutral', 'registernumber', 'dhppl', 'corona',
              'kennel', 'rabies', 'heartworm']
    template_name = 'dogs/infocreate.html'

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        # 입력한 값들을 검증 한 후 에러가 없다면 하단 if 문 실행 (DB 저장)
        if form.is_valid():
            form.instance.save()
            return redirect('/dogs/info/')
        else:
            return self.render_to_response({'form': form})

class infoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = mydogs
    success_url = '/dogs/info/'
    fields = ['names', 'dogpic', 'birth', 'weight', 'species', 'gender', 'neutral', 'registernumber', 'dhppl', 'corona',
              'kennel', 'rabies', 'heartworm']
    template_name = 'dogs/infoupdate.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class infoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = mydogs
    success_url = '/dogs/info/'
    template_name = 'dogs/infodelete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class PostTOL(LoginRequiredMixin, TaggedObjectList):
    model = daily
    template_name = 'dogs/taglist.html'


@login_required
def daily_list(request):
    daily_list = daily.objects.filter(owner=request.user)
    paginator = Paginator(daily_list, 30)  # Show 20 contacts per page

    page = request.GET.get('page')

    try:
        dailys = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dailys = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dailys = paginator.page(paginator.num_pages)

    return render(request, 'dogs/dailylist.html', {'dailys': dailys})

class dailyCreate(LoginRequiredMixin, CreateView):

    model = daily
    fields = ['names', 'walkcount', 'walktime', 'foodamount', 'snackcount', 'remarks', 'statustrace', 'tag']
    template_name = 'dogs/dailycreate.html'

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        # 입력한 값들을 검증 한 후 에러가 없다면 하단 if 문 실행 (DB 저장)
        if form.is_valid():
            form.instance.save()
            return redirect('/dogs/daily/')
        else:
            return self.render_to_response({'form': form})

class dailyDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = daily
    template_name = 'dogs/dailydetail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class dailyUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = daily
    fields = ['names', 'walkcount', 'walktime', 'foodamount', 'snackcount', 'remarks', 'statustrace', 'tag']
    template_name = 'dogs/dailyupdate.html'
    success_url = '/dogs/daily/'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class dailyDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = daily
    success_url = '/'
    template_name = 'dogs/dailydelete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

@login_required
def chartt(request):

    ##### 견종별 몸무게 및 숫자 #####

    # 대형
    afghanAVG = mydogs.objects.filter(species='Afghan Hound').aggregate(Avg('weight'), Count('species'))
    pitbullAVG = mydogs.objects.filter(species='American Pitbull Terrier').aggregate(Avg('weight'), Count('species'))
    bloodAVG = mydogs.objects.filter(species='Bloodhound').aggregate(Avg('weight'), Count('species'))
    chowAVG = mydogs.objects.filter(species='Chow Chow').aggregate(Avg('weight'), Count('species'))
    dalmatianAVG = mydogs.objects.filter(species='Dalmatian').aggregate(Avg('weight'), Count('species'))
    dutchAVG = mydogs.objects.filter(species='Dutch Shepherd').aggregate(Avg('weight'), Count('species'))
    englishAVG = mydogs.objects.filter(species='English Foxhound').aggregate(Avg('weight'), Count('species'))
    gershepherdAVG = mydogs.objects.filter(species='German Shepherd').aggregate(Avg('weight'), Count('species'))
    goldadorAVG = mydogs.objects.filter(species='Goldador').aggregate(Avg('weight'), Count('species'))
    goldenAVG = mydogs.objects.filter(species='Golden Retriever').aggregate(Avg('weight'), Count('species'))
    daneAVG = mydogs.objects.filter(species='Great Dane').aggregate(Avg('weight'), Count('species'))
    pyreneesAVG = mydogs.objects.filter(species='Great Pyrenees').aggregate(Avg('weight'), Count('species'))
    houndAVG = mydogs.objects.filter(species='Greyhound').aggregate(Avg('weight'), Count('species'))
    samoyedAVG = mydogs.objects.filter(species='Samoyed').aggregate(Avg('weight'), Count('species'))
    huskyAVG = mydogs.objects.filter(species='Siberian Husky').aggregate(Avg('weight'), Count('species'))
    airedaleAVG = mydogs.objects.filter(species='Airedale Terrier').aggregate(Avg('weight'), Count('species'))
    appenzellerAVG = mydogs.objects.filter(species='Appenzeller Sennenhund').aggregate(Avg('weight'), Count('species'))
    bulldogAVG = mydogs.objects.filter(species='Bulldog').aggregate(Avg('weight'), Count('species'))
    bigAVG = mydogs.objects.filter(species='Afghan Hound'and'American Pitbull Terrier'and'Bloodhound'
                                   and 'Bulldog' and 'Chow Chow' and 'Dalmatian' and 'Dutch Shepherd' and
                                           'English Foxhound' and 'Appenzeller Sennenhund' and 'German Shepherd' and 'Goldador'
                                           and 'Golden Retriever' and 'Great Dane' and 'Great Pyrenees' and 'Greyhound'
                                           and 'Samoyed' and 'Siberian Husky' and 'Airedale Terrier').aggregate(Avg('weight'), Count('species'))

    # 중형
    eskimoAVG = mydogs.objects.filter(species='American Eskimo Dog').aggregate(Avg('weight'), Count('species'))
    cockerAVG = mydogs.objects.filter(species='Cocker Spaniel').aggregate(Avg('weight'), Count('species'))
    corgiAVG = mydogs.objects.filter(species='Pembroke Welsh Corgi').aggregate(Avg('weight'), Count('species'))
    borderAVG = mydogs.objects.filter(species='Border Collie').aggregate(Avg('weight'), Count('species'))
    pinscherAVG = mydogs.objects.filter(species='German Pinscher').aggregate(Avg('weight'), Count('species'))
    middleAVG = mydogs.objects.filter(species='American Eskimo Dog' and 'German Pinscher'
                                              and 'Border Collie' and 'Cocker Spaniel' and 'Pembroke Welsh Corgi').aggregate(Avg('weight'), Count('species'))

    # 소형
    australianAVG = mydogs.objects.filter(species='Australian Terrier').aggregate(Avg('weight'), Count('species'))
    beagleAVG = mydogs.objects.filter(species='Beagle').aggregate(Avg('weight'), Count('species'))
    bichonAVG = mydogs.objects.filter(species='Bichon Frise').aggregate(Avg('weight'), Count('species'))
    bostonAVG = mydogs.objects.filter(species='Boston Terrier').aggregate(Avg('weight'), Count('species'))
    chiAVG = mydogs.objects.filter(species='Chihuahua').aggregate(Avg('weight'), Count('species'))
    dachhundAVG = mydogs.objects.filter(species='Dachshund').aggregate(Avg('weight'), Count('species'))
    poodleAVG = mydogs.objects.filter(species='Poodle').aggregate(Avg('weight'), Count('species'))
    pugAVG = mydogs.objects.filter(species='Pug').aggregate(Avg('weight'), Count('species'))
    tzuAVG = mydogs.objects.filter(species='Shih Tzu').aggregate(Avg('weight'), Count('species'))
    yorkAVG = mydogs.objects.filter(species='Yorkshire Terrier').aggregate(Avg('weight'), Count('species'))
    malteseAVG = mydogs.objects.filter(species='Maltese').aggregate(Avg('weight'), Count('species') and Count('species'))
    pomeAVG = mydogs.objects.filter(species='Pomeranian').aggregate(Avg('weight'), Count('species'))
    smallAVG = mydogs.objects.filter(species='Australian Terrier' and 'Beagle' and 'Bichon Frise' and 'Boston Terrier'
                                                and 'Chihuahua' and 'Dachshund' and 'Poodle' and 'Pug' and 'Shih Tzu' and
                                                'Yorkshire Terrier' and 'Maltese' and 'Pomeranian').aggregate(Avg('weight'), Count('species'))

    # 내 반려견
    mymy = mydogs.objects.filter(owner=request.user)
    janM = daily.objects.filter(owner=request.user, created__range=["2019-01-01", "2019-01-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    febM = daily.objects.filter(owner=request.user, created__range=["2019-02-01", "2019-02-28"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    marM = daily.objects.filter(owner=request.user, created__range=["2019-03-01", "2019-03-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    aprM = daily.objects.filter(owner=request.user, created__range=["2019-04-01", "2019-04-30"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    mayM = daily.objects.filter(owner=request.user, created__range=["2019-05-01", "2019-05-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    junM = daily.objects.filter(owner=request.user, created__range=["2019-06-01", "2019-06-30"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    julM = daily.objects.filter(owner=request.user, created__range=["2019-07-01", "2019-07-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    augM = daily.objects.filter(owner=request.user, created__range=["2019-08-01", "2019-08-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    sepM = daily.objects.filter(owner=request.user, created__range=["2019-09-01", "2019-09-30"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    octM = daily.objects.filter(owner=request.user, created__range=["2019-10-01", "2019-10-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    novM = daily.objects.filter(owner=request.user, created__range=["2019-11-01", "2019-11-30"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))
    decM = daily.objects.filter(owner=request.user, created__range=["2019-12-01", "2019-12-31"]).aggregate(Avg('foodamount'), Avg('snackcount'), Avg('walkcount'))

    # 전체 평균
    janMA = daily.objects.filter(created__range=["2019-01-01", "2019-01-31"]).aggregate(Avg('walkcount'))
    febMA = daily.objects.filter(created__range=["2019-02-01", "2019-02-28"]).aggregate(Avg('walkcount'))
    marMA = daily.objects.filter(created__range=["2019-03-01", "2019-03-31"]).aggregate(Avg('walkcount'))
    aprMA = daily.objects.filter(created__range=["2019-04-01", "2019-04-30"]).aggregate(Avg('walkcount'))
    mayMA = daily.objects.filter(created__range=["2019-05-01", "2019-05-31"]).aggregate(Avg('walkcount'))
    junMA = daily.objects.filter(created__range=["2019-06-01", "2019-06-30"]).aggregate(Avg('walkcount'))
    julMA = daily.objects.filter(created__range=["2019-07-01", "2019-07-31"]).aggregate(Avg('walkcount'))
    augMA = daily.objects.filter(created__range=["2019-08-01", "2019-08-31"]).aggregate(Avg('walkcount'))
    sepMA = daily.objects.filter(created__range=["2019-09-01", "2019-09-30"]).aggregate(Avg('walkcount'))
    octMA = daily.objects.filter(created__range=["2019-10-01", "2019-10-31"]).aggregate(Avg('walkcount'))
    novMA = daily.objects.filter(created__range=["2019-11-01", "2019-11-30"]).aggregate(Avg('walkcount'))
    decMA = daily.objects.filter(created__range=["2019-12-01", "2019-12-31"]).aggregate(Avg('walkcount'))


    return render(request, 'dogs/chart.html', {'mymy': mymy,
                                               'afghanAVG': afghanAVG, 'pitbullAVG': pitbullAVG,
                                               'bloodAVG': bloodAVG, 'borderAVG': borderAVG, 'chowAVG': chowAVG,
                                               'dalmatianAVG': dalmatianAVG, 'dutchAVG': dutchAVG, 'englishAVG': englishAVG,
                                               'pinscherAVG': pinscherAVG, 'gershepherdAVG': gershepherdAVG, 'goldadorAVG': goldadorAVG,
                                               'goldenAVG': goldenAVG, 'daneAVG': daneAVG, 'pyreneesAVG': pyreneesAVG,
                                               'houndAVG': houndAVG, 'samoyedAVG': samoyedAVG, 'huskyAVG': huskyAVG,
                                               'bigAVG': bigAVG,
                                               'airedaleAVG': airedaleAVG, 'eskimoAVG': eskimoAVG, 'appenzellerAVG': appenzellerAVG,
                                               'bulldogAVG': bulldogAVG, 'cockerAVG': cockerAVG, 'corgiAVG': corgiAVG,
                                               'middleAVG': middleAVG,
                                               'australianAVG': australianAVG, 'beagleAVG': beagleAVG, 'bichonAVG': bichonAVG,
                                               'bostonAVG': bostonAVG, 'chiAVG': chiAVG, 'dachhundAVG': dachhundAVG,
                                               'poodleAVG': poodleAVG, 'pugAVG': pugAVG, 'tzuAVG': tzuAVG,
                                               'yorkAVG': yorkAVG, 'malteseAVG': malteseAVG, 'pomeAVG': pomeAVG,
                                               'smallAVG': smallAVG,
                                               'janM': janM, 'febM': febM, 'marM': marM, 'aprM': aprM, 'mayM': mayM, 'junM': junM, 'julM': julM, 'augM': augM,
                                               'janMA': janMA, 'febMA': febMA, 'marMA': marMA, 'aprMA': aprMA, 'mayMA': mayMA, 'junMA': junMA, 'julMA': julMA, 'augMA': augMA })