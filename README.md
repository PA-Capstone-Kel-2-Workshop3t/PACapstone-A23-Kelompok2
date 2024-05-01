# <span style= "color: #1ba0e2"> **Dokumentasi dan Buku Panduan Program Workshop 3T** </span>

## <span style= "color: #1ba0e2">Mengurangi Kemiskinan Dengan Pelatihan dan Pemberdayaan Untuk Masyarakat di Kawasan 3T
 </span>
 
## <span style= "color: #1ba0e2">**Anggota Kelompok** </span>
* **Muhamad Nur Fadilah** - 2309116001
* **Nazwa Tri Ananda** - 2309116018
* **Muhammad Hisyam Nugroho** - 2309116020
------------------
## <span style= "color: #1ba0e2">**Daftar Isi** </span>

* [**Deskripsi Program**](#Deskripsi-Program)
* [**Struktur Project**](#Struktur-Program)
* [**Fitur dan Fungsionalitas**](#Fitur-dan-Fungsionalitas)
* [**Cara Penggunaan**](#Cara-Penggunaan)
    * [**Menu Login Program**](#Opsi-Awal)
    * [**Tampilan User**](#Tampilan-User)
    * [**Tampilan Admin**](#Menu-Admin)
* [**Cara Penggunaan**](#Cara-Penggunaan)
    * [**Apabila Pengguna Adalah Anggota**](#Anggota)
    * [**Apabila Pengguna Adalah Admin**](#Admin)
  
------------------
## **Deskripsi Program**

Workshop 3T adalah program pelatihan dan pemberdayaan untuk masyarakat dikawasan 3T. Program ini berfokus pada penyediaan keterampilan melalui workshop, meningkatkan keterampilan dan kapasitas masyarakat dalam bidang tertentu, mengurangi tingkat kemiskinan dengan memberdayakan masyarakat melalui pelatihan dan pendampingan, serta menggunakan teknologi database sistem manajemen untuk memantau dan mengevaluasi kemajuan peserta workshop. Program ini di implementasikan dengan struktur data dan algoritma yang telah dipelajari pada kelas praktikum,
yaitu Linked list, Search, dan Sort. 

------------------
## **Struktur Project**
### Flowchart Program
**- Menu Login Program**
  
![PA ASDBMS Flowchart-Menu Login Program drawio](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/15653af4-b74a-481b-bc25-b6a8e2b3c260)

**- Menu Awal Anggota**
  
![PA ASDBMS Flowchart-Menu Awal Anggota drawio](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/67e07f32-1593-485c-b27c-fbcf0e1e2a84)

- Menu Utama Anggota
![PA ASDBMS Flowchart-Menu Anggota Login drawio](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/808d244f-e6cd-42a6-8bf6-5767fcb0f5cf)

**- Login Admin**
  
![PA ASDBMS Flowchart-Login Admin drawio](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/f5f58f4a-c07e-43c5-9acc-0a980338d456)

**- Menu Utama Admin**
  
  ![PA ASDBMS Flowchart-Menu Utama Admin drawio (1)](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/b105cca8-68a2-482f-8b30-a9852f83f170)


------------------
## **Fitur dan Fungsionalitas**
### Fitur
>  1. Modul os dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan folder.
>  2. Modul mysql.connector adalah modul untuk menyediakan fungsi-fungsi untuk menjalankan kueri SQL, memanipulasi data, dan mengelola koneksi ke server MySQL.
>  3. Modul pwinput adalah modul untuk menerima input password tanpa menampilkan karakter yang dimasukkan ke layar, sehingga meningkatkan keamanan saat memasukkan kata sandi.
>  4. Modul pretty table adalah modul yang berguna untuk membuat tabel yang terstruktur dan terlihat rapi di terminal atau konsol Python.

Berdasarkan kebutuhan program, berikut ini adalah fitur pada program:
- Admin (Pengelola Workshop)
>  1. Membuat UMKM : Admin dapat membuat UMKM dengan menginputkan ID UMKM, Nama Usaha, Bidang Usaha, Produk Usaha, Slot Karyawan, Alamat, dan Nomor Telp UMKM.
>  2. Memeriksa Data: Admin dapat memeriksa Daftar Workshop, Daftar Anggota, Daftar UMKM, Rekap Pendanaan Pemerintah.
>  3. Memperbarui Data: Admin dapat memperbarui data UMKM, memperbarui data Anggota.
>  4. Menghapus Data: Admin dapat menghapus data workshop, menghapus data anggota, dan menghapus data pemerintah
>  5. Mencari Data: Admin dapat mencari data yang dibutuhkan seperti mencari data Workshop, mencari data Anggota, dan mencari Data UMKM.
>  6. Mengurutkan Data: Admin dapat Mengurutkan data yang dibutuhkan seperti mengurutkan data Workshop, mengurutkan data Anggota, dan mengurutkan Data UMKM.

- Anggota
>  1. Mendaftar UMKM: Anggota dapat memilih UMKM yang dibutuhkan
>  2. Mendaftar Workshop: Anggota dapat memilih Workshop yang di butuhkan
>  3. Memeriksa Data Diri: Anggota dapat memeriksa Data Diri

### Fungsionalitas
Berdasarkan struktur program, berikut ini adalah fungsionalitas yang terdapat pada program:
>  1. Registrasi Anggota: Anggota Masyarakat dapat mendapatkan pelatihan jika dia mendaftarkan akunnya dan memilih UMKM serta Workshop yang dia butuhkan, Registrasi Anggota dilakukan dengan memasukkan ID Anggota, Nama, Gender, TTL, No Hp, dan Password.
>  2. Login dan Logout (Exit) pada menu Admin dan User. User dapat melakukan login ke dalam program dengan menggunakan ID Admin atau ID Anggota kemudian serta password akun mereka. User dan Admin juga dapat keluar dari program dengan melalui pilihan Exit.
>  4. CRUD, Sorting dan Searching pada Admin. Admin dapat melakukan penambahan UMKM, melihat data, menghapus data, dan mengupdate data serta melakukan sorting dan searching.
>  5. Create dan Read pada Anggota. Anggota dapat melakukan mendaftar pada UMKM dan Workshop. 

-------------------------------------------------------------------------------------------------
## **Cara Penggunaan**
### Apabila Pengguna Adalah Admin
**- Menu Awal Program**
  
  ![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/c5530847-768f-4d40-9b67-91b1383b43a6)

  Apabila pengguna adalah Admin, pengguna dapat memilih **login sebagai Admin** dengan cara memilih angka satu(1) dan menginputkannya didalam program. setelah pengguna menginputkan pilihannya, pengguna akan diarahkan program pada bagian login untuk admin yaitu dengan **memasukkan ID Admin dan Password Akun Admin**.

  Jika Id Admin dan Password yang diinputkan kedalam program sesuai maka program akan menampilkan output seperti berikut ini.
  
  ![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/357895d2-a574-421d-b9eb-15ec4e839a2c)

 **- Menu Utama Admin**
    
![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/c1079c1c-044e-4f9b-a7af-fc9d017a2c7d)

Pada menu utama Admin terdapat 7 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu membuat UMKM apabila memilih satu(1), memeriksa data apabila memilih dua(2), memperbarui 
data apabila memilih tiga(3), menghapus data apabila memilih empat(4), mencari data apabila memilih lima(5), mengurutkan data apabila memilih dua(6), dan keluar apabila memilih 
tujuh(7).

**a. Pilih satu (Menambah UMKM)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/1173cb35-c75e-419b-aabf-0ed670df46d7)

Admin dapat menambahkan UMKM dengan memasukkan **ID UMKM, Nama Usaha, Bidang Usaha, Produk Usaha, Slot Karyawan, Alamat Usaha, dan Nomor Telp UMKM**. setelah itu user bisa menekan enter dan UMKM baru telah berhasil ditambahkan kedalam database.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/1a7a37f9-1c73-4a08-b62d-ab2923d086ac)

Program akan menampilkan data UMKM baru yang baru saja di tambahkan, Admin juga dapat menambahkan UMKM baru dengan menginputkan **y** pada program dan menginputkan **n** jika tidak ingin menambahkan UMKM lagi. kemudian jika user memilih n, Admin akan diarahkan ke menu awal kembali.
    
**b. Pilih dua(Memeriksa Data)**

Pada menu memeriksa data terdapat 5 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu memeriksa data Workshop apabila memilih satu(1), memeriksa data Anggota apabila memilih dua(2), memeriksa data UMKM apabila memilih tiga(3), memeriksa Pendanaan Program apabila memilih empat(4), dan keluar apabila memilih tujuh(5).

**1. Memeriksa Data Workshop**

Program akan menampilkan Keseluruhan data dari Workshop.
   
![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/16c7a5b1-cbe6-4999-b7ae-88219b78ab8d)

**2. Memeriksa Data Anggota**

Program akan menampilkan Keseluruhan data dari Anggota.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/e17f231e-9e17-4fce-a760-4757f2b90a34)

**3. Memeriksa Data UMKM**

Program akan menampilkan Keseluruhan data dari UMKM. 

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/abf26b37-6c39-452d-9d29-2b23a1f72b94)

**4. Memeriksa Pendanaan Program**

Program akan menampilkan Keseluruhan data dari Pendanaan Program dari Pemerintah.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/d19b4ae1-c977-40cd-af40-53dfd1eb720b)

**5. Keluar**
Program akan mengarahkan Admin ke menu utama admin kembali.

**c. Pilih tiga(Memperbarui Data)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/8fe9e995-7c22-4b39-bca6-5d3719117831)

Pada menu memperbarui data terdapat 4 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu memperbarui data Workshop apabila memilih satu(1), memperbarui data Anggota apabila memilih dua(2), memperbarui data UMKM apabila memilih tiga(3), keluar apabila memilih empat(4).

**1. Memperbarui Data Workshop**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/140c4f41-5645-4fbd-a7e1-3b9c007c768f)

Untuk memperbarui Data Workshop, Admin perlu menginputkan **ID Workshop, Nama Lembaga, Waktu Operasional, Alamat Workshop dan No.Telp**. setelah data diinputkkan Admin dapat menekan enter dan data telah diperbarui.

berikut ini adalah tampilan Data Workshop yang telah diperbarui dengan data sebelumnya.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/fd033299-a25d-45c1-a419-d62f70b518c1)


**2. Memperbarui Data Anggota**

Untuk memperbarui Data Anggota, Admin perlu menginputkan** ID Anggota, Nama, Gender, TTL, Alamat dan No.Hp**. setelah data diinputkkan Admin dapat menekan enter dan data telah diperbarui.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/eb51f923-1130-4d4b-a059-fa54d5d8895a)

berikut ini adalah tampilan Data Anggota yang telah diperbarui dengan data sebelumnya.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/bbc1dc89-84d3-42db-84f8-17009b37c2e7)

**3. Memperbarui Data UMKM**

Untuk memperbarui Data UMKM, Admin perlu menginputkan **ID UMKM, Nama Usaha, Bidang Usaha, Produk Usaha, Slot Karyawan, Alamat, dan No.Telp**. setelah data diinputkkan Admin dapat menekan enter dan data telah diperbarui.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/89965202-7935-4e91-af3d-1765096c6a4e)

berikut ini adalah tampilan Data UMKM yang telah diperbarui dengan data sebelumnya.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/24b8ebe8-3429-4eb7-a2b1-b1b04e8f1e90)

**4. Keluar**
Program akan mengarahkan Admin ke menu utama admin kembali.

**d. Pilih empat(Menghapus Data)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/dfd560ee-2e22-47e6-a8ac-aff057477585)

Pada menu menghapus data terdapat 4 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu menghapus data Workshop apabila memilih satu(1), menghapus data Anggota apabila memilih dua(2), menghapus data UMKM apabila memilih tiga(3), keluar apabila memilih empat(4).

untuk menghapus data workshop, anggota dan pemerintah. Admin cukup **menginputkan ID**, seperti berikut ini.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/97b9da8a-1d39-4642-a4c0-de8bfc4a4f2a)

**e. Pilih lima(Mencari Data)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/eb56d1d8-8afc-411e-b51e-80eecdc6b12e)

Pada menu mencari data terdapat 4 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu mencari data Workshop apabila memilih satu(1), mencari data Anggota apabila memilih dua(2), mencari data UMKM apabila memilih tiga(3), keluar apabila memilih empat(4).

untuk mencari data workshop, anggota dan pemerintah. Admin cukup menginputkan ID, seperti berikut ini.
![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/246f19c6-946f-4241-96d4-e6171c5fa03a)

**f. Pilih enam(Mengurutkan Data)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/db1f13ec-07e7-4d59-81d1-70607d09d00c)

Pada menu mengurutkan data terdapat 4 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu mengurutkan data Workshop apabila memilih satu(1), mengurutkan data Anggota apabila memilih dua(2), mengurutkan data UMKM apabila memilih tiga(3), keluar apabila memilih empat(4).

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/a4b4c7d3-6031-4371-a978-9508eddf26ef)

didalam menu pengurutan data terdapat pilihan untuk mengurutkan data secara ascending maupun descending, admin dapat memilih sesuai dengan kebutuhannya, berikut ini adalah tampilan apabila admin memilih pengurutan secara ascending.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/94b5b375-25e9-42b6-b895-a169e2ab51c3)

**g. Pilih tujuh(Keluar)**

Program akan mengarahkan Admin ke menu login program.

-------------------------------------------------------------------------------------------------
### Apabila Pengguna Adalah Anggota
**- Menu Awal Anggota**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/1963d18a-44c2-4f6c-86a5-890a232daa15)

**a. Apabila User Login**

Apabila pengguna adalah Anggota, pengguna dapat memilih angka satu(1) dengan menginputkannya didalam program untuk masuk kedalam menu utama Anggota. setelah pengguna menginputkan pilihannya, pengguna akan diarahkan program pada bagian login untuk admin yaitu dengan **memasukkan ID Anggota dan Password Akun Anggota**.

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/ee204913-a8f5-48e5-974d-5c603e6c52e5)

**b. Apabila User Registrasi**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/d81a1908-89e1-477b-9a05-a42ddae6037f)

meminta pengguna untuk menginput datanya sesuai kolom

**c. Apabila User Kembali**

Program akan mengarahkan Admin ke menu Login Program.

**- Menu Utama Anggota**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/63054e41-2e2e-4290-8e6c-1d8b98a45e42)

Pada menu utama Anggota terdapat 3 pilihan yang dapat Admin pilih sesuai kebutuhannya yaitu mendaftar UMKM apabila memilih satu(1), mendaftar Workshop apabila memilih dua(2), memeriksa data diri apabila memilih tiga(3), dan keluar apabila memilih empat(4).

**a. Pilih satu (Mendaftar UMKM)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/41857509-c459-43ea-b787-cdc59f80adda)

setelah menginputkan y maka program akan memberikan output seperti ini untuk memastikan apakah pengguna yakin ingin mengganti umkm yang didaftar atau tidak 

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/bd893398-5393-442a-ba25-9c923cc7404c)

**b. Pilih dua(Mendaftar Workshop)**

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/9c91cacf-05a9-4c7c-ba89-4bcc9f703c6b)

setelah menginputkan y maka program akan memberikan output seperti ini untuk memastikan apakah pengguna yakin ingin berpindah workshop atau tidak

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/cf53750a-f550-4670-b50a-f4ddc0de9009)

**c. Pilih tiga(Memeriksa Data Diri)**

memperlihatkan biodata dari pengguna sesuai dengan id pengguna saat login

![image](https://github.com/PA-Capstone-Kel-2-Workshop3t/PACapstone-A23-Kelompok2/assets/144808370/198a49e6-a033-4529-b669-a0ee7c4ce9ce)

**d. Pilih empat(Keluar)**

Program akan mengarahkan Admin ke menu awal anggota.

