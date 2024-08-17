from pytube import YouTube

def download_highest_quality_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution video stream available
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Download the video
        print(f"Downloading: {yt.title} in {video_stream.resolution} resolution.")
        video_stream.download(output_path=save_path)
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=your_video_id"  # Replace with your video URL
    save_directory = "/path/to/your/directory"  # Replace with your desired save path
    download_highest_quality_video(video_url, save_directory)
