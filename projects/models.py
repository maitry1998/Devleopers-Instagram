from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length= 200)
    description = models.TextField(null = True,blank = True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpeg")
    demo_link = models.CharField(max_length= 200,null = True,blank = True)
    source_link = models.CharField(max_length = 2000,null = True, blank = True)
    tags = models.ManyToManyField('Tag', blank=False)
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_Ratio = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-vote_Ratio','-vote_total','title']


    @property
    def reviewrs(self):
        reviews= self.review_set.all().values_list('owner__id',flat=True) # we did set here because this is called from project model
        return reviews

    # get all the project's vote count
    @property
    def getVoteCount(self):
        reviews= self.review_set.all() # we did set here because this is called from project model
        upvotes=reviews.filter(value="up").count()
        totalVotes=reviews.count()
        ratio = (upvotes/totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_Ratio = ratio

        self.save()
    
class Review(models.Model):

    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null = True,blank = True)
    value = models.CharField(max_length= 200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value
    



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name
    

