import os
import mysql.connector
import pwinput
from prettytable import PrettyTable

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="workshop_3t"
)
mycursor = mydb.cursor()

# Fungsi untuk membersihkan layar konsol
def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_all_data_pemerintah(self):
        mycursor.execute("SELECT * FROM pemerintah")
        result = mycursor.fetchall()
        if result:
            x = PrettyTable()
            x.field_names = ["ID_Pemerintah", "Nama_Instansi", "Alamat_Instansi", "NO_Telp", "Pendanaan_Program"]
            for row in result:
                x.add_row(row)
            print(x)
        else:
            print("Tidak ada data pemerintah")

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print("Nama Usaha:", current.data["Nama_Usaha"])
            print("Bidang Usaha:", current.data["Bidang_Usaha"])
            print("Produk Usaha:", current.data["Produk_Usaha"])
            print("Slot Karyawan:", current.data["Slot_Karyawan"])
            print("Alamat:", current.data["Alamat"])
            print("No HP:", current.data["No_HP"])
            print("-----------------------------")
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display_workshop(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID_Anggota", "ID_Pemerintah", "ID_Workshop", "ID_Admin", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_pemerintah(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID_Pemerintah", "Nama_Instansi", "Alamat_Instansi", "NO_Telp", "Pendanaan_Program"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_anggota(self):        
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_umkm(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def jump_search(self,arr, x):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n)-1][0] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while arr[prev][0] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev][0] == x:
            return prev
        return -1
        
    def quick_sort(self,arr, ascending=True):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2][0]
        left = [x for x in arr if x[0] < pivot]
        middle = [x for x in arr if x[0] == pivot]
        right = [x for x in arr if x[0] > pivot]
        if ascending:
            return self.quick_sort(left, ascending) + middle + self.quick_sort(right, ascending)
        else:
            return self.quick_sort(right, ascending) + middle + self.quick_sort(left, ascending)
        
    def display_table(self, data_list, fields):
        x = PrettyTable()
        x.field_names = fields
        for data in data_list:
            x.add_row(data)
        print(x)

    # CRUD(create Data)
    def tambah_umkm(self):
        new_umkm_list = []  # Membuat list untuk menyimpan semua data UMKM baru
        while True:
            try: 
                clear()  # Membersihkan layar konsol
                ID_UMKM = int(input("Masukkan ID UMKM baru: "))
                Nama_Usaha = input("Masukkan Nama Usaha baru: ")
                Bidang_Usaha = input("Masukkan Bidang Usaha baru: ")
                Produk_Usaha = input("Masukkan Produk Usaha baru: ")
                Slot_Karyawan = input("Masukkan Slot Karyawan baru: ")
                Alamat = input("Masukkan Alamat baru: ")
                No_HP = input("Masukkan No. Telp UMKM baru: ")

                query = f"""
                INSERT INTO umkm (ID_UMKM, Nama_Usaha, Bidang_Usaha, Produk_Usaha, Slot_Karyawan, Alamat, No_HP)
                VALUES ({ID_UMKM}, '{Nama_Usaha}', '{Bidang_Usaha}', '{Produk_Usaha}', '{Slot_Karyawan}', '{Alamat}', '{No_HP}')
                """

                mycursor.execute(query)
                mydb.commit()
                print("DATA DATABASE BERHASIL DITAMBAHKAN")

                new_umkm_list.append((ID_UMKM, Nama_Usaha, Bidang_Usaha, Produk_Usaha, Slot_Karyawan, Alamat, No_HP))  # Menambahkan data baru ke dalam list

                input("Tekan Enter untuk melanjutkan...")
                clear()  # Membersihkan layar konsol

                # Menampilkan semua UMKM yang baru ditambahkan
                print("UMKM yang baru saja ditambahkan:")
                x = PrettyTable()
                x.field_names = ["ID_UMKM", "Nama Usaha", "Bidang Usaha", "Produk Usaha", "Slot Karyawan", "Alamat", "No. Telp"]
                x.add_rows(new_umkm_list)  # Menambahkan semua data UMKM baru ke dalam PrettyTable
                print(x)
                
                ulangi = input("Apakah Anda ingin menambahkan UMKM lagi? (y/n): ")
                if ulangi.lower() != 'y':
                    break
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!.")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    def display_table(self,data_list, fields):
        x = PrettyTable()
        x.field_names = fields
        for data in data_list:
            x.add_row(data)
        print(x)

    #CRUD(Read Data)
    def memeriksa_data_workshop(self):
        mycursor.execute("SELECT * FROM Workshop")
        result = mycursor.fetchall()
        data_list = [list(row) for row in result]
        return data_list

    def memeriksa_data_anggota(self):
        mycursor.execute("SELECT * FROM Anggota")
        result = mycursor.fetchall()
        data_list = [list(row) for row in result]
        return data_list

    def memeriksa_data_umkm(self):
        mycursor.execute("SELECT * FROM UMKM")
        result = mycursor.fetchall()
        data_list = [list(row) for row in result]
        return data_list

    def memeriksa_rekap_pendanaan(self):
        mycursor.execute("SELECT * FROM Pemerintah")
        result = mycursor.fetchall()
        data_list = [list(row) for row in result]
        return data_list

    def menu_memeriksa_data(self):
        while True:
            try:
                clear()
                print("======================================")
                print("|         Menu Memeriksa Data        |")
                print("======================================")
                print("| 1. Memeriksa Data Workshop        |")
                print("| 2. Memeriksa Data Anggota         |")
                print("| 3. Memeriksa Data UMKM            |")
                print("| 4. Rekap Pendanaan Program        |")
                print("| 5. Kembali                        |")
                print("=====================================")
                pilput_memeriksa = input("Masukkan pilihan Anda: ")

                if pilput_memeriksa == '1':
                    workshop_data = self.memeriksa_data_workshop()
                    fields = ["ID_Workshop", "ID_Pemerintah", "ID_Admin", "ID_Anggota", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
                    self.display_table(workshop_data, fields)
                    input("Klik Enter Untuk Kembali")
                    clear()

                elif pilput_memeriksa == '2':
                    anggota_data = self.memeriksa_data_anggota()
                    fields = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
                    self.display_table(anggota_data, fields)
                    input("Klik Enter Untuk Kembali")
                    clear()

                elif pilput_memeriksa == '3':
                    umkm_data = self.memeriksa_data_umkm()
                    fields = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
                    self.display_table(umkm_data, fields)
                    input("Klik Enter Untuk Kembali")
                    clear()

                elif pilput_memeriksa == '4':
                    pendanaan_program = self.memeriksa_rekap_pendanaan()
                    fields = ["ID_Pemerintah", "Nama_Instansi", "Alamat_Instansi", "NO_Telp", "Pendanaan_Program"]
                    self.display_table(pendanaan_program, fields)
                    input("Klik Enter Untuk Kembali")
                    clear()

                elif pilput_memeriksa == '5':
                    return
                
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!.")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)


    # CRUD (Update Data)
    def tampilkan_data_terbaru(self, data_list, fields):
        x = PrettyTable()
        x.field_names = fields
        for data in data_list:
            x.add_row(data)
        print(x)

    def perbarui_data_workshop(self):
        mycursor.execute("SELECT * FROM workshop")
        myresult = mycursor.fetchall()
        x = PrettyTable()
        x.field_names = ["ID_Anggota", "ID_Pemerintah", "ID_Workshop", "ID_Admin", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
        for data in myresult:
            x.add_row(data)
        print(x)

        try:
            ID_Workshop = int(input("Masukkan ID Workshop Yang Ingin di Perbarui: "))
            Lembaga = input("Masukkan Nama Lembaga: ")
            Waktu_Operasional = input("Masukkan Waktu_Operasional: ")
            Alamat_Workshop = input("Masukkan Alamat_Workshop: ")
        except KeyboardInterrupt:
            print("\nSilahkan Melakukan Input Dengan Benar!.")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}") 
        except mysql.connector.Error as err:
            print("Error:", err)

        query = f"""
        UPDATE Workshop
        SET Lembaga = '{Lembaga}',
        Waktu_Operasional = '{Waktu_Operasional}',
        Alamat_Workshop = '{Alamat_Workshop}'
        WHERE ID_Workshop = {ID_Workshop}
        """

        mycursor.execute(query)
        mydb.commit()
        print("DATA BERHASIL DIPERBARUI")

        print("\nData Workshop Setelah Diperbarui:")
        workshop_data = self.memeriksa_data_workshop()
        fields = ["ID_Workshop", "ID_Pemerintah", "ID_Admin", "ID_Anggota", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
        self.tampilkan_data_terbaru(workshop_data, fields)

        input("Tekan Enter untuk melanjutkan...")  
        clear() 

    def perbarui_data_anggota(self):
        mycursor.execute("SELECT * FROM Anggota")
        myresult = mycursor.fetchall()
        x = PrettyTable()
        x.field_names = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
        for data in myresult:
            x.add_row(data)
        print(x)
        try:
            ID_Anggota = int(input("Masukkan ID Anggota Yang Ingin di Perbarui: "))
            Nama_Anggota = input("Masukkan Nama Anggota: ")
            Gender = input("Masukkan Jenis Kelamin Anggota: ")
            TTL = input("Masukkan Tempat/Tanggal Lahir Anggota: ")
            No_Hp = input("Masukkan No_Hp Anggota: ")
            Password = pwinput.pwinput("Masukkan Password Anggota: ")
        except KeyboardInterrupt:
            print("\nSilahkan Melakukan Input Dengan Benar!.")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}") 
        except mysql.connector.Error as err:
            print("Error:", err)

        query = f"""
        UPDATE anggota
        SET Nama_Anggota = '{Nama_Anggota}',
        Gender = '{Gender}',
        TTL = '{TTL}',
        No_Hp = '{No_Hp}',
        Password = '{Password}'
        WHERE ID_Anggota = {ID_Anggota}
        """

        mycursor.execute(query)
        mydb.commit()
        print("DATA BERHASIL DIPERBARUI")

        print("\nData Anggota Setelah Diperbarui:")
        anggota_data = self.memeriksa_data_anggota()
        fields = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
        self.tampilkan_data_terbaru(anggota_data, fields)

        input("Tekan Enter untuk melanjutkan...") 
        clear()  

    def perbarui_data_umkm(self):
        umkm_data = self.memeriksa_data_umkm()
        fields_names = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
        self.display_table(umkm_data, fields_names)
        try:
            ID_UMKM = int(input("Masukkan ID UMKM yang ingin diperbarui: "))
            Nama_Usaha = input("Masukkan Nama Usaha: ")
            Bidang_Usaha = input("Masukkan Bidang Usaha: ")
            Produk_Usaha = input("Masukkan Produk Usaha: ")
            Slot_Karyawan = input("Masukkan Slot Karyawan: ")
            Alamat = input("Masukkan Alamat: ")
            No_HP = input("Masukkan No. Telp: ")
        except KeyboardInterrupt:
            print("\nSilahkan Melakukan Input Dengan Benar!.")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}") 
        except mysql.connector.Error as err:
            print("Error:", err)

        query = f"""
        UPDATE UMKM
        SET Nama_Usaha = '{Nama_Usaha}',
            Bidang_Usaha = '{Bidang_Usaha}',
            Produk_Usaha = '{Produk_Usaha}',
            Slot_Karyawan = '{Slot_Karyawan}',
            Alamat = '{Alamat}',
            No_HP = '{No_HP}'
        WHERE ID_UMKM = {ID_UMKM}
        """

        mycursor.execute(query)
        mydb.commit()
        print("Data UMKM berhasil diperbarui")

        print("\nData UMKM Setelah Diperbarui:")
        umkm_data = self.memeriksa_data_umkm()
        fields_names = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
        self.tampilkan_data_terbaru(umkm_data, fields_names)

        input("Tekan Enter untuk melanjutkan...") 
        clear() 

    def menu_memperbarui_data(self):
        while True:
            try:
                clear()
                print("======================================")
                print("|       Menu Memperbarui Data        |")
                print("======================================")
                print("| 1. Memperbarui Data Workshop      |")
                print("| 2. Memperbarui Data Anggota       |")
                print("| 3. Memperbarui Data UMKM          |")
                print("| 4. Kembali                        |")
                print("=====================================")
                pilput_memperbarui = input("Masukkan pilihan Anda: ")

                if pilput_memperbarui == '1':
                    self.perbarui_data_workshop()
                elif pilput_memperbarui == '2':
                    self.perbarui_data_anggota()
                elif pilput_memperbarui == '3':
                    self.perbarui_data_umkm()
                elif pilput_memperbarui == '4':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!.")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    # CRUD(Delete Data)
    def menu_menghapus_data(self):
        while True:
            try:
                clear()
                print("======================================")
                print("|         Menu Menghapus Data        |")
                print("======================================")
                print("| 1. Menghapus Data Pemerintah      |")
                print("| 2. Kembali                        |")
                print("=====================================")
                pilput_memeriksa = input("Masukkan pilihan Anda: ")

                if pilput_memeriksa == '1':
                    LinkedList().hapus_data_pemerintah()
                    pemerintah_data = LinkedList().get_all_data_pemerintah()  # Mendapatkan data setelah penghapusan
                    if pemerintah_data is not None:
                        print("Data Pemerintah:")
                        for data in pemerintah_data:
                            print(data)
                    else:
                        print("Tidak ada data pemerintah.")
                elif pilput_memeriksa == '2':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
                    input("Tekan enter untuk kembali...")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!.")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    def hapus_data_pemerintah(self):
            try:
                self.get_all_data_pemerintah()
                ID_Pemerintah = int(input("Masukkan ID Pemerintah yang ingin dihapus: "))
                # Periksa keterkaitan dengan tabel workshop
                query_check_workshop = f"SELECT * FROM workshop WHERE ID_Pemerintah = {ID_Pemerintah}"
                mycursor.execute(query_check_workshop)
                related_data = mycursor.fetchall()

                if related_data:
                    # Perbarui nilai foreign key di tabel workshop menjadi NULL atau nilai default yang sesuai
                    query_update_workshop = f"UPDATE workshop SET ID_Pemerintah = NULL WHERE ID_Pemerintah = {ID_Pemerintah}"
                    mycursor.execute(query_update_workshop)
                    mydb.commit()

                # Lakukan operasi penghapusan dari tabel pemerintah
                query_delete_pemerintah = f"DELETE FROM pemerintah WHERE ID_Pemerintah = {ID_Pemerintah}"
                mycursor.execute(query_delete_pemerintah)
                mydb.commit()
                print("Data pemerintah berhasil dihapus.\n")
                input("Tekan enter untuk kembali...")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!.")
                input("Tekan Enter untuk Kembali")
                # continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    # Mencari Data
    def mencari_data_workshop(self):
            try:
                clear()
                id_workshop = input("Masukkan ID Workshop yang ingin dicari: ")
                data_list = self.memeriksa_data_workshop()
                found = False
                for i, data in enumerate(data_list):
                    if str(data[0]) == id_workshop:  # Membandingkan ID workshop sebagai string
                        print("Data Workshop ditemukan:")
                        fields = ["ID_Workshop", "ID_Pemerintah", "ID_Admin", "ID_Anggota", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
                        self.display_table([data], fields)
                        found = True
                        break
                if not found:
                    print("Data Workshop tidak ditemukan")
                input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nOperasi dibatalkan oleh pengguna. Lanjutkan program...")
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    def mencari_data_anggota(self):
            try:
                clear()
                id_anggota = input("Masukkan ID Anggota yang ingin dicari: ")
                data_list = self.memeriksa_data_anggota()
                found = False
                for data in data_list:
                    if str(data[0]) == id_anggota:  # Membandingkan ID anggota sebagai string
                        print("Data Anggota ditemukan:")
                        fields = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
                        self.display_table([data], fields)
                        found = True
                        break
                if not found:
                    print("Data Anggota tidak ditemukan")
                input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    def mencari_data_umkm(self):
            try:
                clear()
                id_umkm = input("Masukkan ID UMKM yang ingin dicari: ")
                data_list = self.memeriksa_data_umkm()
                found = False
                for i, data in enumerate(data_list):
                    if str(data[0]) == id_umkm:  # Membandingkan ID workshop sebagai string
                        print("Data UMKM ditemukan:")
                        fields = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
                        self.display_table([data], fields)
                        found = True
                        input("Klik Enter untuk Kembali")
                        break
                if not found:
                    print("Data Workshop tidak ditemukan")
                    input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)
    
    def menu_mencari_data(self):
        while True:
            try:
                clear()
                print("============================")
                print("|      Mencari Data        |")
                print("============================")
                print("|  1. Data Workshop        |")
                print("|  2. Data Anggota         |")
                print("|  3. Data UMKM            |")
                print("|  4. Kembali              |")
                print("============================")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == '1':
                    self.mencari_data_workshop()
                elif pilihan == '2':
                    self.mencari_data_anggota()
                elif pilihan == '3':
                    self.mencari_data_umkm()
                elif pilihan == '4':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)
    # Mengurutkan Data
    def urut_data_workshop(self):
        while True:
            try:
                clear()
                print("=============================")
                print("|   Urutkan Data Workshop   |")
                print("=============================")
                print("|  1. Ascending             |")
                print("|  2. Descending            |")
                print("|  3. Kembali               |")
                print("=============================")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == '1':
                    ascending = True
                    break
                elif pilihan == '2':
                    ascending = False
                    break
                elif pilihan == '3':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
                input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)


        data_list = self.memeriksa_data_workshop()
        sorted_data = self.quick_sort(data_list, ascending)
        if sorted_data:
            print("Data Workshop yang Diurutkan:")
            fields = ["ID_Workshop", "ID_Pemerintah", "ID_Admin", "ID_Anggota", "Lembaga", "Waktu_Operasional", "Alamat_Workshop"]
            self.display_table(sorted_data, fields)
            input("Klik Enter untuk Kembali...")
        else:
            print("Data Workshop kosong")
            input("Klik Enter untuk Kembali...")

    def urut_data_anggota(self):
        while True:
            try:
                clear()
                print("=============================")
                print("|   Urutkan Data Anggota    |")
                print("=============================")
                print("|  1. Ascending             |")
                print("|  2. Descending            |")
                print("|  3. Kembali               |")
                print("=============================")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == '1':
                    ascending = True
                    break
                elif pilihan == '2':
                    ascending = False
                    break
                elif pilihan == '3':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
                input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

        clear()
        data_list = self.memeriksa_data_anggota()
        sorted_data = self.quick_sort(data_list, ascending)
        if sorted_data:
            print("Data Anggota yang Diurutkan:")
            fields = ["ID_Anggota", "ID_UMKM", "ID_Workshop", "Nama_Anggota", "Gender", "TTL", "No_Hp", "Password"]
            self.display_table(sorted_data, fields)
            input("Klik Enter untuk Kembali...")
        else:
            print("Data Anggota kosong")
            input("Klik Enter untuk Kembali...")

    def urut_data_umkm(self):
        while True:
            try:
                clear()
                print("=============================")
                print("|   Urutkan Data Anggota    |")
                print("=============================")
                print("|  1. Ascending             |")
                print("|  2. Descending            |")
                print("|  3. Kembali               |")
                print("=============================")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == '1':
                    ascending = True
                    break
                elif pilihan == '2':
                    ascending = False
                    break
                elif pilihan == '3':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
                input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

        clear()
        data_list = self.memeriksa_data_umkm()
        sorted_data = self.quick_sort(data_list, ascending)
        if sorted_data:
            print("Data UMKM yang Diurutkan:")
            fields = ["ID_UMKM", "Nama_Usaha", "Bidang_Usaha", "Produk_Usaha", "Slot_Karyawan", "Alamat", "No_HP"]
            self.display_table(sorted_data, fields)
            input("Klik Enter untuk Kembali...")
        else:
            print("Data Anggota kosong")
            input("Klik Enter untuk Kembali...")
    
    def menu_urut_data(self):
        while True:
            try:
                clear()
                print("=============================")
                print("|     Mengurutkan Data      |")
                print("=============================")
                print("|  1. Data Workshop         |")
                print("|  2. Data Anggota          |")
                print("|  3. Data UMKM             |")
                print("|  4. Kembali               |")
                print("=============================")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == '1':
                    self.urut_data_workshop()
                elif pilihan == '2':
                    self.urut_data_anggota()
                elif pilihan == '3':
                    self.urut_data_umkm()
                elif pilihan == '4':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
                    input("Klik Enter untuk Kembali")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

#Class Admin
class Admin:
    def __init__(self):
        pass

    # Metode untuk memeriksa kredensial admin di database
    def check_admin_credentials(self, id_admin, password):
        try:
            query = "SELECT * FROM admin WHERE ID_Admin = %s AND Password = %s"
            mycursor.execute(query, (id_admin, password))
            result = mycursor.fetchone()
            if result:
                return True
            return False
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    # Metode untuk login admin

    def login_admin(self):
        while True:
            clear()
            id_admin = input("Enter ID Admin: ")
            password = pwinput.pwinput("Enter Password: ")
            periksa_data_admin = self.check_admin_credentials(id_admin, password)
            if periksa_data_admin:
                clear()  # Bersihkan layar
                # Ambil data admin dari database dan tampilkan pesan selamat datang
                query = "SELECT Nama_Lengkap FROM admin WHERE ID_Admin = %s"
                mycursor.execute(query, (id_admin,))
                admin_data = mycursor.fetchone()
                if admin_data:
                    print("===================================================")
                    print("| >>>>>>>>>>>> Welcome to Workshop 3T <<<<<<<<<<< |")
                    print("===================================================")
                    print(f"Admin : {admin_data[0]}!           ")    # Tampilkan pesan welcome
                    input("\nKlik Enter Untuk Melanjutkan ke Menu Utama Admin...")  # Tambahkan jeda
                    self.menu_utama_admin()
                    break
                else:
                    print("Data admin tidak ditemukan")
                    input("Klik Enter untuk Kembali")
            else:
                print("ID Admin atau Kata Sandi tidak valid")
                input("Klik Enter untuk Kembali")
                break

    # Menu Utama admin
    def menu_utama_admin(self):
        linked_list = LinkedList()  # Membuat instance LinkedList
        while True:
            try:
                clear()
                print("================================")
                print("|       Menu Utama Admin       |")
                print("================================")
                print("| 1. Tambahkan UMKM            |")
                print("| 2. Memeriksa Data            |")
                print("| 3. Memperbarui Data          |")
                print("| 4. Menghapus Data            |")
                print("| 5. Mencari Data              |")
                print("| 6. Mengurutkan Data          |")
                print("| 7. Kembali                   |")
                print("===============================")
                pilput_admn = input("Masukkan pilihan Anda: ")

                if pilput_admn == '1':
                    linked_list = LinkedList()
                    linked_list.tambah_umkm()  
                elif pilput_admn == '2':
                    linked_list = LinkedList()
                    linked_list.menu_memeriksa_data()  
                elif pilput_admn == '3':
                    linked_list = LinkedList()
                    linked_list.menu_memperbarui_data() 
                elif pilput_admn == '4':
                    linked_list = LinkedList()
                    linked_list.menu_menghapus_data()  
                elif pilput_admn == '5':
                    linked_list = LinkedList()
                    linked_list.menu_mencari_data()
                elif pilput_admn == '6':
                    linked_list = LinkedList()
                    linked_list.menu_urut_data()                
                elif pilput_admn == '7':
                    return
                else:
                    print("Input tidak valid, harap masukkan pilihan yang valid!")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 

# # Kelas User
class User:
    def __init__(self, database):
        self.database = database
        self.id_anggota = None  # Tambahkan variabel untuk menyimpan ID Anggota setelah login berhasil
        self.cursor = self.database.cursor()
        self.umkm_list = LinkedList()  # Linked list untuk menyimpan daftar UMKM

    def get_anggota_info(self):
        try:
            query = """
            SELECT anggota.ID_Anggota, anggota.Nama_Anggota, anggota.Gender, anggota.TTL, anggota.No_HP, 
                IFNULL(umkm.Nama_Usaha, 'Belum Terdaftar') AS Nama_Usaha, 
                IFNULL(workshop.Lembaga, 'Belum Terdaftar') Lembaga
            FROM anggota
            LEFT JOIN umkm ON anggota.ID_UMKM = umkm.ID_UMKM
            LEFT JOIN workshop ON anggota.ID_Workshop = workshop.ID_Workshop
            WHERE anggota.ID_Anggota = %s
            """
            self.cursor.execute(query, (self.id_anggota,))
            result = self.cursor.fetchone()

            if result:
                # Menampilkan hasil query
                print("ID Anggota:", result[0])
                print("Nama Anggota:", result[1])
                print("Gender:", result[2])
                print("TTL:", result[3])
                print("No HP:", result[4])
                print("Nama Usaha:", result[5])
                print("Nama Lembaga:", result[6])
            else:
                print("Data anggota tidak ditemukan.")
        except mysql.connector.Error as err:
            print("Error:", err)


    
    def check_user_credentials(self, id_anggota, password):
        try:
            query = "SELECT ID_Anggota, Password FROM anggota WHERE ID_Anggota = %s AND Password = %s"
            mycursor.execute(query, (id_anggota,password))
            result = mycursor.fetchone()
            if result:
                if result[1] == password:
                    return True
            return False
        except mysql.connector.Error as err:
            print("Error:", err)
            input("Klik Enter untuk Kembali...")
            return False


    def register_user(self):
        while True:
            try:
                # Menampilkan contoh ID Anggota
                print("Contoh: 2001")

                # Meminta pengguna untuk memasukkan ID Anggota
                id_anggota = input("Masukkan ID Anggota Anda: ")

                # Melakukan pengecekan apakah ID anggota sudah ada dalam database
                query_check_id = "SELECT ID_Anggota FROM anggota WHERE ID_Anggota = %s"
                self.cursor.execute(query_check_id, (id_anggota,))
                existing_id = self.cursor.fetchone()
                
                if existing_id:
                    print("ID Anggota sudah ada dalam database. Mohon masukkan ID yang berbeda.")
                    continue  # Melanjutkan loop untuk meminta input ID yang berbeda
                
                # Meminta pengguna untuk memasukkan data diri mereka
                nama = input("Masukkan Nama Anda: ")
                gender = input("Masukkan Jenis Kelamin Anda: ")
                ttl = input("Masukkan Tanggal Lahir Anda (Format: YYYY-MM-DD): ")
                no_hp = input("Masukkan Nomor HP Anda: ")
                password = input("Masukkan Password Anda: ")
                
                # Melakukan validasi data yang dimasukkan pengguna jika diperlukan
                
                # Melakukan registrasi pengguna
                query = "INSERT INTO anggota (ID_Anggota, Nama_Anggota, Gender, TTL, No_HP, Password) VALUES (%s, %s, %s, %s, %s, %s)"
                self.cursor.execute(query, (id_anggota, nama, gender, ttl, no_hp, password))
                self.database.commit()  # Menggunakan self.database, bukan self.mydb
                
                print("Registrasi pengguna berhasil!")
                break  # Keluar dari loop setelah registrasi berhasil

            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

        input("Klik Enter untuk Kembali")


    
    def login(self):
        while True:
            try:
                clear()
                id_anggota = input("Enter ID Anggota: ")
                password_akun = pwinput.pwinput("Enter Password: ")
                if self.check_user_credentials(id_anggota, password_akun):  
                    self.id_anggota = id_anggota
                    self.get_umkm_membership()
                    self.menu_utama_user()
                else:
                    print("ID Anggota atau Kata Sandi tidak valid")
                    input("Klik Enter untuk Kembali...")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

    def get_umkm_membership(self):
        try:
            # Query untuk mengambil ID UMKM di mana anggota terdaftar
            query = "SELECT ID_UMKM FROM anggota WHERE ID_Anggota = %s"
            self.cursor.execute(query, (self.id_anggota,))
            umkm_id = self.cursor.fetchone()
            if umkm_id:
                self.umkm_id = umkm_id[0]
            else:
                print("Anggota tidak terdaftar di UMKM manapun.")
        except mysql.connector.Error as err:
            print("Error:", err)
            
    def display_workshop_list(self):
        try:
            # Query untuk mengambil daftar workshop yang tersedia
            query = "SELECT ID_Workshop, Lembaga FROM workshop"
            self.cursor.execute(query)
            workshop_list = self.cursor.fetchall()

            if workshop_list:
                # Membuat objek PrettyTable untuk menampilkan daftar workshop
                table = PrettyTable(["ID Workshop", "Nama Lembaga"])
                
                # Menambahkan setiap workshop ke dalam tabel
                for workshop in workshop_list:
                    table.add_row(workshop)
                
                # Mengatur format tabel
                table.align = 'l'  # Mengatur teks menjadi rata kiri
                
                # Menampilkan tabel
                print("Daftar Workshop yang Tersedia:")
                print(table)
            else:
                print("Belum ada workshop yang tersedia.")
        except mysql.connector.Error as err:
            print("Error:", err)
            
    def display_umkm_list(self):
        try:
            # Query untuk mengambil daftar UMKM yang tersedia
            query = "SELECT ID_UMKM, Nama_Usaha, Bidang_Usaha, Produk_Usaha, Slot_Karyawan FROM umkm"
            self.cursor.execute(query)
            umkm_list = self.cursor.fetchall()

            if umkm_list:
                # Membuat objek PrettyTable untuk menampilkan daftar UMKM
                table = PrettyTable(["ID UMKM", "Nama Usaha", "Bidang Usaha", "Produk Usaha", "Slot Karyawan"])
                
                # Menambahkan setiap UMKM ke dalam tabel
                for umkm in umkm_list:
                    table.add_row(umkm)
                
                # Mengatur format tabel
                table.align = 'l'  # Mengatur teks menjadi rata kiri
                
                # Menampilkan tabel
                print("Daftar UMKM yang Tersedia:")
                print(table)
            else:
                print("Belum ada UMKM yang tersedia.")
        except mysql.connector.Error as err:
            print("Error:", err)
    
    def display_umkm_details(self, umkm_id):
        try:
            if umkm_id:
                # Query untuk mengambil detail UMKM
                query = "SELECT Nama_Usaha, Bidang_Usaha, Alamat, No_HP FROM umkm WHERE ID_UMKM = %s"
                self.cursor.execute(query, (umkm_id,))
                umkm_details = self.cursor.fetchone()

                if umkm_details:
                    # Menampilkan detail UMKM
                    print("Anggota terdaftar di UMKM berikut:")
                    print(f"Nama Usaha: {umkm_details[0]}")
                    print(f"Bidang Usaha: {umkm_details[1]}")
                    print(f"Alamat: {umkm_details[2]}")
                    print(f"No HP: {umkm_details[3]}")
                else:
                    print("Detail UMKM tidak ditemukan.")
            else:
                print("ID UMKM tidak valid.")
        except mysql.connector.Error as err:
            print("Error:", err)
    
    def register_workshop(self):

        while True:
            try:
                # Periksa apakah anggota sudah terdaftar di suatu workshop
                query_check_registration = "SELECT ID_Workshop FROM anggota WHERE ID_Anggota = %s AND ID_Workshop IS NOT NULL"
                self.cursor.execute(query_check_registration, (self.id_anggota,))
                existing_registration = self.cursor.fetchone()
                
                if existing_registration:
                    # Jika sudah terdaftar di sebuah workshop, tampilkan informasi workshop yang sudah didaftarkan
                    workshop_id = existing_registration[0]
                    query_get_workshop_info = "SELECT Lembaga FROM workshop WHERE ID_Workshop = %s"
                    self.cursor.execute(query_get_workshop_info, (workshop_id,))
                    workshop_info = self.cursor.fetchone()

                    print("Anda sudah terdaftar di workshop", workshop_info[0])
                    change_workshop = input("Apakah Anda ingin berpindah workshop? (y/n): ")

                    if change_workshop.lower() == 'n':
                        return

                # Menampilkan daftar workshop yang tersedia
                self.display_workshop_list()
                
                # Meminta pengguna untuk memasukkan ID workshop yang ingin mereka daftarkan
                while True:
                    workshop_id = input("Masukkan ID Workshop yang ingin Anda daftarkan (atau ketik 'b' untuk kembali): ")
                    
                    if workshop_id.lower() == 'b':
                        return  # Kembali ke menu utama jika pengguna memilih untuk membatalkan pendaftaran workshop
                    elif not workshop_id.isdigit():
                        print("Masukkan ID Workshop dengan benar.")
                        continue  # Lanjutkan loop jika input tidak valid
                    else:
                        # Keluar dari loop jika input valid
                        break

                # Menampilkan detail workshop yang dipilih
                query_display_workshop_details = "SELECT * FROM workshop WHERE ID_Workshop = %s"
                self.cursor.execute(query_display_workshop_details, (workshop_id,))
                workshop_details = self.cursor.fetchone()
                
                if workshop_details:
                    print("Detail Workshop:")
                    print("ID Workshop:", workshop_details[0])
                    print("Lembaga:", workshop_details[3])
                    print("Waktu Operasional:", workshop_details[4])
                    print("Alamat Workshop:", workshop_details[5])
                else:
                    print("Workshop dengan ID tersebut tidak ditemukan.")
                    return

                # Meminta konfirmasi dari pengguna untuk mendaftar workshop
                confirm = input("Apakah Anda yakin ingin mendaftar workshop ini? (y/n): ")
                if confirm.lower() == 'y':
                    # Melakukan pendaftaran workshop
                    query_register_workshop = "UPDATE anggota SET ID_Workshop = %s WHERE ID_Anggota = %s"
                    self.cursor.execute(query_register_workshop, (workshop_id, self.id_anggota))
                    self.database.commit()

                    print("Pendaftaran workshop berhasil!")
                else:
                    print("Pendaftaran workshop dibatalkan.")
                
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

        input("Klik Enter untuk Kembali")
    
    def register_umkm(self):

        while True:
            try:
            # Periksa apakah anggota sudah terdaftar di suatu UMKM
                query_check_membership = "SELECT ID_UMKM FROM anggota WHERE ID_Anggota = %s AND ID_UMKM IS NOT NULL"
                self.cursor.execute(query_check_membership, (self.id_anggota,))
                current_umkm = self.cursor.fetchone()
                
                if current_umkm:
                    # Jika sudah terdaftar di sebuah UMKM, tampilkan informasi UMKM yang sudah didaftarkan
                    umkm_id = current_umkm[0]
                    query_get_umkm_info = "SELECT Nama_Usaha FROM umkm WHERE ID_UMKM = %s"
                    self.cursor.execute(query_get_umkm_info, (umkm_id,))
                    umkm_info = self.cursor.fetchone()

                    print("Anda sudah terdaftar di UMKM", umkm_info[0])
                    change_umkm = input("Apakah Anda ingin berganti UMKM? (y/n): ")

                    if change_umkm.lower() == 'n':
                        return

                # Menampilkan daftar UMKM yang tersedia
                self.display_umkm_list()
                
                # Meminta pengguna untuk memasukkan ID UMKM yang ingin mereka daftarkan
                while True:
                    umkm_id = input("Masukkan ID UMKM yang ingin Anda daftarkan (atau ketik 'b' untuk kembali): ")
                    
                    if umkm_id.lower() == 'b':
                        return  # Kembali ke menu utama jika pengguna memilih untuk membatalkan pendaftaran UMKM
                    elif not umkm_id.isdigit():
                        print("Masukkan ID UMKM dengan benar.")
                        continue  # Lanjutkan loop jika input tidak valid
                    else:
                        # Keluar dari loop jika input valid
                        break

                # Menampilkan detail UMKM yang dipilih
                query_display_umkm_details = "SELECT * FROM umkm WHERE ID_UMKM = %s"
                self.cursor.execute(query_display_umkm_details, (umkm_id,))
                umkm_details = self.cursor.fetchone()
                
                if umkm_details:
                    print("Detail UMKM:")
                    print("ID UMKM:", umkm_details[0])
                    print("Nama UMKM:", umkm_details[1])
                    print("Alamat UMKM:", umkm_details[2])
                    print("Deskripsi UMKM:", umkm_details[3])
                else:
                    print("UMKM dengan ID tersebut tidak ditemukan.")
                    return

                # Meminta konfirmasi dari pengguna untuk mendaftar UMKM
                confirm = input("Apakah Anda yakin ingin mendaftar UMKM ini? (y/n): ")
                if confirm.lower() == 'y':
                    # Melakukan pendaftaran UMKM
                    query_register_umkm = "UPDATE anggota SET ID_UMKM = %s WHERE ID_Anggota = %s"
                    self.cursor.execute(query_register_umkm, (umkm_id, self.id_anggota))
                    self.database.commit()

                    print("Pendaftaran UMKM berhasil!")
                else:
                    print("Pendaftaran UMKM dibatalkan.")
                
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

        input("Klik Enter untuk Kembali")
    
    def menu_utama_user(self):
        while True:
            try:
                clear()
                print("===========================")
                print("|       Menu User         |")
                print("===========================")
                print("|  1. Mendaftar UMKM      |")
                print("|  2. Mendaftar Workshop  |")
                print("|  3. Memeriksa Data Diri |")
                print("|  4. Kembali             |")
                print("===========================")
                user_menu = input("Masukkan Pilihan Anda: ")

                if user_menu == '1':
                    self.register_umkm()
                elif user_menu == '2':
                    self.register_workshop()
                elif user_menu == '3':
                    clear()
                    print("Biodata Anggota beserta jenis UMKM :")
                    self.get_anggota_info() 
                    input("Klik Enter untuk Kembali")
                elif user_menu == '4':
                    return
                else:
                    print("Input Tidak Valid, Mohon Masukkan Input Dengan Benar!")
            except KeyboardInterrupt:
                print("\nSilahkan Melakukan Input Dengan Benar!")
                input("Tekan Enter untuk Kembali")
                continue
            except Exception as e:
                print(f"Terjadi kesalahan tak terduga: {e}") 
            except mysql.connector.Error as err:
                print("Error:", err)

# Menu untuk pengguna
def user_menu(database):
    
    while True:
        try:
            clear()
            print("=========================")
            print("|     Menu Awal User    |")
            print("=========================")
            print("|  1. Login User        |")
            print("|  2. Register User     |")
            print("|  3. Kembali           |")
            print("=========================")
            user_menu = input("Masukkan Pilihan Anda: ")

            if user_menu == '1':
                user = User(database)
                user.login()
            elif user_menu == '2':
                user = User(database)
                user.register_user()
            elif user_menu == '3':
                return
            else:
                print("Input Tidak Valid, Mohon Masukkan Input Dengan Benar!")
        except KeyboardInterrupt:
            print("\nSilahkan Melakukan Input Dengan Benar!")
            input("Tekan Enter untuk Kembali")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}") 
        except mysql.connector.Error as err:
            print("Error:", err)

# Menu utama
def main_menu(database):
    while True:
        try:
            clear()
            print("=========================")
            print("|      WORKSHOP 3T      |")
            print("=========================")
            print("|       Main Menu       |")
            print("=========================")
            print("|  1. Admin             |")
            print("|  2. User              |")
            print("|  3. Exit              |")
            print("=========================")
            pilput = input("Masukkan Pilihan yang Anda Ingingkan : ")

            if pilput == '1':
                admin = Admin()
                admin.login_admin()
            elif pilput == '2':
                user_menu(database)
            elif pilput == '3':
                clear()
                print("---------------------------------")
                print("| Program Layanan Telah Selesai |")
                print("---------------------------------")
                break
            else:
                print("Input Tidak Valid, Mohon Masukkan Input Dengan Benar!")
    
        except KeyboardInterrupt:
            print("\nSilahkan Melakukan Input Dengan Benar!")
            input("Tekan Enter untuk melanjutkan")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}") 
        except mysql.connector.Error as err:
            print("Error:", err)

# Jalankan program
if __name__ == "__main__":
    main_menu(mydb)
