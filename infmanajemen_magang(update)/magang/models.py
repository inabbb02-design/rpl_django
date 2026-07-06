from django.db import models

# Create your models here.

# ==========================================
# 1. MODEL UTAMA / BASIS SISTEM
# ==========================================

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Siswa', 'Siswa'),
        ('Guru', 'Guru'),
        ('Supervisor', 'Supervisor'),
    ]
    # id_user otomatis bertindak sebagai id (Primary Key) bawaan Django
    nama = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    kontak = models.CharField(max_length=50)
    status_aktif = models.CharField(max_length=50)
    tanggal_dibuat = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} ({self.role})"


class Perusahaan(models.Model):
    nama_instansi = models.CharField(max_length=255)
    alamat = models.TextField()
    kontak_supervisor = models.CharField(max_length=50)
    id_user_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perusahaan_supervisor')
    deskripsi_pekerjaan = models.TextField()
    kuota_maksimal = models.IntegerField()
    status_mitra = models.CharField(max_length=50)
    tanggal_bergabung = models.DateField()

    def __str__(self):
        return self.nama_instansi


class Lowongan(models.Model):
    id_perusahaan = models.ForeignKey(Perusahaan, on_delete=models.CASCADE, related_name='lowongan_perusahaan')
    judul_posisi = models.CharField(max_length=255)
    deskripsi = models.TextField()
    kriteria = models.TextField()
    kuota_tersedia = models.IntegerField()
    tanggal_dibuat = models.DateField(auto_now_add=True)
    batas_lamaran = models.DateField()
    status_lowongan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.judul_posisi} - {self.id_perusahaan.nama_instansi}"


# ==========================================
# 2. SUB-TYPE / EXTENSION PROFIL USER
# ==========================================

class Siswa(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='siswa_profile')
    nisn = models.CharField(max_length=50, unique=True)
    jurusan = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return f"Siswa: {self.id_user.nama}"


class GuruPembimbing(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guru_profile')
    nidn = models.CharField(max_length=50, unique=True)
    mata_pelajaran = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return f"Guru: {self.id_user.nama}"


class Admin(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    bagian = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return f"Admin: {self.id_user.nama}"


class SupervisorPerusahaan(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor_profile')
    id_perusahaan = models.ForeignKey(Perusahaan, on_delete=models.CASCADE, related_name='supervisors')
    jabatan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return f"Supervisor: {self.id_user.nama} ({self.id_perusahaan.nama_instansi})"


# ==========================================
# 3. PROSES TRANSAKSI, OPERASIONAL & EVALUASI
# ==========================================

class Lamaran(models.Model):
    id_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='lamaran_siswa')
    id_lowongan = models.ForeignKey(Lowongan, on_delete=models.CASCADE, related_name='lamaran_lowongan')
    tanggal_lamaran = models.DateField()
    status_lamaran = models.CharField(max_length=50)
    catatan_admin = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lamaran {self.id_siswa.id_user.nama} di {self.id_lowongan.judul_posisi}"


class MagangPenempatan(models.Model):
    id_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='penempatan_siswa')
    id_perusahaan = models.ForeignKey(Perusahaan, on_delete=models.CASCADE, related_name='penempatan_perusahaan')
    id_guru = models.ForeignKey(GuruPembimbing, on_delete=models.CASCADE, related_name='penempatan_guru')
    id_lowongan = models.ForeignKey(Lowongan, on_delete=models.CASCADE, related_name='penempatan_lowongan')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status_magang = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Magang {self.id_siswa.id_user.nama} - {self.id_perusahaan.nama_instansi}"


class Notifikasi(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifikasi_user')
    judul = models.CharField(max_length=255)
    pesan = models.TextField()
    jenis = models.CharField(max_length=50)  # info / pengingat / peringatan
    status_baca = models.BooleanField(default=False)
    tanggal_dibuat = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Notif: {self.judul} -> {self.id_user.nama}"


class JurnalHarian(models.Model):
    id_magang = models.ForeignKey(MagangPenempatan, on_delete=models.CASCADE, related_name='jurnal_magang')
    tanggal = models.DateField()
    deskripsi_aktivitas = models.TextField()
    lampiran_foto = models.CharField(max_length=255, blank=True, null=True)
    status_validasi = models.CharField(max_length=50)
    catatan_validasi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Jurnal {self.id_magang.id_siswa.id_user.nama} - {self.tanggal}"


class Laporan(models.Model):
    id_magang = models.ForeignKey(MagangPenempatan, on_delete=models.CASCADE, related_name='laporan_magang')
    judul_laporan = models.CharField(max_length=255)
    file_laporan = models.CharField(max_length=255)
    tanggal_upload = models.DateField(auto_now_add=True)
    revisi_ke = models.IntegerField(default=0)
    catatan_pembimbing = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Laporan {self.judul_laporan} ({self.id_magang.id_siswa.id_user.nama})"


class Nilai(models.Model):
    id_magang = models.ForeignKey(MagangPenempatan, on_delete=models.CASCADE, related_name='nilai_magang')
    nilai_industri = models.DecimalField(max_digits=5, decimal_places=2)
    nilai_laporan = models.DecimalField(max_digits=5, decimal_places=2)  # nilai_laporan (akademis)
    nilai_ujian_akhir = models.DecimalField(max_digits=5, decimal_places=2)
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2)
    rekomendasi_perusahaan = models.TextField(blank=True, null=True)
    tanggal_input_industri = models.DateField()
    tanggal_input_guru = models.DateField()

    def __str__(self):
        return f"Nilai Akhir: {self.nilai_akhir} ({self.id_magang.id_siswa.id_user.nama})"