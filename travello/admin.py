from django.contrib import admin
from .models import Package, Vendor

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'approved')  # Show approval status in admin
    list_filter = ('approved',)
    actions = ['approve_packages']

    def approve_packages(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected packages have been approved.")

    approve_packages.short_description = "Approve selected packages"

admin.site.register(Package, PackageAdmin)
admin.site.register(Vendor)
