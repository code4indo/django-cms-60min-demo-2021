Currently this project has 3 live instances:
- 1fortheworld.org chapter's resource - http://chapters.1fortheworld.org/
- it's the official demo for [DjangoCMS project](https://github.com/divio/django-cms/) - https://control.divio.com/demo/get-new/
- Effective Altruism Netherlands - https://effectiefaltruisme.nl/en/


Development Setup
-------------------------------------------------------------------------------

See the general [setup instructions](https://github.com/django-cms/djangocms-template/blob/master/docs/local-setup-instructions.md)

[Project intro & guidelines](https://github.com/django-cms/djangocms-template/blob/master/docs/README.md)

You can download and import the demo data [here](https://drive.google.com/drive/folders/1Q3ZyK4uvCAWR-qWa3Nk1zL3a7RyQgEJM?usp=sharing). In order to import the data:
- extract data.zip into the root directory of the project
- docker-compose up
- import demo-2021-07-09 into the `db` database



Codebase Source
-------------------------------------------------------------------------------

This project is built upon https://gitlab.com/effective-altruism/ea-cms-template/ (with friendly permission from EA).


## Tech Stack

- Debian 10
- Python 3.9
- Django 3.1
- DjangoCMS 3.8
- Node 14
- Webpack 5
- TypeScript 4
- Bootstrap 4

### Mempersiapan Environment
install docker  
install docker-compose

Untuk menginstal Docker dan Docker Compose pada sistem Ubuntu, Anda dapat mengikuti langkah-langkah berikut. Perintah ini diasumsikan dijalankan pada Ubuntu versi 20.04 atau lebih baru, tetapi harus kompatibel dengan versi Ubuntu lainnya.

1. Instalasi Docker:

   a. Update paket dan tambahkan dependensi yang diperlukan:

   ```
   sudo apt-get update
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```

   b. Tambahkan kunci GPG resmi Docker:

   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

   c. Tambahkan repositori Docker:

   ```
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

   d. Update paket dan instal Docker:

   ```
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

   e. Verifikasi apakah Docker berhasil diinstal dan berjalan dengan baik:

   ```
   sudo systemctl status docker
   ```

2. Instalasi Docker Compose:

   a. Unduh rilis terbaru Docker Compose dari repositori GitHub:

   ```
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

   Catatan: Ganti `1.29.2` dengan versi terbaru Docker Compose. Anda bisa melihat versi terbaru di [https://github.com/docker/compose/releases](https://github.com/docker/compose/releases).

   b. Berikan izin eksekusi untuk file `docker-compose`:

   ```
   sudo chmod +x /usr/local/bin/docker-compose
   ```

   c. Verifikasi apakah Docker Compose berhasil diinstal:

   ```
   docker compose --version
   ```

Setelah menjalankan perintah di atas, Anda seharusnya telah berhasil menginstal Docker dan Docker Compose pada sistem Ubuntu Anda.

### Project Setup 
```
docker compose up --build -d 
```
### penjelasan 
Perintah `docker compose up --build -d` adalah perintah yang digunakan untuk membangun, membuat, dan menjalankan container dari layanan yang didefinisikan dalam file `docker-compose.yml`. Mari kita bahas setiap bagian dari perintah ini:

1. `docker compose up`: Perintah dasar ini digunakan untuk membuat dan menjalankan container berdasarkan konfigurasi dalam file `docker-compose.yml`. Jika container sudah ada, perintah ini akan memulai kembali container tersebut dengan konfigurasi terbaru.

2. `--build`: Opsi ini digunakan untuk memaksa pembuatan (build) ulang image untuk layanan yang didefinisikan dalam file `docker-compose.yml`. Ini berguna ketika Anda ingin memastikan bahwa image terbaru yang digunakan oleh container mencerminkan perubahan dalam Dockerfile atau konteks build sejak build sebelumnya.

3. `-d`: Opsi ini merupakan singkatan dari `--detach`. Dengan menggunakan opsi ini, container akan dijalankan dalam mode "detached", yang berarti container akan berjalan di latar belakang dan tidak akan mengikat terminal atau stdout Anda. Ini berguna jika Anda ingin terus menggunakan terminal Anda untuk perintah lain atau jika Anda ingin menjalankan container dalam mode "production".

Jadi, perintah `docker compose up --build -d` akan membangun ulang image (jika perlu), membuat dan menjalankan container dari layanan yang didefinisikan dalam `docker-compose.yml` dalam mode latar belakang.

### firstly remove /static_collected from .docker ignore
4. docker compose di jalankan berdasarkan pada file docker-compose.yml, berikut apa yang dilakukannya:
Berdasarkan file `docker-compose.yml` yang diberikan, ada beberapa kesimpulan tentang apa yang telah dibuat dan dilakukan dalam konfigurasi ini:

1. Terdapat tiga layanan yang didefinisikan dalam konfigurasi ini: `web`, `frontend`, dan `db`.
2. Layanan `web` menggunakan Dockerfile dengan nama `Dockerfile` dan menjalankan server web menggunakan perintah `python manage.py runserver 0.0.0.0:80`.
3. Layanan `frontend` menggunakan Dockerfile dengan nama `frontend.Dockerfile` dan menjalankan server pengembangan webpack menggunakan perintah `yarn webpack-dev-server-in-docker`.
4. Layanan `db` menggunakan image `postgres:9.6-alpine` sebagai basis dan mengatur konfigurasi PostgreSQL menggunakan variabel lingkungan.
5. Konfigurasi ini mengatur beberapa volume untuk menyimpan data aplikasi dan membaginya di antara layanan yang berbeda.
6. Konfigurasi ini juga mengatur pemetaan port antara container dan host untuk masing-masing layanan agar dapat diakses dari luar container.
7. Layanan `web` terhubung ke layanan `db` dengan menggunakan alias `postgres`.

Dalam konfigurasi ini, aplikasi multi-container terdiri dari komponen web, frontend, dan database yang saling terhubung dan bekerja sama. Anda dapat menggunakan perintah `docker-compose up` untuk membuat dan menjalankan semua layanan ini secara bersamaan dan mulai mengembangkan aplikasi Anda.