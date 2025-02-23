![image](https://github.com/user-attachments/assets/10e43ad7-edad-45e7-9161-1976cb30ff24)
# Spotify Playlist Downloader 🎵

Welcome to **SpotiPie**! This Python script allows you to download all tracks from any Spotify playlist using the **spotdl** tool. The script fetches track details using the **Spotify API**, then downloads the songs in parallel, making the process faster and more efficient.

---

## Features 🚀

- **Spotify API Integration**: Fetches playlist track details using Spotify's Web API.
- **Parallel Downloads**: Utilizes Python's **ThreadPoolExecutor** to download multiple tracks simultaneously.
- **Cross-Platform**: Compatible with **Windows**, **Linux**, and **macOS**.
- **Spotdl Tool**: Downloads tracks in high-quality MP3 format using the **spotdl** command-line tool.
- **User-Friendly**: Interactive prompts guide you throughout the process.

---

## Cons ⚠️

While SpotiPie is a powerful tool, please consider the following drawbacks:

- **Spotdl Dependency**: The script relies on **spotdl**, which depends on third-party services. Occasionally, **spotdl** might encounter errors or not support certain track types or regions.
- **Rate Limiting**: Spotify's API can impose rate limits. Downloading too many tracks in a short period may result in temporary blocks or errors.
- **No Built-In Error Recovery**: Failed downloads are not automatically retried; you may need to re-run the script or download problematic tracks manually.
- **Not Ideal for Large Playlists**: Large playlists may take considerable time to process, even with parallel downloads.
- **Manual Spotify Authentication**: First-time users must manually authenticate the application, which might be confusing for those new to the Spotify API.
- **Legal Concerns**: Downloading tracks may violate Spotify's terms of service and copyright laws. Use responsibly.
- **Only Your Own Playlists**: The script can download only playlists that you own or have created, not public playlists that you do not own, due to Spotify API limitations.

---
⚠️ Disclaimer
By using SpotiPie, you agree to the following terms and conditions:

Legal Responsibility:
SpotiPie is intended for personal use only. Downloading tracks from Spotify may violate Spotify's terms of service and copyright laws. You are solely responsible for ensuring that your use of this script complies with all applicable laws and regulations in your region.

Third-Party Dependencies:
SpotiPie relies on third-party services, such as spotdl and the Spotify API. These services are subject to change, and SpotiPie may not always function as expected due to external factors, such as API changes or outages. We are not responsible for any issues or disruptions caused by these dependencies.

Privacy and Authentication:
SpotiPie requires access to your Spotify account for authentication purposes. By using this script, you grant the necessary permissions for authentication, and you acknowledge the risks involved in sharing your Spotify credentials.

Use at Your Own Risk:
While we strive to ensure that SpotiPie functions correctly, the software is provided "as-is", without any warranties or guarantees. We are not responsible for any data loss, system malfunctions, or damages resulting from the use of this script.

No Commercial Use:
This script is not intended for commercial use or for downloading content for redistribution or resale. It is intended solely for personal enjoyment of your own playlists.

Responsibility:
By using SpotiPie, you agree to take full responsibility for your actions, including any violations of Spotify's terms of service and copyright laws. The authors are not liable for any consequences arising from the use of this script.

---

## Prerequisites 🛠️

Before running the script, ensure you have the following:

1. **Python 3.6+** installed on your system.
2. **Spotify Developer Account**:
   - Create a [Spotify Developer](https://developer.spotify.com/dashboard/applications) App and create a new application. App to obtain your **client ID**, **client secret**, and **redirect URI**.
   - Set the **Redirect URI** to `http://localhost:8888/callback`.
3. **Required Python Libraries**:
   - All required dependencies are listed in the **requirements.txt** file.

---

## Installation and Setup ⚙️

1. **Install Dependencies**:  
   In your terminal, navigate to the project directory and run:
   ```bash
   git clone https://github.com/sssaaapuyoy/SpotiPie.git
   cd SpotiPie-main
   pip install -r requirements.txt
   python3 SpotiPieV2.py
