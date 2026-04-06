from rest_framework import serializers
from .models import User, Role


# 1. Definir primero el de la relación "Uno" (Role)
class RoleSerializer(serializers.ModelSerializer):
    # Esto permite ver la lista de usuarios que tienen este rol
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ["id", "name", "description", "users"]


# 2. Definir luego el de "Muchos" (User)
class UserSerializer(serializers.ModelSerializer):
    # Serializador anidado para ver los detalles del rol en lugar de solo el ID
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "dni", "birth_date", "role", "activo"]
