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

## Cons ⚠️

While the Spotify Playlist Downloader is a powerful tool, there are some drawbacks you should consider:

- **Spotdl Dependency**: The script relies on **spotdl**, which in turn depends on third-party services. Occasionally, **spotdl** might encounter errors or may not support all track types or regions, leading to incomplete downloads.
  
- **Rate Limiting**: The script interacts with Spotify's API, which can impose rate limits. If you download too many tracks in a short time, you may be temporarily blocked from making requests, or receive an error.

- **No Built-In Error Recovery**: If a track fails to download, the script does not attempt to retry or recover the failed download. You may need to re-run the script or download problematic tracks manually.

- **Not for Large Playlists**: For playlists with a large number of tracks, the process may take a significant amount of time, even with parallel downloads. Network speeds and the spotdl tool’s limitations might cause slowdowns.

- **Manual Spotify Authentication**: For first-time use, users need to authenticate the application manually, which could be confusing for those not familiar with the Spotify API.

- **Legal Concerns**: Downloading tracks from Spotify may violate their terms of service and copyright laws. Use this tool responsibly and only for tracks that you have permission to download.

- **Only Your Own Playlists**: The script is designed to download only playlists that you own or have created. It will not work for playlists that are public but not owned by you. This is due to the limitations of Spotify's API regarding access to non-personal playlists.


---
## Prerequisites 🛠️

Before running the script, you need the following:

1. **Python 3.6+**: Make sure Python is installed on your system.
2. **Install dependencies**: 
    - **spotipy**: For interacting with the Spotify API.
    - **spotdl**: For downloading music from Spotify.
    
    You can install the dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Spotify Developer Account**: You'll need to create a **Spotify Developer App** to get your **client ID**, **client secret**, and **redirect URI**. 
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to create an application.
   - Set the **Redirect URI** to `http://localhost:8888/callback`.

---

## Installation and Setup ⚙️


1. **Obtain Spotify Developer Credentials**:
    - Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
    - Copy the `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and set the `SPOTIPY_REDIRECT_URI` to `http://localhost:8888/callback`.
    - Paste these credentials in the script where indicated.

2. **Clone the repository**:
    - Clone this repository to your local machine:
      ```bash
      git clone https://github.com/sssaaapuyoy/SpotiPie.git
      cd SpotiPie-main
      ```

3. **Configure the script**:
    - Open the script (`SpotiPieV2.py`) and replace the placeholders for your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`.

---

## How to Run the Script 💻

### 

1. Open **Terminal**.
2. Navigate to the folder where you saved the script:
   ```bash
   cd path\to\SpotiPie-main
   python3 SpotiPieV2
