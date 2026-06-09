from django.contrib import admin
from .models import Post, Author

# Register the Post model
admin.site.register(Post)

# Register the Author model
admin.site.register(Author)