from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tagging.fields import TagField


class mydogs(models.Model) :
    # user.id 를 받아와
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dogs')

    # 강아지 세부정보 입력필드
    names = models.CharField(max_length=100)
    dogpic = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    birth = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    species = models.CharField(max_length=50)
    registernumber = models.IntegerField()

    # 중성화
    gender = models.CharField(max_length=15)
    neutral = models.BooleanField()

    # 예방접종 필드
    dhppl = models.DateField(blank=True, null=True)
    corona = models.DateField(blank=True, null=True)
    kennel = models.DateField(blank=True, null=True)
    rabies = models.DateField(blank=True, null=True)
    heartworm = models.DateField(blank=True, null=True)

    # 정보 작성 일자 및 업데이트 날짜 표기
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.owner.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('/', args=[str(self.id)])


class daily(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_daily')

    names = models.CharField(max_length=100)

    # 일기 주요부분
    walkcount = models.IntegerField()
    walktime = models.TimeField(blank=True, null=True)
    foodamount = models.DecimalField(max_digits=10, decimal_places=2)
    snackcount = models.DecimalField(max_digits=10, decimal_places=2)

    # 임의 작성 필드
    remarks = models.TextField(blank=True, null=True)
    statustrace = models.TextField(blank=True, null=True)

    # 정보 작성 일자 및 업데이트 날짜 표기
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tag = TagField()

    class Meta:
        ordering = ['-updated']

        def __str__(self):
            return self.owner.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
