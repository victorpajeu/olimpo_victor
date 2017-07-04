from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import re

class user(AbstractBaseUser, PermissionsMixin):

    #Criando o AVATARS atraves de strings
    DEFAULT = 'deafult'
    ELYSE = 'elyse'
    EVE = 'eve'
    KRISTY = 'kristy'
    LENA = 'lena '
    MARK = 'mark'
    MATTHEW = 'matthew'
    MOLLY = 'molly'
    RACHEL = 'rachel'

    AVATARS  = (
        (DEFAULT, 'deafult'),
        (ELYSE, 'elyse'),
        (EVE , 'eve'),
        (KRISTY, 'kristy'),
        (LENA, 'lena '),
        (MARK, 'mark'),
        (MATTHEW, 'matthew'),
        (MOLLY, 'molly'),
        (RACHEL, 'rachel')

    )
    #limitando nome de usuário através de uma expressão regular
    username = models.CharField('Usuário', max_length=25, unique=True, validators=[
         validators.RegexValidator(
             re.compile('^[\w.@+-]+$'),
             'Informe o nome de usuário válido',
             'Este valor deve conter apenas letras'
             'e os caracteres: @/./+/-/_',
             'ivalid'
         )
         ], help_text = 'Um nome curto que será usado para indentifica-lo de forma única'
    )
    name = models.CharField('Nome', max_length=190)
    email = models.EmailField('Email', unique=True)
    avatar = models.CharField('Avatar', max_length=50, choices=AVATARS, default=DEFAULT)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined =models.DateTimeField('Data de entrada', auto_now_add=True)
    #daqui pra cima so conf o model de usuário

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
