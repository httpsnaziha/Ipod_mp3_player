
<h2 align="center"><u>Ipod-mp3-player</u></h2>

<p align="center">
<br>
    <img src="https://img.shields.io/badge/Author-NAZiha-magenta?style=flat-square">
    <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>
<img width="449" height="212" alt="Capture d’écran 2026-07-23 153506" src="https://github.com/user-attachments/assets/ec6baeb2-6cba-48bc-9e93-f1ce7b6f6548" />

# 🎧 iPod Music Player

A retro-style desktop MP3 player built with **Python**, **Tkinter**, and **Pygame**, inspired by the classic iPod click-wheel interface.

<img width="449" height="212" alt="Capture d’écran" src="https://github.com/user-attachments/assets/1abd32eb-167a-402f-8135-5ad78b146436" />

## Features

- 🎵 **Local MP3 playback** — load an entire folder of `.mp3` files and play them back-to-back
- 🖱️ **Click-wheel style controls** — circular iPod-inspired UI with Play/Pause, Next, Previous, and Menu buttons
- 📃 **Music library screen** — browse and select any loaded track from a scrollable list
- ⏯️ **Play / Pause / Resume** — toggle playback from the center wheel button
- ⏭️ **Next / Previous track** — cycles through the loaded playlist (wraps around at the ends)
- 📂 **Folder import** — pick a folder via a file dialog and all MP3s inside are added to the queue
- ⚙️ **Settings screen** — placeholder screen for future app settings
- 🎨 **Pastel retro theme** — soft pink/gray color scheme with a hand-drawn "Ivy" font style

## How It Works

1. Launch the app — you'll see the classic iPod-style circular control wheel.
2. Click **MENU** to open the main menu (`music`, `files`, `settings`).
3. Select **files** to open a folder picker and import all `.mp3` files from a chosen directory.
4. Select **music** to view your imported tracks; click any track to start playing it.
5. Use the wheel's **center button** to play/pause, and the **◀ / ▶** icons to skip between tracks.

## Requirements

- Python 3.x
- [pygame](https://pypi.org/project/pygame/) — audio playback
- [Pillow](https://pypi.org/project/Pillow/) (`PIL`) — icon image handling

Install dependencies with:

```bash
pip install pygame pillow
```

> Note: `tkinter` usually ships with Python by default. On Linux, you may need to install it separately (e.g. `sudo apt install python3-tk`).

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/httpsnaziha/Ipod_mp3_palyer.git
   cd Ipod_mp3_palyer
   ```
2. Make sure the `icons/` folder (containing `next.png`, `previous.png`, and `pause.png`) is present alongside `ipod_mp3.py`.
3. Run the app:
   ```bash
   python ipod_mp3.py
   ```

## Project Structure

```
Ipod_mp3_palyer/
├── ipod_mp3.py     # Main application (GUI + playback logic)
├── icons/          # Control icons (next, previous, pause)
└── music/          # Sample/bundled music folder
```

## Notes

- The player only scans the top level of the folder you choose for `.mp3` files — subfolders are not scanned recursively.
- The music queue is kept in memory only; nothing is saved between sessions, so you'll need to re-import your folder each time you launch the app.
- The "settings" screen is currently just a placeholder with no functional options yet.






