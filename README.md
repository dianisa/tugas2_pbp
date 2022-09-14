Nama        : Dianisa Wulandari

NPM         : 2106702150

Kelas       : PBP A

Kode Asdos  : LAH

Link Heroku : https://katalog-tugas2pbp.herokuapp.com/katalog/

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![client request django drawio](https://user-images.githubusercontent.com/92663592/190253648-b7a19305-1477-4111-9c72-266e5ec7a21c.png)

Request yang diterima dari client akan dirouting oleh urls.py ke views.py. File views.py berisi function yang menerima HttpRequest dan mengembalikan HttpResponse. Apabila terdapat request untuk read/write data, views.py akan berinteraksi dengan models.py. File models.py berisi data yang sudah diambil dari database. Kemudian, data akan dimasukkan ke katalog.html dan web page bisa ditampilkan

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk menciptakan lingkungan yang eksklusif bagi suatu program. Perubahan-perubahan yang terjadi di luar virtual environment tidak akan memengaruhi keadaan virtual environment itu. Seiring berjalannya waktu, banyak terjadi perubahan pada modul-modul yang digunakan untuk membuat suatu program. Hal ini bisa menyebabkan program yang dahulu dibuat menjadi tidak compatible dengan modul-modul yang sudah mengalami perubahan tersebut. Dengan adanya virtual environment, kita dapat menyimpan modul-modul yang compatible saja dengan program tersebut. Kita tetap dapat membuat aplikasi web berbasis Django tanpa virtual environment. Akan tetapi, program harus disesuaikan kembali apabila terjadi perubahan pada modul-modul yang digunakan.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Pada views.py, dibuat sebuah fungsi yang akan menerima HttpRequest, mengambil data dari models.py dan mereturn HttpResponse. Pengambilan data dilakukan dengan cara memanggil CatalogItem.objects.all() dan menyimpannya dalam variabel data_barang_katalog. Kemudian, dibuat dictionary context untuk menyimpan data_barang_katalog. Dictionary tersebut akan ditampilkan pada file katalog.html dengan proses looping.
2. Routing dilakukan dengan mendaftarkan fungsi path('', show_katalog, name='show_katalog') pada list urlpatterns. fungsi path akan melakukan routing ke fungsi pada views.py yang sesuai dan mengembalikan urlpattern.
3. Pemetaan data ke katalog.html dilakukan dengan looping. QuerySet yang tersimpan dengan key item_katalog akan diloop dan ditampilkan seluruh attributenya (item_name, item_price, item_stock, rating, description, item_url)
4. Pertama, push seluruh file program yang sudah dibuat ke github. kedua, buat aplikasi di heroku dengan menekan tombol create new app. ketiga, copy API key dari heroku dan simpan sebagai secrets di github. Buat secrets yang berisi nama aplikasi sesuai yang terdaftar pada heroku juga. Terakhir, jalankan kembali workflow commit dan deployment di github. 
