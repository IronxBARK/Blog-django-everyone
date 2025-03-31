from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    particular = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    blog = models.Manager()
    slug = models.SlugField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Blog Entries'
        ordering = ['-date']  # Order by newest first
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
