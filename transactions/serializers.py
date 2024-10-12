from rest_framework import serializers

from transactions.models import User, Transaction


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        model = User
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'category', 'description', 'date']

