import tkinter
import customtkinter
from pytube import YouTube

# Fungsi untuk memulai proses download video
def startDownload():
    try:
        # Membuat objek YouTube dengan URL yang dimasukkan pengguna
        url = YouTube(url_var.get())
        # Mengambil stream video pertama dan menjalankan fungsi on_progress saat proses download berlangsung
        video = url.streams.first(on_progress_callback=on_progress)
        # Mengonfigurasi label title dengan judul video dan warna teks putih
        title.configure(text=video.title, text_color="white")
        # Mengosongkan label progress
        progress.configure(text="")
        # Memulai proses download video
        video.download()
        # Menampilkan pesan sukses setelah proses download selesai
        tkinter.messagebox.showinfo("Berhasil", "Video berhasil di download")
    except:
        # Menampilkan pesan error jika link video tidak valid
        tkinter.messagebox.showerror("Gagal", "Link video tidak valid")
        
# Fungsi untuk memperbarui progress bar saat proses download berlangsung
def on_progress(stream, chunk, bytes_remaining):
    # Menghitung ukuran total file video
    total_size = stream.filesize
    # Menghitung ukuran data yang sudah diunduh
    bytes_downloaded = total_size - bytes_remaining
    # Menghitung persentase proses download
    Percentage_of_completion = bytes_downloaded / total_size * 100
    # Mengonversi persentase ke string dan memperbarui label Percentage
    per = str(int(Percentage_of_completion))
    Percentage.configure(text=per + '%')
    Percentage.update()
    
    # Memperbarui progress bar
    progressBar.set(float(Percentage_of_completion) / 100)

# Mengatur tampilan aplikasi sesuai dengan sistem operasi
customtkinter.set_appearance_mode("System")
# Mengatur tema warna aplikasi menjadi biru
customtkinter.set_default_color_theme("blue")

# Membuat jendela aplikasi
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Menambahkan label judul
title = customtkinter.CTkLabel(app, text="Masukkan Link Video")
title.pack(padx=10, pady=10)

# Menambahkan input field untuk memasukkan URL video
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Menambahkan tombol Download dan menghubungkannya dengan fungsi startDownload
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Menambahkan label untuk menampilkan progress download
progress = customtkinter.CTkLabel(app, text="")
progress.pack()

# Menambahkan label untuk menampilkan persentase progress download
Percentage = customtkinter.CTkLabel(app, text="0%")
Percentage.pack()

# Menambahkan progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Menjalankan aplikasi
app.mainloop()