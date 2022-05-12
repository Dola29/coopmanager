from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import RegisterForm, LoanForm

class RegisterFormSerializer (serializers.ModelSerializer):
    class Meta:
        model = RegisterForm
        fields = "__all__"
        extra_kwargs = {
            'name' : {'required': True},
            'lastname' : {'required': True},
            'payment_method_ic' : {'required': True},
            'inicial_contributions' : {'required': True},
            'payment_method_ic' : {'required': True},
            'payment_method_is' : {'required': True},
            'initial_savings' : {'required': True},
            'phone_number' : {'required': True},
            'email' : {'required': True}
        }
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class LoanFormSerializer (serializers.ModelSerializer):
    class Meta:
        model = LoanForm
        fields = "__all__"
        extra_kwargs = {
            'name' : {'required': True},
            'lastname' : {'required': True},
            'cedula' : {'required': True},
            'monthly_income' : {'required': True},
            'loan_amount' : {'required': True},
            'dob' : {'required': True},
            'phone_number' : {'required': True},
            'email' : {'required': True}
        }
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)