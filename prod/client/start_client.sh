#!/bin/bash
echo ">>> Lancement du Client"
python3 servo_order_sender.py &
python3 streaming_receiver.py
