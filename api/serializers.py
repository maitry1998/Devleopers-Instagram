from rest_framework import serializers
from projects.models import Project
from projects.models import Project, Tag, Review
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    owner= ProfileSerializer(many=False)
    tags=TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()


    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self, obj):
        review = obj.review_set.all() # here obj is the Project model's object
        serializers = ReviewSerializer(review,many=True)
        return serializers.data

