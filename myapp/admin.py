from django.contrib import admin
from myapp.models import Activity, Vote

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Activity._meta.fields]

admin.site.register(Activity,ActivityAdmin)

class VoteAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Vote._meta.fields]

admin.site.register(Vote,VoteAdmin)
