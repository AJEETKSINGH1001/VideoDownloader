import os
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter import ttk
from pytube import YouTube


def download_and_play():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if not stream:
            messagebox.showerror("Error", "No MP4 format available for download.")
            return

        video_filename = f"{yt.title}.mp4"
        if os.path.exists(video_filename):
            messagebox.showinfo("Info", "Video already downloaded.")
        else:
            stream.download(filename=video_filename)
            messagebox.showinfo("Success", "Video downloaded successfully!")

        play_downloaded_video(video_filename)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")


def play_downloaded_video(video_filename):
    try:
        if os.path.exists(video_filename):
            os.startfile(video_filename)
        else:
            messagebox.showerror("Error", "Video file not found for playback.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to play video: {e}")


# Create main window
root = Tk()
root.title("YouTube Video Downloader")


# Create URL entry
url_label = Label(root, text="Enter Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create Download button
download_button = Button(root, text="Download & Play", command=download_and_play)
download_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Set style for widgets
style = ttk.Style()
style.configure('TButton', foreground='black', background='#4CAF50', font=('Arial', 12))
style.configure('TEntry', foreground='black', font=('Arial', 12))

# Run the main event loop
root.mainloop()
