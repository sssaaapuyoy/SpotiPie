import subprocess
import os
import platform

import spotipy
from spotipy.oauth2 import SpotifyOAuth

version = '1.0.0'

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'Sikee! Get Your own Credentials.'
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-private playlist-read-collaborative'# Scope needed to access a user's playlists and read their contents

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

BRIGHT_YELLOW = "\033[93m"
RESET = "\033[0m"

Banner = f"""
{BRIGHT_YELLOW}
    _____         _   _    _____ _     
    |   __|___ ___| |_|_|  |  _  |_|___ 
    |__   | . | . |  _| |  |   __| | -_|
    |_____|  _|___|_| |_|  |__|  |_|___|
        |_|                           

                                  {version}
{RESET}
"""
def Show_Banner():
    print(Banner)

def clear_screen():
    """Clear the terminal screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_playlist_info(playlist_id):
    """Get playlist name from Spotify."""
    try:
        playlist = sp.playlist(playlist_id)
        return playlist['name']
    except spotipy.SpotifyException as e:
        print(f"  Error retrieving playlist: {e}")
        return None

def get_playlist_tracks(playlist_id):
    """Get all tracks from the playlist."""
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']
        total_tracks = results['total']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks, total_tracks
    except spotipy.SpotifyException as e:
        print(f"  Error retrieving tracks: {e}")
        return [], 0

def download_tracks(playlist_name, track_urls):
    """Download tracks using spotdl."""
    print("  Downloading songs...\n")
    downloaded_count = 0
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
    os.chdir(playlist_name)
    
    for url in track_urls:
        try:
            result = subprocess.run(['spotdl', url], check=True, text=True)
            if result.returncode == 0:
                downloaded_count += 1
            else:
                print(f"  Error downloading {url}")
        except subprocess.CalledProcessError as e:
            print(f"  Error downloading {url}: {e}")
    
    os.chdir("..")  # Change back to the original directory
    print(f"\n  Downloaded {downloaded_count} songs from the playlist '{playlist_name}'.")

def ask_to_download(playlist_name, total_tracks, track_urls):
    """Ask the user if they want to download the songs."""
    user_input = input(f"  Do you want to download these {total_tracks} songs from '{playlist_name}'? [Y/n]: ")
    if user_input.lower() in ['y', 'Y', 'yes', 'Yes', 'Ye', 'ye']:
        download_tracks(playlist_name, track_urls)
    else:
        print("  Download cancelled.")

def main():
    """Main function to execute the script."""
    clear_screen()
    Show_Banner()
    
    playlist_url = input('  Playlist URL: ')
    playlist_id = playlist_url.split('/')[-1].split('?')[0]  # Extract the playlist ID from the URL
    
    playlist_name = get_playlist_info(playlist_id)
    if playlist_name:
        tracks, total_tracks = get_playlist_tracks(playlist_id)
        track_urls = [item['track']['external_urls']['spotify'] for item in tracks]
        ask_to_download(playlist_name, total_tracks, track_urls)
    else:
        print("\n  Failed to retrieve playlist information. \n  checking the playlist url might help.")


if __name__ == '__main__':
    main()