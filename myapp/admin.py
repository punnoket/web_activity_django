from django.contrib import admin
from myapp.models import Activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Activity._meta.fields]

admin.site.register(Activity,ActivityAdmin)
