
@echo off
echo Installing PortAudio...
winget install -e --id PortAudio.PortAudio

echo Installing MPV...
winget install -e --id VideoLAN.VLC  || choco install mpv

echo Installing Python dependencies...
pip install -r requirements.txt

echo Installation Complete!
pause
