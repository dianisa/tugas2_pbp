Nama		: Dianisa Wulandari<br>
NPM		    : 2106702150<br>
Kelas		: F<br>
Kode Asdos	: LAH<br>

Link Heroku : https://tugas-pbp-dian.herokuapp.com/todolist/

####Tugas 4
- Apa kegunaan {% csrf_token %} pada elemen \<form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen \<form>?

{% csrf_token %} berfungsi untuk melindungi user dari pemalsuan request dengan cara menambahkan token pada setiap request yang dikirim user. Tanpa {% csrf_token %}, \<form> dapat diakses dengan mudah oleh pihak luar melalui website lain dengan cara mengirim request palsu ke \<form>. Contoh:

Kamu login ke website A. Setelah itu, kamu membuka website B. Website B dapat mengirim request ke website A dan website A memproses request tersebut tanpa memperhatikan dari mana request tersebut datang.

Dengan {% csrf_token %}, website A akan mencantumkan sebuah token tambahan pada setiap request yang dibuat user. Bila token tidak sesuai (ada pemalsuan), maka request tersebut tidak akan diproses oleh website A.

- Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

{{form.as_table}} akan merender elemen form menjadi sebuah tabel. Berikut langkah untuk membuatnya secara manual:
1. Buat tag \<table> dan endtag \</table> pada file HTML milik form
2. Buat setiap baris tabel dengan menyisipkan tag \<tr> dan endtag \</tr> di antara tag \<table> dan endtag \</table>
3. Buat setiap table cell pada sebuah baris tabel dengan menyisipkan \<td> dan </td> di antara sebuah \<tr> dan \</tr>
4. Terakhir, masukkan elemen di antara tag \<td> dan \</td>. Untuk membuat sebuah tulisan, langsung tulis saja di antara tag \<td> dan \</td> atau di antara tag \<label>. Contoh:<br>
\<td> Contoh tulisan \</td><br>
Untuk membuat input (dapat berupa button, checkbox, password, submit, dll), buat \<input (parameter)> di antara tag \<td> dan \</td>. Contoh dari parameter adalah type, id, value, name, size, placeholder, dll. Contoh:<br>
\<td>\<input required type="text" name="contoh_input" placeholder="Masukkan input" class="form-control">\</td>

- Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1. User memasukkan data melalui input pada form HTML. Form tersebut mengirim request POST.
2. Pada sebuah views function, ambil hasil input user dengan cara:
request.POST.get('\<name>')
Pastikan \<name> sesuai dengan parameter name yang ada di input HTML.
3. Buat sebuah object dari models yang sudah dibuat dan isi atribut-atributnya berdasarkan input user. Jangan lupa untuk menyimpannya dengan \<object>.save(). Kini data sudah tersimpan di database.
4. Untuk menampilkan data, buat sebuah variabel dan assign dengan \<model>.objects.all(). Variabel tersebut akan berisi semua data dan dapat diiterasi.
5. Pasangkan variabel tersebut dengan sebuah key di dictionary context, lalu kirim context ke file HTML melalui fungsi render().
6. File HTML dapat mengakses dan menampilkan data yang ada di context dengan cara memanggil keynya.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buka repositori lokal dari project tugas django dan aktivasi virtual environment. Buat app baru dengan perintah python manage.py startapp \<nama_app>. Kemudian, daftarkan nama app ke INSTALLED_APPS di settings.py pada folder project_django.
2. tambahkan path('todolist/', include('todolist.urls')) ke urlpatterns di urls.py pada folder project_django.
3. buat class Task(models.Model) di file models.py. Isi dengan atribut user, date, title, dan description. Assign datafield yang sesuai ke semua atribut. Untuk atribut user, assign models.ForeignKey(User, on_delete=models.CASCADE).
4. Buat masing-masing function pada views.py untuk melakukan login, register, dan logout. Pastikan bahwa user harus login. Kemudian, function register dan logout akan me-redirect user kembali ke login.
5. Pada function di views.py yang meng-handle halaman todolist, ambil user yang sedang aktif dengan request.user serta ambil data pada database dengan \<model>.objects.all(). Simpan user dan data ke dictionary context dan kirimkan context ke file HTML dengan fungsi render(). Pada file HTML todolist.html, akses dan tampilkan data yang ada pada context dengan menggunakan keynya. Buat tombol create task dan logout dengan menambahkan:<br>
\<button>\<a href="{% url 'todolist:<fungsi views>' %}">\<nama_tombol>\</a>\</button>
6. Buat sebuah file HTML yang mengirimkan request POST dan dapat menerima input judul dan deskripsi dari user. Untuk mmebuat input dapat menggunakan:<br>
\<input required type="<type>" name="<nama_input>" placeholder="<placeholder>" class="form-control"><br>
Pada fungsi di views.py yang menghandle create task, buat variabel yang akan menmpung tanggal pembuatan task. Assign variabel tersebut dengan datetime.date.today(). Kemudian, buat sebuah object model dan ambil data input user dengan request.POST.get('\<nama_input>'). Setelah itu, masukkan data ke atribut dari object yang dibuat. Jangan lupa untuk melakukan save dengan \<object>.save().
7. Buat routing dengan menambahkan:<br>
path('<nama_path>/', \<function_views>, name='\<function_views>')<br>
ke urlpatterns di urls.py pada folder todolist.
8. Karena menggunakan repository yang sama dengan tugas 2 dan 3, maka cukup push ke repository github dan aplikasi bisa langsung diakses.
9. CreateSuperUser di bash heroku untuk membuat akun admin. Masuk ke \<nama_app>.herokuapp.com/admin/ dan buat users serta tambahkan datanya.