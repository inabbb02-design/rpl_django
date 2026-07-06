"""
URL configuration for infmanajemen_magang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from infmanajemen_magang import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home),

    # User
    path('user/', views.user),
    path('user/buat/', views.user_buat),
    path('user/<int:id>/', views.user_detail),
    path('user/<int:id>/edit/', views.user_edit),
    path('user/<int:id>/hapus/', views.user_hapus),

    # Siswa
    path('siswa/', views.siswa),
    path('siswa/buat/', views.siswa_buat),
    path('siswa/<int:id>/', views.siswa_detail),
    path('siswa/<int:id>/edit/', views.siswa_edit),
    path('siswa/<int:id>/hapus/', views.siswa_hapus),

    # Guru
    path('guru/', views.guru),
    path('guru/buat/', views.guru_buat),
    path('guru/<int:id>/', views.guru_detail),
    path('guru/<int:id>/edit/', views.guru_edit),
    path('guru/<int:id>/hapus/', views.guru_hapus),

    # Admin
    path('admin-data/', views.admin_data),
    path('admin-data/buat/', views.admin_buat),
    path('admin-data/<int:id>/', views.admin_detail),
    path('admin-data/<int:id>/edit/', views.admin_edit),
    path('admin-data/<int:id>/hapus/', views.admin_hapus),

    # Supervisor
    path('supervisor/', views.supervisor),
    path('supervisor/buat/', views.supervisor_buat),
    path('supervisor/<int:id>/', views.supervisor_detail),
    path('supervisor/<int:id>/edit/', views.supervisor_edit),
    path('supervisor/<int:id>/hapus/', views.supervisor_hapus),

    # Perusahaan
    path('perusahaan/', views.perusahaan),
    path('perusahaan/buat/', views.perusahaan_buat),
    path('perusahaan/<int:id>/', views.perusahaan_detail),
    path('perusahaan/<int:id>/edit/', views.perusahaan_edit),
    path('perusahaan/<int:id>/hapus/', views.perusahaan_hapus),

    # Lowongan
    path('lowongan/', views.lowongan),
    path('lowongan/buat/', views.lowongan_buat),
    path('lowongan/<int:id>/', views.lowongan_detail),
    path('lowongan/<int:id>/edit/', views.lowongan_edit),
    path('lowongan/<int:id>/hapus/', views.lowongan_hapus),

    # Lamaran
    path('lamaran/', views.lamaran),
    path('lamaran/buat/', views.lamaran_buat),
    path('lamaran/<int:id>/', views.lamaran_detail),
    path('lamaran/<int:id>/edit/', views.lamaran_edit),
    path('lamaran/<int:id>/hapus/', views.lamaran_hapus),

    # Magang
    path('magang/', views.magang),
    path('magang/buat/', views.magang_buat),
    path('magang/<int:id>/', views.magang_detail),
    path('magang/<int:id>/edit/', views.magang_edit),
    path('magang/<int:id>/hapus/', views.magang_hapus),

    # Jurnal
    path('jurnal/', views.jurnal),
    path('jurnal/buat/', views.jurnal_buat),
    path('jurnal/<int:id>/', views.jurnal_detail),
    path('jurnal/<int:id>/edit/', views.jurnal_edit),
    path('jurnal/<int:id>/hapus/', views.jurnal_hapus),

    # Laporan
    path('laporan/', views.laporan),
    path('laporan/buat/', views.laporan_buat),
    path('laporan/<int:id>/', views.laporan_detail),
    path('laporan/<int:id>/edit/', views.laporan_edit),
    path('laporan/<int:id>/hapus/', views.laporan_hapus),

    # Nilai
    path('nilai/', views.nilai),
    path('nilai/buat/', views.nilai_buat),
    path('nilai/<int:id>/', views.nilai_detail),
    path('nilai/<int:id>/edit/', views.nilai_edit),
    path('nilai/<int:id>/hapus/', views.nilai_hapus),

    # Notifikasi
    path('notifikasi/', views.notifikasi),
    path('notifikasi/buat/', views.notifikasi_buat),
    path('notifikasi/<int:id>/', views.notifikasi_detail),
    path('notifikasi/<int:id>/edit/', views.notifikasi_edit),
    path('notifikasi/<int:id>/hapus/', views.notifikasi_hapus),
]
