from django.contrib import admin
from courses.models import Category, Course, Lesson
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):


    content = forms.CharField(widget=CKEditorUploadingWidget)


    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'create_date']
    search_fields = ['subject']
    form= LessonForm
    list_display = ['id', 'subject', 'create_date']
    readonly_fields = ['avatar']

    def avatar(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)

# Register your models here.
