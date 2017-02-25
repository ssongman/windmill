



gst-launch-1.0 -v tcpclientsrc host=192.168.0.50    port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
#gst-launch-1.0 -v tcpclientsrc host=192.168.43.229    port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
#gst-launch-1.0 -v tcpclientsrc host=192.168.0.48    port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
#gst-launch-1.0 -v tcpclientsrc host=175.197.168.198 port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
#gst-launch-1.0 -v tcpclientsrc host=192.168.43.253   port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false




