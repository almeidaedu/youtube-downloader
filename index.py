import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if not stream:
            messagebox.showerror("Error", "Stream not available.")
            return
        stream.download()
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("YouTube 720p Downloader")

tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_btn = tk.Button(root, text="Download 720p MP4", command=download_video)
download_btn.pack(pady=10)

root.mainloop()