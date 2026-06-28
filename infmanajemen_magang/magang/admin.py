from django.contrib import admin

# Register your models here.

from .models import (
    User, Perusahaan, Lowongan, Siswa, GuruPembimbing, 
    Admin, SupervisorPerusahaan, Lamaran, MagangPenempatan, 
    Notifikasi, JurnalHarian, Laporan, Nilai
)


admin.site.register(User)
admin.site.register(Perusahaan)
admin.site.register(Lowongan)
admin.site.register(Siswa)  
admin.site.register(GuruPembimbing)
admin.site.register(Admin)
admin.site.register(SupervisorPerusahaan)
admin.site.register(Lamaran)
admin.site.register(MagangPenempatan)
admin.site.register(Notifikasi)
admin.site.register(JurnalHarian)
admin.site.register(Laporan)
admin.site.register(Nilai)