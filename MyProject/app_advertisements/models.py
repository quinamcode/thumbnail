from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils import timezone

user = get_user_model()
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=64)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('Изображение', upload_to='advertisement')
    user = models.ForeignKey(user, verbose_name='пользователь', on_delete=models.CASCADE, null=True, default=None)

    @admin.display(description='Дата создания')
    def created_date(self):

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span style="color: black; fond-weight: bold";>Сегодня в {created_time}</span>'
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):

        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; fond-weight: bold";>Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price: .2f})>'