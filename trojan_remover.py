from PIL import Image
import base64

def remove_payload(image_path, key):
    try:
        img = Image.open(image_path)
        payload_encoded = img.info.get('payload')
        key_encoded = img.info.get('key')

        if not payload_encoded or not key_encoded:
            print("Tidak ada payload atau kunci di dalam gambar.")
            return

        key_decoded = base64.b64decode(key_encoded).decode()

        if key_decoded == key:
            # Hapus payload dan kunci dari metadata
            del img.info['payload']
            del img.info['key']
            img.save(image_path)
            print("Payload berhasil dihapus dari gambar.")
        else:
            print("Kunci salah.")
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Path gambar yang mau dibersihin
image_path = "gambar_trojan.jpg" # Ganti sama nama file gambar lo
key = "dafaputra"

remove_payload(image_path, key)
