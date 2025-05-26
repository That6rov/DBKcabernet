from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>🎉 Welcome to DBKcabernet IPTV</h2><p><a href="/playlist.m3u">Download Playlist</a></p>'

@app.route('/playlist.m3u')
def serve_playlist():
    return send_file('playlist.m3u', mimetype='audio/x-mpegurl')
