1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?


- langkah paling pertama yang saya lakukan adalah menentukan nama proyek django yang akan saya lakukan, setelah itu saya buat directory nya di local file
- pada directory tersebut saya buat python virtual environment dengan command berikut ``python -m venv env1``
- dalam implementasi checklist ini saya mostly lakukan dengan terminal (Powershell) dan edit file lewat VScode
- Setiap ingin mengerjakan projek django, saya tidak lupa mengaktifkan environment tadi dalam terminal saya
- Selanjutnya saya siapkan dependencies yang diperlukan dalam pembuatan proyek django, seperti menginstall library/package yang ada di file requirements.txt yang saya buat lewat command ``pip install -r requirements.txt``
- lalu saya buat proyek djangonya dengan command ini ``django-admin startproject capybaras_corner .``
- kemudian, dalam settings.py yang ada pada file proyek, saya tambahkan beberapa host seperti localhost yang bertujuan untuk mengecek proyek saya tanpa harus langsung mendeploy ke PWS
- untuk menjalankan proyek saya pada local dapat dilakukan dengan command ini ``python manage.py runserver``
- pada tahap ini dasar proyek djangonya sudah terbentuk, kemudian saya buat repository githubnya. pada direktori utama saya lakukan git init, bertujuan untuk meng-enable fungsionalitas git pada direktori tersebut
- lalu tinggal kita hubungkan repository pada github ke direktori lokal, untuk branch utamanya saya langsung namai master
- sebelum itu saya telah buat file .gitignore, baru saya lakukan git add, git commit, git push pertama saya dalam projek django ini
- 
