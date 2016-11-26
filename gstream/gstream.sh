raspivid -fps 25 -h 720 -w 1080  -n -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.43.229 port=5000
#raspivid -fps 25 -h 720 -w 1080  -n -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000
