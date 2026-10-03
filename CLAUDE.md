# Kopi Koma Partner Portal (EDTS APM 2027 written test)

## Konteks tes
- Screening test posisi Associate Product Manager di EDTS.
- Case: franchisor ingin mendigitalkan alur dengan calon franchisee, dari pengajuan sampai approval kedua pihak. Deliverable: prototype HTML yang bisa diklik + spec doc (PRD) sebagai pitch.
- Spec doc wajib berisi: asumsi (bisnis klien, pain point), fitur yang dipilih dan alasannya, serta cara memakai AI selama pengerjaan (lampirkan screenshot atau PDF percakapan AI).
- Format spec doc: Arial 11, justified, Bahasa Indonesia atau Inggris. Header kiri atas: "Nama - Universitas". Nama file: "EDTS APM 2027 - Nama - Universitas".
- Submission: prototype di-upload lewat https://vercel.com/drop, lalu link Vercel + spec doc dikirim ke Google Form https://tinyurl.com/TaskAPM2027.
- Deadline: 6 Oktober 2026, 18:00 WIB.

## Asumsi bisnis
- Klien fiktif: Kopi Koma, brand kopi kekinian lokal, sekitar 80 outlet, target ekspansi sekitar 50 outlet per tahun. Tulis "nama fiktif" di PRD (ada brand nyata bernama Titik Koma).
- Paket: Gerobak (Rp 45 jt, tanpa royalti) dan Cafe (Rp 450 jt, royalti 5%). Kiosk sudah dihapus.
- Data pendukung sektor: F&B 47,77% dari waralaba Indonesia (Kemendag, Feb 2025); jumlah kedai kopi naik hampir 3x dalam 3 tahun (Kemenperin, Mei 2025). Pertumbuhan nilai pasar kopi moderat (proyeksi 3,61% 2024-2029), jadi argumennya adalah ekspansi gerai via franchise, bukan "pasar booming".
- Revenue = nilai deal paket kemitraan setelah diskon dari franchisee yang disetujui. Royalti tidak dihitung.

## Alur (POV franchisor), 8 tahap
| # | Tahap | PIC | Batas waktu |
|---|---|---|---|
| 1 | Lead baru | Sistem (otomatis) / Manajer | 1 hari |
| 2 | Presentasi bisnis + kirim prospektus (wajib secara regulasi) | Sales | 4 hari |
| 3 | Survei lokasi | Sales | 5 hari |
| 4 | Penilaian kelayakan: wawancara, pemeriksaan latar belakang, verifikasi finansial, KYC, komitmen | Penilai | 4 hari |
| 5 | Quotation (dulu "proposal") | Sales | 3 hari |
| 6 | Negosiasi: sales catat tanggapan (setuju / minta perubahan / mundur) | Sales | 7 hari |
| 7 | Persetujuan akhir: setujui / tolak / minta revisi lokasi | Manajer | 2 hari |
| + | Disetujui, Ditolak | | |

Aturan penting:
- Lead baru: lead dari sales langsung diteruskan ke presentasi. Lead mandiri (website/Instagram) otomatis ditugaskan ke sales sesuai wilayah. Masuk antrean manajer bila: kota di luar wilayah, terindikasi duplikat (HP/email sama dengan lead aktif), atau sales wilayah sudah memegang 5 lead aktif.
- Minta perubahan saat negosiasi: aplikasi kembali ke Quotation (label Revisi). Sales dan manajer berdiskusi DI LUAR sistem; saat kirim quotation versi berikutnya sales wajib isi "Hasil diskusi dengan manajer".
- Minta revisi lokasi: kembali ke Survei lokasi; setelah layak langsung ke Quotation (tanpa penilaian kelayakan ulang).
- Pengingat sepenuhnya otomatis (notifikasi dashboard + email) ke PIC dan manajer saat lewat batas waktu. Tidak ada tombol kirim pengingat manual. Tidak ada WhatsApp.
- Dua aplikasi terpisah dari `index.html` yang sama: dashboard franchisor di `/` (hanya POV franchisor, tanpa tautan ke sisi franchisee) dan Portal Mitra untuk calon franchisee di `/mitra` (rewrite di `vercel.json`; saat tes lokal pakai `index.html#mitra`). Portal Mitra: formulir pendaftaran (masuk sebagai lead mandiri lalu ikut aturan penugasan otomatis), tracker status 7 langkah (cek dengan nomor pengajuan + email/HP), dan tanggapan quotation langsung (setujui / minta perubahan / tidak melanjutkan). Quotation dikirim via email beserta link portal. Bila franchisee menjawab lewat telepon/tatap muka, sales tetap bisa mencatat tanggapan di tab Negosiasi. Aksi franchisee tercatat di audit trail sebagai "Calon franchisee (portal mitra)" (`by: FR`).

## Peran (login demo, password semua akun: demo123)
| Peran | Akun | Menu | Bisa memproses |
|---|---|---|---|
| Super Admin | arif.hakim@kopikoma.id | Pipeline, Semua tugas, Target dan pencapaian, Kinerja sales, Pengguna dan peran | Semua tahap (tercatat atas namanya) |
| Manajer | laras.anggraini@kopikoma.id | Pipeline, Tugas saya, Semua tugas, Target, Kinerja sales | Penugasan lead baru (pengecualian), persetujuan akhir |
| Sales | rendi / putri / agus / wulan @kopikoma.id | Pipeline saya (lead sendiri), Tugas saya, Target saya | Input lead, presentasi, survei, quotation, negosiasi |
| Penilai | bima.prasetyo / dimas.arya @kopikoma.id | Pipeline, Tugas saya | Penilaian kelayakan |

- Indikator lewat batas waktu hanya terlihat oleh Super Admin dan Manajer.
- Wilayah sales: Rendi = Tangerang Raya; Putri = Jakarta, Bogor, Depok, Bekasi, Cikarang; Agus = Bandung Raya; Wulan = Jawa Tengah.

## Fitur lain
- Persetujuan dua pihak: 1 dari 2 = franchisee menyetujui quotation (di portal atau dicatat sales), 2 dari 2 = persetujuan akhir manajer.
- Status persetujuan per aplikasi (modal timeline 7 langkah, PIC + lama menunggu), dari kartu, drawer, dan tabel tugas.
- Skor kecocokan AI (profil 40%, lokasi 60%) dengan alasan plus/minus. DISIMULASIKAN dengan pembobotan aturan + data peta simulasi; jujur sebutkan di PRD. Alat bantu, bukan penolakan otomatis.
- Target dan pencapaian: periode Bulanan/Kuartal/Semester/Tahunan, target vs "seharusnya per hari ini" (MTD/QTD/HTD/YTD), revenue + kuantitas, funnel 6 tahap dihitung mundur dari rasio konversi (bisa diubah).
- Kinerja sales (manajer/super admin): dua tabel terpisah (revenue dan kuantitas), diurutkan dari paling perform, kolom Target, Seharusnya per 20 Okt, Capaian, %, Selisih, Status. Status mengikuti metrik terlemah.
- Profil pengguna (peran, menu, tugas, notifikasi email, aktivitas), Pengguna dan peran (matriks akses).
- Audit trail per aplikasi, termasuk akses dokumen. Persetujuan data pribadi (UU PDP) wajib saat input lead.
- Data demo "hari ini" = 20 Oktober 2026 supaya angka MTD bermakna.

## Struktur kode
- Satu file `index.html` tanpa build (plus `vercel.json` untuk route `/mitra`): CSS di `<style>`, JS vanilla di `<script>`, font Plus Jakarta Sans dari Google Fonts.
- Bagian JS ditandai komentar `/* ===================== nama ===================== */`: base, people & roles, flow, AI score, seed data, sales history, state, helpers, top bar, render (login + tab per peran), pipeline, all tasks, users & roles, profile, partner portal (calon franchisee), approval status modal, detail drawer, actions, add lead, target & sales performance.
- `MODE` (`staff` / `mitra`) menentukan aplikasi yang dirender. Data aplikasi dan notifikasi (`state.apps`, `state.notifs`, `tick`, `nid`) disimpan di localStorage (`kopikoma-demo-v2`; naikkan versinya bila seed atau teks log berubah agar data lama otomatis diganti) supaya kedua aplikasi terhubung, termasuk antar-tab lewat event `storage`. State UI dan login (`ME`) tetap di memori. Tombol "Reset data demo (khusus prototipe)" di menu akun menghapus data tersimpan dan kembali ke seed.
- UI dalam Bahasa Indonesia. Istilah bisnis yang lazim tetap dipakai: Sales, Lead, Quotation, Pipeline, Franchisee, KYC, Super Admin, revenue, funnel. Selain itu pakai Bahasa Indonesia (Penilaian kelayakan, Penilai, Persetujuan, Capaian, Kinerja sales, dasbor, tindak lanjut, kesepakatan, wawancara, prototipe). Hindari em dash di teks UI.

## Cara tes
Jalankan tes headless dengan Playwright (Python) terhadap `file://.../index.html`, panggil fungsi global seperti `quickLogin('rendi')`, `openAdd(); demoFill(); submitLead()`, `submitPresentasi`, `submitSurvey`, `submitAssessment`, `sendQuote`, `negoAgree`, `finalDecision(id,'ok')`, dan pastikan tidak ada `pageerror`. Bersihkan localStorage di awal tes. Sisi franchisee (buka `index.html#mitra`): `openPortal('form'); portalDemoFill(); submitPortal()`, lalu `openPortal('track'); portalLookup(id, email)`, `portalAgree(id)` / `portalChange(id)` / `portalWithdraw(id)`.

## Pekerjaan berikutnya
1. Pertimbangkan menggabungkan kolom Disetujui dan Ditolak jadi "Selesai" (kanban sekarang 9 kolom dan perlu scroll horizontal di laptop).
2. Perbarui PRD/spec doc agar sesuai prototype terbaru: alur 8 tahap, peran, aturan penugasan otomatis, batas waktu, definisi revenue, skor AI simulasi, MoSCoW (MVP vs fase berikutnya), kebutuhan non-fungsional (UU PDP, mobile, audit trail, AI sebagai alat bantu), roadmap, dan bagian penggunaan AI.
3. Upload ulang `index.html` ke vercel.com/drop setiap kali ada revisi, lalu kirim link terbaru.
