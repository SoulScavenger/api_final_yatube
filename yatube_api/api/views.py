from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly, ReadOnlyComments
from api.serializers import (
    CommentSerializer,
    FollowCreateSerializer,
    FollowListSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post, User


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_serializer_class(self):
        if self.action == 'create':
            return FollowCreateSerializer
        return FollowListSerializer

    def get_user_instance(self):
        return self.request.user

    def get_following_instance(self):
        return User.objects.all().filter(
            username=self.request.data.get('following')
        ).first()

    def perform_create(self, serializer):
        serializer.save(
            user=self.get_user_instance(),
            following=self.get_following_instance()
        )

    def get_queryset(self):
        return self.get_user_instance().users.all()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return (ReadOnlyComments(),)

        return super().get_permissions()

    def get_post_instance(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self, *args, **kwargs):
        return self.get_post_instance().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post_instance()
        )
