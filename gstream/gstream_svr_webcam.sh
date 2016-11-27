gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, framerate=15/1, width=640, height=480 ! omxh264enc ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000
#gst-launch-1.0 -vv -e v4l2src device=/dev/video0  ! videoscale ! "video/x-raw,width=400,height=200,framerate=10/1" ! x264enc pass=qual quantizer=20  tune=zerolatency  ! h264parse ! rtph264pay config-interval=5 pt=96  ! udpsink host=192.168.0.48 port=5000
#gst-launch -v udpsrc port=1234 ! fakesink dump=1
#gst-launch -v audiotestsrc ! udpsink host=127.0.0.1 port=1234
#gst-launch -v v4l2src device=/dev/video0 ! queue ! videoscale method=1 ! "video/x-raw-yuv,width=320,height=240" ! queue ! videorate ! "video/x-raw-yuv,framerate=(fraction)15/1" ! queue ! udpsink host=127.0.0.1 port=5000
#gst-launch -v v4l2src device=/dev/video0 ! queue ! videoscale method=1 ! "video/x-raw-yuv,width=320,height=240" ! queue ! videorate ! "video/x-raw-yuv,framerate=(fraction)30/1" ! queue ! udpsink host=192.168.0.48 port=5000
#gst-launch v4l2src device=/dev/video0 ! 'video/x-raw-yuv,width=640,height=480' !  x264enc pass=qual quantizer=20 tune=zerolatency ! rtph264pay ! udpsink host=192.168.0.48 port=5000
#gst-launch -v v4l2src device=/dev/video0 ! image/jpeg ! jpegdec ! ffmpegcolorspace ! ximagesink

