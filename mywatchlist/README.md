Nama		: Dianisa Wulandari

NPM		    : 2106702150

Kelas		: F

Kode Asdos	: LAH

Link Heroku : https://tugas-pbp-dian.herokuapp.com/mywatchlist/

Tugas 3

- Jelaskan perbedaan antara JSON, XML, dan HTML!

HTML (Hyper Text Markup Language) adalah markup language yang berfungsi untuk mengatur tata letak elemen sebuah website. XML (Extensive Markup Language) adalah markup language yang berfungsi untuk menyimpan dan mengirim data. Sementara itu, JSON (JavaScript Object Notation) adalah format yang menyimpan dan menampilkan data. 

- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan agar client dapat berkomunikasi dengan server. Data yang disimpan dan diolah di server harus dikirimkan ke client agar dapat ditampilkan sesuai request user.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buka direktori proyek Django pada command prompt dan jalankan command python manage.py startapp wishlist. Kemudian, tambahkan 'mywatchlist' ke variabel INSTALLED_APPS di file settings.py.
2. Menambahkan 'path('mywatchlist/', include('mywatchlist.urls'))' ke list urlpatters di file urls.py pada folder project_django dan menambahkan ' path('', show_mywatchlist, name='show_mywatchlist')' ke list urlpatters di file urls.py pada folder mywatchlist.
3. Pada file models.py di folder mywatchlist, buat class MyWatchList. Daftarkan atributnya seperti watched, title, rating, release_date, dan review. Masukkan field yang sesuai dengan atributnya.
4. Buat folder fixtures di dalam folder mywatchlist. Kemudian, buat file initial_mywatchlist_data.json dan isi dengan data yang dibutuhkan.
5. Buat sebuah fungsi routing show_mywatchlist_json_xml yang akan mengembalikan "application/json" apabila memanggil path json/ dan mengembalikan "application/xml" apabila memanggil path xml/.
6. Buka urls.py di folder mywatchlist dan tambahkan path('html/', show_mywatchlist, name='show_mywatchlist'), path('xml/', show_mywatchlist_json_xml, name='show_mywatchlist_json_xml'), serta path('json/', show_mywatchlist_json_xml, name='show_mywatchlist_json_xml') ke list urlpatterns. Jika mengakses path 'html/', show_mywatchlist akan dipanggil. Jika mengakses path 'xml/' atau 'json/', show_mywatchlist_json_xml akan dipanggil.
7. Karena menggunakan repository yang sama dengan tugas 2, maka cukup push folder mywatchlist ke github dan aplikasi bisa langsung diakses.

Postman:

![messageImage_1663770217464](https://user-images.githubusercontent.com/92663592/191530633-35c27ef4-4f3e-48d3-906c-a8d9275e17e3.jpg)

![messageImage_1663770179014](https://user-images.githubusercontent.com/92663592/191530785-a73c5452-e8b1-443c-8849-82630c0fd018.jpg)

![messageImage_1663770143936](https://user-images.githubusercontent.com/92663592/191530864-0b9dad5a-8eae-4feb-a609-7f0486c12218.jpg)