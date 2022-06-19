from django.contrib import admin
from .models import Profile,Post, Puzzle, Question

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Puzzle)