Nama		: Dianisa Wulandari<br>
NPM		    : 2106702150<br>
Kelas		: F<br>
Kode Asdos	: LAH<br>

Link Heroku : https://tugas-pbp-dian.herokuapp.com/todolist/

####Tugas 6

- Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada synchronous programming, eksekusi setiap task/request dilakukan secara sequential. Task selanjutnya tidak akan dilakukan apabila task sebelumnya belum selesai. Dengan kata lain, program hanya mengeksekusi satu task pada satu waktu. Sedangkan, asynchronou programming dapat mengeksekusi task/request selanjutnya walaupun task sebelumnya belum selesai dieksekusi.

- Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Pada event-driven programming, program dapat merespon hal-hal yang dilakukan user seperti kik tombol. Pada tugas ini, salah satu contohnya ada pada tombol create task.

- Jelaskan penerapan asynchronous programming pada AJAX.

Saat sebuah event terjadi, JavaScript akan membuat XMLHttpRequest. request ini akan diproses dan direspon kembali ke halaman web. respon tersebut akan diterima dan diproses oleh JavaScript. Dengan ajax, data dapat diupdate tanpa menunggu halaman web direload. Sehingga, halaman web dapat diupdate secara asynchronous.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

 1. AJAX GET
    a. Buat sebuah view  yang akan mengembalikan data dalam bentuk json dan buat sebuah path yang mengarah ke view tersebut.

    b. Buat function getTodolist() yang akan mengambil data json dari view tersebut dengan memanfaatkan fetch. Kemudian, data tersebut akan disimpan pada sebuah variabel di function refershTodolist(). Iterasi setiap data pada variabel tersebut dan tampilkan dengan card.

 2. AJAX POST
    a. Buat tombol yang akan membuka sebuah modal untuk membuat todolist baru. Pada modal tersebut, buat sebuah form yang akan menerima task title dan task description. Buat pula tombol submit dan letakkan data-bs-dismiss="modal" pada tombol tersebut agar modal langsung tertutup setelah berhasil menambahkan task.

    b. Buat sebuah view yang akan mengambil data input dengan request.POST.get(\<nama_field_input>). Buat object Task baru dan simpan ke database dengan \<nama_object>.save(). Buat sebuah path yang mengarah ke view tersebut.

    c. Buat function addTodolist() yang akan melakukan fetch terhadap view tersebut dan mengirim method POST. Sehingga, saat function addTodolist() dipanggil maka view tersebut akan dijalankan.
    
    d. Panggil function refereshTodolist() di dalam function addTodolist() agar halaman web diupdate secara asinkronus setelah penambahan task dilakukan.