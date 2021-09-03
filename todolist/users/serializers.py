from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


from users.models import CustomUser, CustomUserRole


# class UserSerializer(HyperlinkedModelSerializer):
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class UsersRoleSerializer(ModelSerializer):
    # user = CustomUserSerializer()

    class Meta:
        model = CustomUserRole
        fields = '__all__'



