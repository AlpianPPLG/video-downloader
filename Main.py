import tkinter
import customtkinter
from pytube import YouTube

# Function to start the video download process
def start_download():
    try:
        # Create a YouTube object with the URL entered by the user
        url = YouTube(url_var.get())
        # Get the first video stream and run the on_progress function during the download process
        video = url.streams.first(on_progress_callback=on_progress)
        # Configure the title label with the video title and white text color
        title.configure(text=video.title, text_color="white")
        # Clear the progress label
        progress.configure(text="")
        # Start the video download process
        video.download()
        # Show a success message after the download process is complete
        tkinter.messagebox.showinfo("Success", "Video downloaded successfully")
    except:
        # Show an error message if the video link is invalid
        tkinter.messagebox.showerror("Failed", "Invalid video link")

# Function to update the progress bar during the download process
def on_progress(stream, chunk, bytes_remaining):
    # Calculate the total file size of the video
    total_size = stream.filesize
    # Calculate the size of the data that has been downloaded
    bytes_downloaded = total_size - bytes_remaining
    # Calculate the percentage of the download process
    percentage_of_completion = bytes_downloaded / total_size * 100
    # Convert the percentage to a string and update the percentage label
    percentage_str = str(int(percentage_of_completion))
    percentage_label.configure(text=percentage_str + '%')
    percentage_label.update()

    # Update the progress bar
    progress_bar.set(float(percentage_of_completion) / 100)

# Set the appearance mode according to the operating system
customtkinter.set_appearance_mode("System")
# Set the color theme of the application to blue
customtkinter.set_default_color_theme("blue")

# Create the application window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# Add the title label
title = customtkinter.CTkLabel(app, text="Enter Video Link")
title.pack(padx=10, pady=10)

# Add the input field for entering the video URL
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Add the Download button and connect it to the start_download function
download_button = customtkinter.CTkButton(app, text="Download", command=start_download)
download_button.pack(padx=10, pady=10)

# Add the label to display the download progress
progress = customtkinter.CTkLabel(app, text="")
progress.pack()

# Add the label to display the download progress percentage
percentage_label = customtkinter.CTkLabel(app, text="0%")
percentage_label.pack()

# Add the progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Run the application
app.mainloop()