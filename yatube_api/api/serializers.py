from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post', )
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class FollowCreateSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        request = self.context.get("request")
        user = request.user
        following = User.objects.filter(
            username=request.data.get('following')
        ).first()

        if not following:
            raise serializers.ValidationError('Пользователя не существует...')

        if user == following:
            raise serializers.ValidationError('Нельзя подписаться на себя...')

        is_subscribe_in_table = Follow.objects.select_related(
            'user', 'following'
        ).filter(user=user, following=following)

        if is_subscribe_in_table:
            raise serializers.ValidationError('Подписка уже оформлена...')

        return data


class FollowListSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow
