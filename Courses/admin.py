from django.contrib import admin

from Courses.models import Course, Section, CourseComment, SectionComment

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(CourseComment)
admin.site.register(SectionComment)