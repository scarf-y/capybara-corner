### PWS LINK: http://daffa-naufal-capybarascorner.pbp.cs.ui.ac.id ###
## Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

========================= 1 =========================<br />
- langkah paling pertama yang saya lakukan adalah menentukan nama proyek django yang akan saya lakukan, setelah itu saya buat directory nya di local file
- pada directory tersebut saya buat python virtual environment dengan command berikut ``python -m venv env``
- dalam implementasi checklist ini saya mostly lakukan dengan terminal (Powershell) dan edit file lewat VScode
- Setiap ingin mengerjakan projek django, saya tidak lupa mengaktifkan environment tadi dalam terminal saya
- Selanjutnya saya siapkan dependencies yang diperlukan dalam pembuatan proyek django, seperti menginstall library/package yang ada di file *requirements.txt* yang saya buat lewat command ``pip install -r requirements.txt``
- lalu saya buat proyek djangonya dengan command ini ``django-admin startproject capybaras_corner .``
- kemudian, dalam *settings.py* yang ada pada file proyek, saya tambahkan beberapa host seperti localhost yang bertujuan untuk mengecek proyek saya tanpa harus langsung mendeploy ke PWS
- untuk menjalankan proyek saya pada local dapat dilakukan dengan command ini ``python manage.py runserver``
- pada tahap ini dasar proyek djangonya sudah terbentuk, kemudian saya buat repository githubnya. pada direktori utama saya lakukan git init, bertujuan untuk meng-enable fungsionalitas git pada direktori tersebut
- lalu tinggal kita hubungkan repository pada github ke direktori lokal, untuk branch utamanya saya langsung namai master
- sebelum itu saya telah buat file *.gitignore*, baru saya lakukan git add, git commit, git push pertama saya dalam projek django ini
- lalu saya mulai membuat aplikasi pertama yang dinamai `main` lewat command berikut: ``python manage.py startapp main``. kemudian saya daftarkan aplikasi nya ke *settings.py* di direktori proyek
- di dalam direktori main, saya buat direktori baru bernama templates yang berisi fila html yang nantinya digunakan sebagai tampilan yang dilihat user.
- selanjutnya saya edit *models.py* aplikasi saya yang ada di direktori main. Untuk hal ini saya hanya intialize variable/atribut dasar saja (lengkap dengan fieldnya)
- setiap perubahan pada models, saya buat migrations file yang berisi perubahan itu dengan ``python manage.py makemigrations``
- kemudian, baru saya migrate berkas itu ke database dengan ``python manage.py migrate`` 
- lalu, saya hubungkan komponen *views* dengan *templates* aplikasi main, lewat mengedit file *views.py*. Dalam file tersebut saya tambahkan fungsi show_main yang berisi dictionary yang bisa digunakan dalam kode html saya, lalu saya buat hasil return nya dengan render, yang akan mengambil http request user yang lewat *views.py* akan menampilkan *main.html*
- setelah itu, saya modifikasi *main.html* nya dengan syntax python django, yang ditandai dengan ``{{ ... }}``
- kemudian, saya atur jalur URL agar aplikasinya dapat diakses lewat web browser. pengaturan url pada tingkat proyek yaitu dengan mengedit *urls.py* dalam direktori main
- kemudian tambahkan urlpatterns dari url aplikasi ke *urls.py* milik direktori proyek.
- setelah semua siap, dan direktorinya sesuai dengan yang dianjurkan saya coba commit ke github
- langkah terakhir yaitu deploy proyek django saya ke pws, pertama saya buat proyek baru dan add remote pws baru
- lalu untuk mendeploy nya saya push proyeknya ke pws dengan ``git push pws master`` (main branch saya namanya dari awal master)
- akhirnya, untuk melihat hasilnya saya bisa klik ``view project`` dalam projek di pws nya. (meskipun sejauh ini masih error, build successful tapi tidak bisa dilihat)

========================= 2 =========================<br />
![bagan django](photos/baganDjangoDaffa.png)<br />
========================= 3 =========================<br />
Git membantu dalam pengembangan perangkat lunak karena punya kemampuan untuk mengelola perubahan kode, membuat kolaborasi tim menjadi mudah, menghindari konflik kode, dan memastikan kode proyek selalu dapat dipulihkan. Dalam proyek besar yang dikerjakan banyak sekali programmer, git dibutuhkan agar programmernya bisa bekerja dengan lebih efisien dan teroganisir.
Berikut fungsi utama git yang membantu dalam pengembangan perangkat lunak:
- pengelolaan proyek dengan remote repository
- kemudahan kolaborasi dalam tim
- versi kontrol
- backup dan recovery data/file
- audit dan transparansi (terlihat siapa saja yang terlibat dalam pengembangan dan penulisan kodenya)
- menerapkan perubahan dengan aman (lewat pull request dan merge request)

========================= 4 =========================<br />
- django menggunakan bahasa python sebagai dasarnya, yang mana dikenal sebagai bahasa pemrograman yang *newbie friendly*
- django sudah menyiapkan segala macam komponen utama yang diperlukan untuk mengembangkan aplikasi web dari awal hingga akhir
- sesuai poin sebelumnya, ini mempercepat pengembangan, yang mana kita bisa dengan cepat melihat dampak/hasil dari kode kita pada aplikasi webnya
- struktur MVT django memperkenalkan konsep yang (menurut saya) mudah diterima dalam hal pemisahan komponen logis-logisnya
- django ialah framework web yang terkenal, banyak yang memakai. sumber->[sumber](https://blog.jetbrains.com/pycharm/2024/06/the-state-of-django/#:~:text=Developing%20APIs%3A%20Most%20developers%20use,work%20among%20fully%20employed%20devs.)
- dengan banyak yang memakai, komunitas django menjadi besar dan sudah banyak programmer lain yang mungkin mengalami masalah serupa juga sudah ketemu solusinya

========================= 5 =========================<br />
Model pada Django disebut sebagai ORM karena data kita dalam database ditunjukkan lewat classes dan field yang memungkinkan kita tidak perlu menulis kode query SQL. Dengan ORM, pengembang dapat memetakan struktur data dalam bahasa Python ke tabel-tabel dalam database, serta memanipulasi data tersebut.
<br />
## Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

========================= 1 =========================<br />
Data delivery, dari pengertian namanya yaitu pengantaran data, hal itu diperlukan dalam pengembangan platform karena memungkinkan pertukaran informasi antara berbagai bagian dari sistem atau aplikasi, serta antara platform dan pengguna. Tanpa sistem pengiriman data yang efektif, sebuah platform tidak dapat berkomunikasi dengan komponen lain seperti database, UI, server, maupun layanan pihak ketiga. Data delivery juga penting untuk mendukung fitur-fitur seperti pengambilan data dari server ke browser, pemrosesan formulir, atau interaksi real-time, serta untuk integrasi sistem yang lebih luas dalam lingkungan aplikasi modern seperti microservices.

========================= 2 =========================<br />
Secara umum, JSON lebih baik dibandingkan XML dalam banyak skenario, terutama untuk aplikasi web modern. Alasannya adalah sebagai berikut:
- JSON lebih ringan: JSON memiliki struktur yang lebih sederhana dan lebih ringkas dibandingkan XML, sehingga data lebih mudah dibaca dan ukuran lebih kecil, yang membuatnya **lebih cepat** untuk dikirimkan melalui jaringan.
- JSON lebih mudah dipahami: JSON berbasis objek dan memiliki format yang sangat cocok dengan sintaks JavaScript, membuatnya lebih mudah dipahami dan digunakan oleh developer yang familiar dengan JavaScript.
- Parsing lebih cepat: JSON dapat di-parse lebih cepat dibandingkan XML dalam kebanyakan bahasa pemrograman, termasuk JavaScript, karena desainnya yang sederhana.
  
XML, meskipun masih digunakan, biasanya lebih cocok untuk skenario di mana data harus sangat terstruktur atau dalam lingkungan enterprise yang memerlukan skema data yang kuat, seperti di industri yang sangat teregulasi. Namun, web modern membutuhkan pertukaran data yang efisien maka JSON menjadi pilihan yang populer. Sesungguhnya, XML lebih *versatile* dari JSON, tetapi penggunaannya dalam pengembangan platform, JSON dinilai sudah cukup.

========================= 3 =========================<br />
Method is_valid() pada form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Ketika method ini dipanggil, Django akan memeriksa apakah semua field dalam form memenuhi aturan validasi yang telah didefinisikan atau telah sesuai dengan constraint yang telah diatur (misalnya, apakah format entrynya benar, apakah semua field yang wajib diisi sudah diisi, dan sebagainya). Jika semua validasi berhasil, method ini mengembalikan nilai True, yang berarti data tersebut siap untuk diproses lebih lanjut (seperti disimpan di database). Jika tidak, method ini mengembalikan False, dan Django akan memberikan pesan error terkait masalah validasi.

Kita memerlukan is_valid() untuk memastikan bahwa data yang kita terima dari pengguna tidak bermasalah atau cacat (kurang lengkap). Hal ini penting untuk mencegah penyimpanan data yang salah di database, serta menghindari potensi error atau bug yang dapat terjadi jika data yang tidak valid diproses lebih lanjut.

========================= 4 =========================<br />
CSRF (Cross-Site Request Forgery) adalah jenis serangan siber di mana penyerang dapat memalsukan **request** dari pengguna yang sah ke server tanpa sepengetahuan atau persetujuan pengguna tersebut.
Django menyediakan csrf_token untuk melindungi aplikasi dari serangan ini. Token CSRF adalah token unik yang dihasilkan untuk setiap form/request dari user dan harus dikirimkan bersama form saat pengguna melakukan submit. Server kemudian memverifikasi bahwa token ini valid dan terkait dengan sesi pengguna yang sah.

Jika kita tidak menambahkan csrf_token, aplikasi kita menjadi rentan terhadap serangan CSRF. Penyerang dapat mengeksploitasi hal ini dengan mengirimkan permintaan palsu (seperti mengubah data akun atau melakukan pembelian) atas nama pengguna yang tidak menyadari bahwa mereka telah melakukan tindakan tersebut.

Contoh serangan CSRF:

Seorang pengguna login ke situs A.
Penyerang mengirimkan sebuah link berbahaya atau menyisipkan skrip di situs lain (situs B).
Ketika pengguna yang login di situs A mengklik link di situs B, situs B secara diam-diam mengirimkan permintaan POST ke situs A dengan menggunakan kredensial pengguna yang sah.
Tanpa csrf_token, server situs A tidak bisa membedakan antara permintaan yang sah dan yang dimanipulasi, sehingga tindakan yang tidak diinginkan bisa dilakukan oleh penyerang.
source: [youtube](https://youtu.be/80S8h5hEwTY?si=oquuF6UVJfi07k8C)

========================= 5 =========================<br />
- Pertama kali yang saya lakukan adalah membuat template html, dimulai dari membuat direktori baru bernama templates di direktori utama, lalu saya membuat file base.html disitu. Dalam base.html berisi kode html serta DTL, penggunaannya yaitu seperti template/kerangka pada umumnya, misalnya pada file html kita yang ada dalam suatu aplikasi dapat meng-extend base.html, dan area yang kita ubah sesuka hati nantinya berada dalam tag ``{% block %}`` dengan ``{% endblock %}``
- Setelah itu, edit ``settings.py`` yang ada di direktori proyek. Edit pada bagian variable ``TEMPLATES``. kemudian pada ``main.html`` yang ada dalam direktori ../main/templates, update isinya dengan tujuan ``main.html`` meng-extend ``base.html`` dengan syntax DTL, dan juga buat kode original htmlnya untuk masuk diantara tag block dan endblock.
- Selanjutnya, saya mengedit models dari app main saya, yaitu menambahkan ID untuk setiap objek pada database. ID ini berasal dari library uuid. Karena models berubah, kita perlu lakukan migrasi model.
- Lalu, saya membuat sebuah file python baru bernama ``forms.py`` yang berisi kode untuk membuat form input data. Form yang dibuat akan berdasarkan models yang ada di ``main/models.py``. Kemudian, kita atur ``views.py`` yang ada di direktori main, untuk mengatur logic httprequst untuk form kita. Apabila form valid dan httprequest berupa POST maka akan redirect ke show_main. Pada fungsi ``show_main`` kita update untuk menerima entry dari form kita agar bisa mengambil seluruh objek entry form yang ada di databsae.
- Selanjutnya, kita perlu mengupdate urls aplikasi kita, dengan menambahkan path untuk fungsi form kita. Lalu, saya membuat bagian front-end untuk page formnya, tentu saja file htmlnya meng-extend base.html serta berisi kode untuk meminta input user, dalam kodenya juga ditambahkan penjelas bahwa form yang dibuat menggunakan metode POST serta ada csrf token yang digunakan sebagai pencegahan serangan CSRF. Lalu dalam ``main.html`` ditambahkan kode untuk menampilkan hasil dari input form user yang disajikan dengan tabel.
- Setelah itu, saya membuat fungsi untuk menampilkan data input form sebagai XML, JSON, serta versi dengan id spesifiknya. Menggunakan library django ``from django.http import HttpResponse`` dan ``from django.core import serializers``. Fungsi-fungsi ini berada di ``views.py`` pada main, semuanya mengambil data entry dari database dan mereturn HttpResponse dengan jenis delivery data yang sesuai (diset dengan serializers).
Untuk XML dengan ID dan JSON dengan ID kita hanya perlu menambahkan filter pada objek entry form yaitu membuat Primary Key nya yaitu id.
- Setelah membuat fungsinya di views.py, kita perlu mengatur urls.py dengan menambahkan path url pattern agar bisa diakses pengguna.
<br />
<h3 align="center">
Foto penggunaan POSTMAN
</h3>

<p align="center"> 
    <img src="photos/xml.png">
    <img src="photos/xmlbyid.png">
    <img src="photos/json.png">
    <img src="photos/jsonbyid.png">
</p>
<br />

## TUGAS 4
<br />
1. apa perbedaan antara HttpResponseRedirect() dan redirect()<br />
2. Jelaskan cara kerja penghubungan model Product dengan User!<br />
3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.<br />
4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?<br />
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br />

========================= 1 =========================<br />
``HttpResponseRedirect``: bertipe class-based, butuh konstruksi url secara manual, kurang flexible karena hanya bisa bekerja pada URL,
biasanya digunakan ketika kita sudah punya URL kustom yang telah terbentuk

``redirect()``: bertipe fungsi, dapat meredirect ke URL/model instance/view name, lebih flexible, biasanya digunakan ketika ingin djangonya sendiri yang menentukan URLnya

========================= 2 =========================<br />
Dengan membuat hubungan (relationship) antara user dengan objek product. Untuk melakukan hal itu, kita perlu mengubah models.py, intinya 
relationship itu berbentuk 1 to n, dimana 1 user bisa punya banyak product, sedangkan product pasti dimiliki suatu user yang membuat product
harus berpartisipasi secara total, maka jika dibayangkan dalam bentuk table relasionalnya, tabel product harus memiliki PK dari user dan itu 
akan mereference ke user yang sesuai PKey nya (menjadi foreign key).
Oleh karena itu, ketika pengisian form product, views.py akan mengambil username yang sedang terlogin sekarang dan di save sebagai bagian
dari data formnya. Setelah itu, pada homepage akan ditampilkan product-product yang telah difilter sesuai dengan id user yang login sekarang.

========================= 3 =========================<br />
Saat pengguna login, Pengguna memasukkan kredensial (username/password) melalui form login.
Django mencocokkan kredensial ini dengan yang ada di database menggunakan mekanisme otentikasi bawaan (fungsi authenticate).
Jika kredensial valid, pengguna dianggap terotentikasi. Django kemudian memulai sesi pengguna (session), menyimpan informasi pengguna terautentikasi ke dalam request.user. Setelah otentikasi, Django mengizinkan akses ke halaman yang diatur menggunakan otorisasi berdasarkan izin pengguna (misalnya, is_staff atau is_superuser), kurang lebih menentukan privilege dari user yang baru login.

Django menggunakan sistem otentikasi bawaan untuk memverifikasi pengguna melalui django.contrib.auth. Otentikasi ini biasanya dilakukan melalui form login di mana pengguna memasukkan username dan password, lalu Django membandingkannya dengan data di database. Kemudian, Django mengatur otorisasi menggunakan permissions dan groups. Dengan fitur ini, Anda bisa menentukan apa yang dapat dilakukan oleh pengguna. Misalnya, admin mungkin memiliki akses penuh ke seluruh situs, sementara pengguna biasa hanya memiliki akses terbatas.

========================= 4 =========================<br />
Setelah pengguna berhasil login, Django menyimpan ID sesi di cookie pengguna (biasanya disebut sessionid). ID sesi ini adalah referensi ke data sesi yang disimpan di sisi server (misalnya di database, file, atau cache) yang berisi informasi pengguna seperti user ID.

Setiap kali pengguna melakukan request baru ke server, browser akan mengirimkan cookie sessionid ini, dan Django akan menggunakan ID tersebut untuk mengambil informasi sesi yang disimpan di server. Django akan menyimpan status login pengguna dalam sesi. Saat ada permintaan HTTP, Django mengecek apakah sesi tersebut masih aktif dan memverifikasi apakah pengguna masih terautentikasi.

Cookies adalah data kecil yang disimpan di browser pengguna dan dapat digunakan oleh server untuk berbagai keperluan selain manajemen sesi. Berikut kegunaan cookies,
- Manajemen Otentikasi
- Menyimpan Preferensi Pengguna
- Pelacakan Aktivitas Pengguna
- Targeting Iklan
- Penyimpanan Sementara

Tidak semua cookies aman, dan harus dikonfigurasi dengan benar menggunakan atribut seperti Secure, HttpOnly, dan SameSite untuk melindungi dari serangan seperti XSS, CSRF, dan session hijacking.

========================= 5 =========================<br />
- Pertama tidak lupa aktifkan python virtual environment, lalu masuk ke file ``views.py`` di direktori main untuk menambahkan UserCreationForm dan messages
- tambahkan fungsi register pada ``views.py``, lalu buat front end nya ``register.html`` untuk page registration nya. Setelah itu buat pathnya di ``urls.py``
- Lalu untuk fungsionalitas loginnya, kembali ke ``views.py`` dan tambahkan import berikut
``from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login``
- lalu langkah yang sama, buat fungsi login_user untuk mengatur logic user yang ingin login, lalu buat html page nya dan buat path nya di urls.py
- Kemudian, langkah yang sama tetapi untuk membuat fungsionalitas logout user.
- Setelah itu kita perlu merestriksi akses ke show_main / main page dengan menggunakan decorator dari import ini
``from django.contrib.auth.decorators import login_required``
Taruh decoratornya pada fungsi show_main di views.py dengan parameter url ke page login
- Selanjutnya, untuk penerapan last login menggunakan cookies, diperlukan import
``import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse``
Lalu edit logic pada fungsi login_user tepatnya pada block if form.is_valid(). Setelah user diloginkan kita buat response untuk redirect ke page show_main, serta atur cookie dengan key="last_login" value=str(datetime.datetime.now()) untuk dapat waktu sekarang ketika login.
- kemudian, pada fungsi show_main kita tambahkan key value untuk last_login pada context, agar dapat kita tampilkan pada htmlnya.
- lalu, pada fungsi logout_user kita perlu menghapus cookies last_login setelah user dilogoutkan
- Kemudian, untuk memetakan user dengan product yang khusus untuk user tersebut, kita perlu ubah ``models.py`` pada models Product, tambahkan user sebagai foreign key untuk model product
- Lalu update, fungsi untuk form menambahkan product untuk menambahkan user yang login sekarang sekalian dengan form ke database
- kemudian, pada fungsi show_main, kita tidak akan mengambil semua objek Product dari database melainkan difilter terlebih dahulu sesuai dengan objek User yang login sekarang. Dan juga ganti name pada context menjadi username dari objek user.
<br />

## TUGAS 5
<br />
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!<br />
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!<br />
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!<br />
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!<br />
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
<br />

========================= 1 =========================<br />
Prioritas pengambilan CSS selector untuk suatu elemen HTML ditentukan berdasarkan spesifisitas. Spesifisitas ini menghitung tingkat "prioritas" dari masing-masing selector yang diterapkan pada elemen tersebut. Dalam penerapan spesifitasnya, ada dua aturan tambahan, yaitu:
- Spesifisitas Kombinasi: Jika ada kombinasi selector (misalnya, selector elemen dengan class), spesifisitasnya dijumlahkan. Sebagai contoh, selector div.highlight lebih spesifik dibanding div atau .highlight saja.
- Urutan Kemunculan: Jika dua selector memiliki spesifisitas yang sama, aturan yang muncul terakhir dalam file CSS akan diterapkan.

Berikut urutan prioritasnya dari yang paling rendah sampai tinggi:
1. Elemen HTML / Type Selector
Selector yang menggunakan nama tag HTML langsung (misalnya, p, h1, div).
Ini memiliki spesifisitas yang paling rendah.
2. Class Selector
Selector yang menggunakan . diikuti dengan nama kelas (misalnya, .class-name).
Spesifisitasnya lebih tinggi dibanding selector tag.
3. Attribute Selector dan Pseudo-Class Selector
Selector yang memilih elemen berdasarkan atribut atau kondisi pseudo-class (misalnya, [type="text"], :hover, :focus, :nth-child()).
Spesifisitasnya selevel dengan class selector.
4. ID Selector
Selector yang menggunakan # diikuti dengan nama ID (misalnya, #id-name).
Ini memiliki spesifisitas yang lebih tinggi dibanding class dan pseudo-class.
5. Inline Style
CSS yang didefinisikan langsung dalam elemen HTML menggunakan atribut style.
Spesifisitasnya lebih tinggi dibanding semua selector lainnya kecuali !important.
6. Important Rule (!important)
Deklarasi CSS yang menggunakan !important akan mengabaikan urutan spesifisitas biasa dan menjadi prioritas tertinggi. Penggunaan !important sebaiknya diminimalkan karena dapat membuat CSS sulit untuk di-maintain.

========================= 2 =========================<br />
Responsive design penting dalam pengembangan web karena memungkinkan tampilan situs menyesuaikan dengan ukuran layar berbagai perangkat, seperti desktop, tablet, dan smartphone. Ini penting untuk memberikan pengalaman pengguna yang baik dan memastikan website mudah diakses di mana pun.

- Pengalaman Pengguna yang Lebih Baik: Website yang responsif otomatis menyesuaikan elemen seperti teks dan gambar agar nyaman dilihat dan digunakan di perangkat apapun.
- Meningkatkan SEO: Google lebih menyukai website yang ramah mobile, sehingga desain responsif bisa meningkatkan peringkat pencarian.
- Efisiensi Biaya: Hanya perlu satu desain yang berfungsi di semua perangkat, menghemat waktu dan biaya pengembangan.
- Penggunaan Mobile yang Tinggi: Pengguna internet semakin banyak yang mengakses dari smartphone, sehingga desain responsif membantu menjangkau lebih banyak pengguna.
Contoh Aplikasi:
Sudah Responsif:
Spotify dan Discord menyesuaikan tampilan agar tetap mudah digunakan baik di desktop maupun mobile.
Belum Responsif:
Beberapa website perusahaan lama dan forum jadul belum mendukung desain yang baik untuk perangkat mobile, sehingga tampilan di layar kecil sulit diakses. seperti [aren.cs.ui.ac.id](http://aren.cs.ui.ac.id/sda/index.php).

========================= 3 =========================<br />
Margin, border, dan padding adalah elemen penting dalam pengaturan ruang pada desain web.
Margin: Ruang di luar elemen yang memisahkannya dari elemen lain. Fungsinya untuk memberi jarak antar elemen.
``margin: 20px;``

Border: Garis pembatas di sekitar elemen yang membungkus isi elemen dan padding.
``border: 2px solid black;``

Padding: Ruang di dalam elemen, antara konten dan border. Ini memberi jarak antara teks atau gambar dan pinggiran elemen.
``padding: 15px;``

Ketiganya membantu mengatur tampilan layout agar lebih rapi dan terstruktur.

========================= 4 =========================<br />
Dua sistem tata letak yang digunakan dalam CSS untuk mengatur elemen di halaman web adalah Flexbox dan Grid Layout.

Flexbox (Flexible Box Layout):
Flexbox dirancang untuk mengatur elemen dalam satu dimensi (horizontal atau vertikal). Elemen di dalam flex container bisa otomatis disesuaikan untuk mengisi ruang yang tersedia, membuatnya ideal untuk tata letak responsif. Digunakan untuk mengatur elemen yang berbaris (seperti tombol navigasi atau kartu produk) atau menyesuaikan ukuran item secara dinamis dalam satu baris atau kolom.

Grid Layout:
Grid layout bekerja di dua dimensi (baris dan kolom), memungkinkan pengaturan elemen di berbagai posisi dalam grid. Ini memberi lebih banyak kontrol untuk membuat tata letak kompleks seperti dashboard atau galeri, bayangkan seperti menaruh elemen pada diagram kartesius. Cocok untuk struktur tata letak yang lebih kompleks, seperti halaman yang membutuhkan area konten berbeda-beda dalam kolom dan baris.

Keduanya memudahkan pengaturan tata letak responsif dan fleksibel. Flexbox lebih baik untuk tata letak sederhana dalam satu dimensi, sementara Grid lebih cocok untuk tata letak dua dimensi yang lebih kompleks.

========================= 5 =========================<br />
- mengatur static files pada ``settings.py`` di direktori proyek. Untuk proyek ini saya menggunakan tailwind. Tambahkan script cdn tailwind pada ``base.html``.
- Lalu, pergi ``views.py`` untuk menambahkan fitur edit_product dan delete_product, dengan mengambil objek productnya sesuai primary key id objek nya. Untuk edit_product ambil formnya dengan isi sesuai dengan si objek yang ingin diedit lalu jika form valid save form baru itu. Untuk delete_product kita tinggal lakukan method delete. Lalu buat path nya di ``urls.py`` dan buat html nya untuk edit_mood.
- Lalu pada main.html tambahkan button yang merujuk ke edit dan delete sebagai table data untuk tiap row.
- Kemudian pada direktori utama pada file templates buat navbar.html dan isinya sesuai kreasi saya dengan bantuan AI. Juga menambahkan fungsionalitas untuk pengguna mobile.
- Navbar ini menunjukkan nama aplikasi, logo, beberapa button, tombol logout. Lalu pada ``settings.py`` direktori proyek tambahkan middleware whitenoise. Dengan menambahkan middleware WhiteNoise pada settings.py, Django dapat mengelola file statis secara otomatis dalam mode produksi (DEBUG=False) tanpa perlu konfigurasi yang kompleks. Hal ini berguna agar file statis tersebut bisa diakses di deployment kamu sebab secara default, apabila DEBUG=False maka Django tidak akan menyediakan akses ke file statis.
-  Lalu buat ``global.css`` yang berisi defined class dengan styling nya yang lalu dihubungkan ke base.html.
-  Setelah itu tinggal styling lanjutan untuk html-html di main/templates seperti pada main.html, login.html, register.html, edit_product, dan create_product_entry. Dalam main, edit, dan create include navbar.html. Lalu untuk main buat card_info.html serta card_product.html untuk menunjukkan objek/produk yang telah kita entry.
