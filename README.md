# 1_Tugas-Socket-Programming
Tugas UDP Socket Programming by kelompok 1 GAS


Samuel Chris Michael Bagasta Simanjuntak (18223011)


Daffa Athalla Rajasa (18223053)


Ghazy Achmed Movlech Urbayani (18223093)

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
