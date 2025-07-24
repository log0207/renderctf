from flask import Flask, send_from_directory, Response, request, abort

app = Flask(__name__)


@app.route("/")
def flag():
    user_agent = request.headers.get("User-Agent", "")
    # Block browsers but allow nmap, nc, or curl
    if "Mozilla" in user_agent or "Chrome" in user_agent or "Safari" in user_agent:
        abort(403)  # Forbidden
    return "CTF{NMAP_CRACKED_8527}"

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
