1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

========================= 1 =========================
- langkah paling pertama yang saya lakukan adalah menentukan nama proyek django yang akan saya lakukan, setelah itu saya buat directory nya di local file
- pada directory tersebut saya buat python virtual environment dengan command berikut ``python -m venv env1``
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

========================= 2 =========================
\\\\

========================= 3 =========================<br />
Git membantu dalam pengembangan perangkat lunak karena punya kemampuan untuk mengelola perubahan kode, membuat kolaborasi tim menjadi mudah, menghindari konflik kode, dan memastikan kode proyek selalu dapat dipulihkan. Dalam proyek besar yang dikerjakan banyak sekali programmer, git dibutuhkan agar programmernya bisa bekerja dengan lebih efisien dan teroganisir.
Berikut fungsi utama git yang membantu dalam pengembangan perangkat lunak:
- pengelolaan proyek dengan remote repository
- kemudahan kolaborasi dalam tim
- versi kontrol
- backup dan recovery data/file
- audit dan transparansi (terlihat siapa saja yang terlibat dalam pengembangan dan penulisan kodenya)
- menerapkan perubahan dengan aman (lewat pull request dan merge request)

========================= 4 =========================
- django menggunakan bahasa python sebagai dasarnya, yang mana dikenal sebagai bahasa pemrograman yang *newbie friendly*
- django sudah menyiapkan segala macam komponen utama yang diperlukan untuk mengembangkan aplikasi web dari awal hingga akhir
- sesuai poin sebelumnya, ini mempercepat pengembangan, yang mana kita bisa dengan cepat melihat dampak/hasil dari kode kita pada aplikasi webnya
- struktur MVT django memperkenalkan konsep yang (menurut saya) mudah diterima dalam hal pemisahan komponen logis-logisnya
- django ialah framework web yang terkenal, banyak yang memakai. sumber->[sumber](https://blog.jetbrains.com/pycharm/2024/06/the-state-of-django/#:~:text=Developing%20APIs%3A%20Most%20developers%20use,work%20among%20fully%20employed%20devs.)
- dengan banyak yang memakai, komunitas django menjadi besar dan sudah banyak programmer lain yang mungkin mengalami masalah serupa juga sudah ketemu solusinya

========================= 5 =========================
Model pada Django disebut sebagai ORM karena data kita dalam database ditunjukkan lewat classes dan field yang memungkinkan kita tidak perlu menulis kode query SQL. Dengan ORM, pengembang dapat memetakan struktur data dalam bahasa Python ke tabel-tabel dalam database, serta memanipulasi data tersebut.
