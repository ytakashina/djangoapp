from django.db import models


# Create your models here.
class Inquiry(models.Model):
    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    JOB_CHOICES = (
        (1, '会社員'),
        (2, 'フリーター'),
        (3, '学生'),
    )
    user_name = models.CharField("お名前", max_length=20)
    email = models.EmailField("メールアドレス")
    sex = models.IntegerField("性別", choices=SEX_CHOICES, default=1)
    job = models.IntegerField("職業", choices=JOB_CHOICES)
    inquiry_text = models.TextField("問い合わせ内容", max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.user_name
