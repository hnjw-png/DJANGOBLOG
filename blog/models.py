from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


SERVICE_CHOICES = (
    ("WEDDING", "BAPTISM"),
    ("EXAM PARTY", "SCHOOL BALL"),
    ("BIRTHDAY PARTY WITH CHEF"),
    ("WORK PARTY", "AFTERWORK FOOD AND DRINKS"),
    ("UNDECIDED OR UNSPECIFIED FOR NOW")
)

TIME_CHOICES = (
    ("2pm-12pm"),
    ("10am-2pm")
    ("10am-10pm")
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="A LOCAL")
    time = models.CharField(max_length=15, choices=TIME_CHOICES, default="3pm")
    
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}" 
