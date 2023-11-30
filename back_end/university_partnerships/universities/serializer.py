from rest_framework import serializers
from .models import University

class UniversityPartnerSerializer(serializers.ModelSerializer):
    university = serializers.PrimaryKeyRelatedField(many = False, queryset=University.objects.all())

    class Meta:
        model = University
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):

    universityPartner = UniversityPartnerSerializer(many=True)

    class Meta:
        model = University
        fields = ["name", "url", "address", "partner"]

    def create(self, validated_data):
        university_partner_data = validated_data.pop('partner')
        new_university = University.objects.create(**validated_data)
        for uni in university_partner_data:
            new_university.partner_universities.add(uni.id)
        new_university.save()
        return new_university