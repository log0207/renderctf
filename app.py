from flask import Flask, send_from_directory, Response, request, abort

app = Flask(__name__)



@app.route('/')
def nmap_flag():
    ua = request.headers.get("User-Agent", "")
    if "Mozilla" in ua or "Chrome" in ua or "Safari" in ua:
        abort(403)
    return Response("CTF{NMAP_CRACKED_8527}\n", mimetype='text/plain')

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
