import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

PAGE="""\
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"> </script>
<script type=text/javascript> $(function() { $("#Vorwaerts").click(function (event) { $.getJSON('/Vorwaerts', { }, function(data) { }); return false; }); }); </script>
<script type=text/javascript> $(function() { $("#Links").click(function (event) { $.getJSON('/Links', { }, function(data) { }); return false; }); }); </script>
<script type=text/javascript> $(function() { $("#Rechts").click(function (event) { $.getJSON('/Rechts', { }, function(data) { }); return false; }); }); </script>
<script type=text/javascript> $(function() { $("#Rueckwaerts").click(function (event) { $.getJSON('/Rueckwaerts', { }, function(data) { }); return false; }); }); </script>
<script type=text/javascript> $(function() { $("#Stop").click(function (event) { $.getJSON('/Stop', { }, function(data) { }); return false; }); }); </script>
</head>
<body>
<p>&nbsp;</p>
<center>
<h1>Alphabot 2 - Task 5</h1>
</center><center><img src="stream.mjpg" width="640" height="480" /></center><center>
<table>
<tbody>
<tr>
<td>&nbsp;</td>
<td><button id="Vorwaerts" type="button">Vorw&auml;rts</button></td>
<td>&nbsp;</td>
</tr>
<tr>
<td><button id="Links" type="button">Links</button></td>
<td><button id="Stop" type="button">Stop</button></td>
<td><button id="Rechts" type="button">Rechts</button></td>
</tr>
<tr>
<td>&nbsp;</td>
<td><button id="Rueckwaerts" type="button">R&uuml;ckw&auml;rts</button></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
</center>
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/Vorwaerts':
            logging.warning('Vorwaerts!!!')
        elif self.path == '/Links':
            logging.warning('Links!!!')
        elif self.path == '/Rechts':
            logging.warning('Rechts!!!')
        elif self.path == '/Rueckwaerts':
            logging.warning('Rueckwaerts!!!')
        elif self.path == '/Stop':
            logging.warning('Stoooop!!!')

        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 180
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
