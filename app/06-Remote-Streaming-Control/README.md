source .venv/bin/activate
cd 06-Remote-Streaming-Control
pip3 install opencv-python
pip3 install Flask
pip3 install requests SQLAlchemy
deactivate 

640x480
sudo lsof -i :9999