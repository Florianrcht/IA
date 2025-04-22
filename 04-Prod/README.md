##Commande importante :
arp -a (scan les ip)
ssh RASPBERRY_USER1@RASPBERRY_IP (se connecter au rasp)
source ../venv/bin/activate (aller dans lenvironnement virtuel)
pip3 install opencv-python
pip3 install Flask
pip3 install requests SQLAlchemy
deactivate (pour sortir)



##Commande GitHub Raspberry:
sudo apt update && sudo apt install git -y (installer git)
git clone https://github.com/Florianrcht/IA.git (clone le repo)

##Possible erreur : 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is.....

commande resolution : ssh-keygen -R {RASPBERRY_IP}

