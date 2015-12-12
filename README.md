# wiPiBot - In the age of the Internet of Things, this is what you deserve:
  A cool remotely controlled bot like the ones in movies, which can be controlled from anywhere in the world with a browser, with on board camera and full range motions. <br>
 The objective of this project is to create a mobile robot platform powered by two servo motors. There is an onboard camera on the wiPiBot to give its pilot a view of the wiPiBot's sorroundings. The project utilizes a Raspberry Pi B2 model to command all the actions of the robot. Additionally, the Raspberry Pi hosts a server using the Django framework written in Python. The wiPiBot broadcasts the video and various data of its sorroundings to user, and the user controls the wiPiBot's motion through the dashboard that is hosted on the wiPiBot's server.
# To Run Server:
1. Install Django on Raspberry Pi from https://github.com/rmasters/DjangoPi
2. Download the whole project.
3. $ cd ... /wiPiBotServer
4. $ sudo python manage.py runserver 0.0.0.0:8000
5. Use your browser to navigate to your wiPiBot's IP and here comes the fun!

# Launch Camera:
Once having the server running:

1. Download VLC Media Player
2. User your browser to navigate to your wiPiBots IP and go to dashboard.
3. Click on the record video button.
4. Open VLC player, Click Playlist >> Open Media >> Network. In URL field enter tcp/h264://my_pi_address:8001/. Click open to launch the video.

Based on this documentation: http://picamera.readthedocs.org/en/release-1.10/recipes1.html#recording-to-a-network-stream
