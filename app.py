from flask import Flask, send_from_directory, Response, request

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return """
    <h2>Welcome to the CTF Challenge</h2>
    <p>This service contains hidden flags. Try using tools like <b>nmap</b> and <b>curl</b> to find them.</p>
    """

# Nmap-style Flag (Simulated via URL endpoint)
@app.route("/nmap-flag")
def nmap_flag():
    banner = "Service Running: echo-server v1.2.3\nFlag: CTF{open_port_simulated}"
    return Response(banner, mimetype='text/plain')

@app.route("/admin/pass.txt")
def curl_flag():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if 'curl' in user_agent or 'wget' in user_agent or 'httpie' in user_agent:
        return Response("CTF{CURL_FLAG_CRACKED_25}", mimetype='text/plain')
    return Response("403 Forbidden: Browser access not allowed", status=403)

# Optional: Prevent directory browsing or unknown paths
@app.errorhandler(404)
def not_found(e):
    return "Nothing here! Try scanning or guessing the correct endpoint.", 404
