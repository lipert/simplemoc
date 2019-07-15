from .models import Courses

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug' , 'start_date' , 'created_at']
    search_fields = ['name','description']



admin.site.register(Courses,CourseAdmin)
