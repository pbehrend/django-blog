from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


class CategoryInline(admin.StackedInline):
    model = Post.category.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
