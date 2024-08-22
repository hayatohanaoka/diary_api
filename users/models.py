from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password='', **fields):
        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('ユーザー名'),
        max_length=20,
        help_text=_('20字以内かつ、使用可能記号は「@/./+/-/_」のみ'),
        validators=[username_validator]
    )
    email = models.EmailField(
        _('メールアドレス'),
        blank=True,
        unique=True,
        error_messages={
            'unique': _('このユーザー名は既に使用されています。'),
        }
    )
    nickname = models.CharField(
        _('ニックネーム'),
        max_length=20,
        blank=True
    )
    is_superuser = models.BooleanField(
        _('管理者'),
        default=False
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
    )
    is_active = models.BooleanField(
        _('使用中フラグ'),
        default=True
    )
    date_joined = models.DateTimeField(_('追加日'), default=timezone.now)
    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'tbl_users'
        verbose_name = _('ユーザー')
        verbose_name_plural = _('ユーザー管理')
