import random
from django.utils.text import slugify
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
# ------------------STREAMING PLATFORMS----------#
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            while True:
                if StreamPlatform.objects.filter(slug=self.slug).exists():
                    self.slug = f"{self.slug}{random.randint(1,5)}"
                    print('i am here')
                    continue
                break
        super(StreamPlatform, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} | {self.slug}"

# ------------------Watch------------------------#
class Show(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='show')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Show, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# ------------------Review------------------------#
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(default=True)
    Show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='reviews')
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating:{int(self.rating)} | Movie:{self.Show.title}" 