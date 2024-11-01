# 1_Tugas-Socket-Programming
Tugas UDP Socket Programming by kelompok 1 GAS


Samuel Chris Michael Bagasta Simanjuntak (18223011)


Daffa Athalla Rajasa (18223053)


Ghazy Achmed Movlech Urbayani (18223093)

# UDP Chatroom

UDP Chatroom adalah aplikasi chat sederhana berbasis jaringan UDP. Proyek ini terdiri dari dua komponen utama: server dan klien. Server berfungsi untuk menerima dan menyiarkan pesan dari klien, sementara klien memungkinkan pengguna untuk mengirim dan menerima pesan.

## Fitur

- **Login**: Pengguna dapat login dengan username dan password.
- **Pesan Siaran**: Pesan yang dikirim oleh satu klien akan disiarkan ke semua klien lain yang terhubung.
- **Antarmuka Pengguna Grafis**: Klien memiliki antarmuka pengguna grafis sederhana berbasis Tkinter.

## Pustaka yang Digunakan

1. **socket**: 
   - Digunakan untuk membuat koneksi jaringan menggunakan protokol UDP. Modul ini menyediakan antarmuka untuk komunikasi jaringan tingkat rendah.

2. **argparse**: 
   - Digunakan untuk mem-parsing argumen baris perintah. Membantu dalam mengambil input dari pengguna saat menjalankan skrip dari terminal.

3. **threading**: 
   - Memungkinkan aplikasi untuk menjalankan beberapa operasi secara bersamaan dalam thread terpisah. Digunakan untuk mengelola pengiriman dan penerimaan pesan secara bersamaan.

4. **sys**: 
   - Digunakan untuk berinteraksi dengan interpreter Python. Modul ini digunakan untuk keluar dari program dan menangani input/keluaran standar.

5. **tkinter**: 
   - Library standar Python untuk membuat antarmuka pengguna grafis (GUI). Digunakan untuk membangun jendela login dan jendela chat klien.

6. **tkinter.messagebox**: 
   - Komponen dari Tkinter yang digunakan untuk menampilkan kotak pesan seperti peringatan atau informasi kepada pengguna.

## Persyaratan

- Python 3.x
- Tkinter (biasanya sudah terpasang dengan Python)
- Koneksi jaringan yang stabil

## Penggunaan

1. **Login**: Masukkan username dan password saat diminta. Password default adalah `GAS1`.
2. **Mengirim Pesan**: Ketik pesan di kotak input dan tekan Enter atau klik tombol "Send".
3. **Keluar**: Ketik "QUIT" dan tekan Enter untuk keluar dari chatroom.

# Prosedur untuk menjalankan program GAS Chatroom
  Sebelum menjalankan aplikasi, pastikan pengaturan firewall di komputer atau laptop sudah mengizinkan koneksi UDP pada port yang akan dipakai. Untuk GAS Chatroom, port yang harus ditambahkan dalam aturan firewall adalah 8080 serta 5000-5010. Selain itu, pastikan jaringan internet stabil agar komunikasi UDP antara server dan klien dapat berjalan dengan baik.
Langkah-langkah pengujian program adalah sebagai berikut:
1. Menjalankan Server

   
   a. Pastikan server.py dan client.py berada dalam satu folder.


   b. Pastikan Laptop client dan server terhubung pada jaringan yang sama.


   c. Membuka terminal pada folder yang berisi server.py dan client,py di laptop atau komputer
      yang bertindak sebagai server


   d. Command untuk run server:


      python server.py < IP SERVER> -p [PORT]


   e. Tunggu respons dari terminal

   
2. Menjalankan client


   a. Pastikan server.py dan client.py berada dalam satu folder

   
   b. Pastikan laptop client dan server terhubung pada jaringan yang sama

   
   c. Membuka terminal pada folder yang berisi server.py dan client.py di laptop atau komputer

   
   d. Command untuk menghubungkan client ke server : python client.py <IP SERVER> <PORT SERVER>       <PORT CLIENT>

   
   e. Client akan diminta untuk memasukkan username dan password pada GUI yang muncul

   
   f. Client akan disiapkan untuk dapat mengirim serta menerima pesan dari server

   
   g. Lakukan langkah yang sama apabila ingin melakukan pengujian pada 2 client namun pastikan        client kedua memiliki port yang berbeda

   
3. Pengujian Chatroom

   
   a. Setelah client pertama berhasil terhubung, ketika client kedua baru terhubung maka pada         aplikasi Chatroom client pertama akan ada notifikasi bahwa client 2 sudah hadir

   
   b. Client pertama dapat mengirim pesan kepada server untuk kemudian diteruskan ke client           lain yang terhubung

   
   c. Untuk melihat proses menerima dan mengirim pesan antar client maka pengguna dapat membuka       terminal yang sudah dijalankan untuk server

   
   d. Apabila salah satu ataupun kedua client sudah selesai mengirim pesan, maka client bisa          memberi command “QUIT’ untuk keluar dari aplikasi Chatroom.


## Kontribusi

Kontribusi sangat diterima! Jika Anda memiliki saran atau perbaikan, silakan buat pull request atau buka isu.
