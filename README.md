# Spotify Playlist Downloader 🎵

Welcome to the **SpotiPie**! This Python script allows you to download all tracks from any Spotify playlist using the **spotdl** tool. The script fetches track details using the **Spotify API**, and then proceeds to download the songs in parallel, making the process faster and more efficient.


---

## Features 🚀

- **Spotify API Integration**: Fetch playlist track details using Spotify's Web API.
- **Parallel Downloads**: Uses Python's **ThreadPoolExecutor** for downloading multiple tracks simultaneously, speeding up the process.
- **Cross-Platform**: Works on **Windows**, **Linux**, and **macOS**.
- **Spotdl Tool**: Downloads songs in high-quality MP3 format using the **spotdl** command-line tool.
- **User-Friendly**: Interactive prompts to guide you through the process.

---

## Prerequisites 🛠️

Before running the script, you need the following:

1. **Python 3.6+**: Make sure Python is installed on your system.
2. **Install dependencies**: 
    - **spotipy**: For interacting with the Spotify API.
    - **spotdl**: For downloading music from Spotify.
    
    You can install the dependencies by running:

    ```bash
    pip install spotipy spotdl
    ```

3. **Spotify Developer Account**: You'll need to create a **Spotify Developer App** to get your **client ID**, **client secret**, and **redirect URI**. 
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to create an application.
   - Set the **Redirect URI** to `http://localhost:8888/callback`.

---

## Installation and Setup ⚙️

1. **Install Python dependencies**:
    - Open your terminal and run the following command:
      ```bash
      pip install spotipy spotdl
      ```

2. **Obtain Spotify Developer Credentials**:
    - Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
    - Copy the `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and set the `SPOTIPY_REDIRECT_URI` to `http://localhost:8888/callback`.
    - Paste these credentials in the script where indicated.

3. **Clone the repository**:
    - Clone this repository to your local machine:
      ```bash
      git clone https://github.com/your-username/spotify-playlist-downloader.git
      cd spotify-playlist-downloader
      ```

4. **Configure the script**:
    - Open the script (`SpotiPieV2.py`) and replace the placeholders for your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`.

---

## How to Run the Script 💻

### 

1. Open **Terminal**.
2. Navigate to the folder where you saved the script:
   ```bash
   cd path\to\SpotiPie-main
