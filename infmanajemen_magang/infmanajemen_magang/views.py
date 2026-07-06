from django.shortcuts import render

# ==========================
# HOME
# ==========================

def home(request):
    return render(request, 'home.html')


# ==========================
# USER
# ==========================

def user(request):
    return render(request, 'user/index.html',)

def user_buat(request):
    return render(request, 'user/tambah.html')

def user_detail(request, id):
    return render(request, 'user/detail.html', {'id': id})

def user_edit(request, id):
    return render(request, 'user/edit.html', {'id': id})

def user_hapus(request, id):
    return render(request, 'user/hapus.html', {'id': id})


# ==========================
# SISWA
# ==========================

def siswa(request):
    return render(request, 'siswa/index.html')

def siswa_buat(request):
    return render(request, 'siswa/tambah.html')

def siswa_detail(request, id):
    return render(request, 'siswa/detail.html', {'id': id})

def siswa_edit(request, id):
    return render(request, 'siswa/edit.html', {'id': id})

def siswa_hapus(request, id):
    return render(request, 'siswa/hapus.html', {'id': id})


# ==========================
# GURU
# ==========================

def guru(request):
    return render(request, 'guru/index.html')

def guru_buat(request):
    return render(request, 'guru/tambah.html')

def guru_detail(request, id):
    return render(request, 'guru/detail.html', {'id': id})

def guru_edit(request, id):
    return render(request, 'guru/edit.html', {'id': id})

def guru_hapus(request, id):
    return render(request, 'guru/hapus.html', {'id': id})


# ==========================
# ADMIN
# ==========================

def admin_data(request):
    return render(request, 'admin/index.html')

def admin_buat(request):
    return render(request, 'admin/tambah.html')

def admin_detail(request, id):
    return render(request, 'admin/detail.html', {'id': id})

def admin_edit(request, id):
    return render(request, 'admin/edit.html', {'id': id})

def admin_hapus(request, id):
    return render(request, 'admin/hapus.html', {'id': id})


# ==========================
# SUPERVISOR
# ==========================

def supervisor(request):
    return render(request, 'supervisor/index.html')

def supervisor_buat(request):
    return render(request, 'supervisor/tambah.html')

def supervisor_detail(request, id):
    return render(request, 'supervisor/detail.html', {'id': id})

def supervisor_edit(request, id):
    return render(request, 'supervisor/edit.html', {'id': id})

def supervisor_hapus(request, id):
    return render(request, 'supervisor/hapus.html', {'id': id})


# ==========================
# PERUSAHAAN
# ==========================

def perusahaan(request):
    return render(request, 'perusahaan/index.html')

def perusahaan_buat(request):
    return render(request, 'perusahaan/tambah.html')

def perusahaan_detail(request, id):
    return render(request, 'perusahaan/detail.html', {'id': id})

def perusahaan_edit(request, id):
    return render(request, 'perusahaan/edit.html', {'id': id})

def perusahaan_hapus(request, id):
    return render(request, 'perusahaan/hapus.html', {'id': id})


# ==========================
# LOWONGAN
# ==========================

def lowongan(request):
    return render(request, 'lowongan/index.html')

def lowongan_buat(request):
    return render(request, 'lowongan/tambah.html')

def lowongan_detail(request, id):
    return render(request, 'lowongan/detail.html', {'id': id})

def lowongan_edit(request, id):
    return render(request, 'lowongan/edit.html', {'id': id})

def lowongan_hapus(request, id):
    return render(request, 'lowongan/hapus.html', {'id': id})


# ==========================
# LAMARAN
# ==========================

def lamaran(request):
    return render(request, 'lamaran/index.html')

def lamaran_buat(request):
    return render(request, 'lamaran/tambah.html')

def lamaran_detail(request, id):
    return render(request, 'lamaran/detail.html', {'id': id})

def lamaran_edit(request, id):
    return render(request, 'lamaran/edit.html', {'id': id})

def lamaran_hapus(request, id):
    return render(request, 'lamaran/hapus.html', {'id': id})


# ==========================
# MAGANG
# ==========================

def magang(request):
    return render(request, 'magang/index.html')

def magang_buat(request):
    return render(request, 'magang/tambah.html')

def magang_detail(request, id):
    return render(request, 'magang/detail.html', {'id': id})

def magang_edit(request, id):
    return render(request, 'magang/edit.html', {'id': id})

def magang_hapus(request, id):
    return render(request, 'magang/hapus.html', {'id': id})


# ==========================
# JURNAL
# ==========================

def jurnal(request):
    return render(request, 'jurnal/index.html')

def jurnal_buat(request):
    return render(request, 'jurnal/tambah.html')

def jurnal_detail(request, id):
    return render(request, 'jurnal/detail.html', {'id': id})

def jurnal_edit(request, id):
    return render(request, 'jurnal/edit.html', {'id': id})

def jurnal_hapus(request, id):
    return render(request, 'jurnal/hapus.html', {'id': id})


# ==========================
# LAPORAN
# ==========================

def laporan(request):
    return render(request, 'laporan/index.html')

def laporan_buat(request):
    return render(request, 'laporan/tambah.html')

def laporan_detail(request, id):
    return render(request, 'laporan/detail.html', {'id': id})

def laporan_edit(request, id):
    return render(request, 'laporan/edit.html', {'id': id})

def laporan_hapus(request, id):
    return render(request, 'laporan/hapus.html', {'id': id})


# ==========================
# NILAI
# ==========================

def nilai(request):
    return render(request, 'nilai/index.html')

def nilai_buat(request):
    return render(request, 'nilai/tambah.html')

def nilai_detail(request, id):
    return render(request, 'nilai/detail.html', {'id': id})

def nilai_edit(request, id):
    return render(request, 'nilai/edit.html', {'id': id})

def nilai_hapus(request, id):
    return render(request, 'nilai/hapus.html', {'id': id})


# ==========================
# NOTIFIKASI
# ==========================

def notifikasi(request):
    return render(request, 'notifikasi/index.html')

def notifikasi_buat(request):
    return render(request, 'notifikasi/tambah.html')

def notifikasi_detail(request, id):
    return render(request, 'notifikasi/detail.html', {'id': id})

def notifikasi_edit(request, id):
    return render(request, 'notifikasi/edit.html', {'id': id})

def notifikasi_hapus(request, id):
    return render(request, 'notifikasi/hapus.html', {'id': id})