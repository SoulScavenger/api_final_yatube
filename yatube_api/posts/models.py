from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import TITLE_SLICE

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:TITLE_SLICE]


class Post(models.Model):
    text = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Сообщество'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:TITLE_SLICE]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публикация'
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return (
            f'Комментарий автора: {self.author} '
            f'к Посту: {self.post} '
            f'Текст: {self.text[:TITLE_SLICE]}'
        )


class Follow(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь'
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
        verbose_name='Подписан на'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
            models.CheckConstraint(
                name='check_user_following',
                check=~models.Q(user=models.F("following")),
            )
        ]

    def __str__(self):
        return (
            f'Пользователь: {self.user} '
            f'Подписан на: {self.following} '
        )
