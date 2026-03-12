import http.server
import ssl
import os

# Web papkani ishchi papka sifatida o'rnatamiz
os.chdir("Web")  # <-- bu qator Web papkani “root” qiladi

server_address = ('127.0.0.1', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# SSL kontekstini yaratish
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='../server.crt', keyfile='../server.key')  
# ../server.crt va ../server.key Web papkaning bir daraja yuqorida joylashgani uchun

# Serverni ishga tushirish
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print("HTTPS server 127.0.0.1:4443 da ishga tushdi…")
httpd.serve_forever()