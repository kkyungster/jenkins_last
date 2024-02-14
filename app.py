# app.py

from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def system_info():
    client_ip = request.remote_addr
    server_host = socket.gethostname()
    server_ip = socket.gethostbyname(server_host)
    return f"""
    <h1>시스템 정보 v5 </h1>
    <p><strong>접속한 클라이언트 IP:</strong> {client_ip}</p>
    <p><strong>서버 호스트 명:</strong> {server_host}</p>
    <p><strong>서버 IP:</strong> {server_ip}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
