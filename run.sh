echo 'starting...'
nohup sh loopGetCode.sh >> logs/shloopGetCode.log &
nohup python status.py >> logs/pystatus.log &
echo 'Started'
