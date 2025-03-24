##Commande importante :
arp -a (scan les ip)
ssh RASPBERRY_USER1@RASPBERRY_IP (se connecter au rasp)


##Commande GitHub Raspberry:
sudo apt update && sudo apt install git -y (installer git)




##Possible erreur : 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:QUroD2HsS/G8WDitgKDwTbYssLvNl18D+1VElmVUP8k.
Please contact your system administrator.
Add correct host key in /Users/florianrichet/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /Users/florianrichet/.ssh/known_hosts:2
Host key for 192.168.1.41 has changed and you have requested strict checking.
Host key verification failed.

commande resolution : ssh-keygen -R {RASPBERRY_IP}
