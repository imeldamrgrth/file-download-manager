from pySmartDL import SmartDL


def download_file(url):
    obj = SmartDL(url, "./")
    obj.start()
    print("File sedang didownload.")

    if obj.isSuccessful():
        destination_download = obj.get_dest()
        print("Sukses download file.")
        print("File kamu ada di ", destination_download)
    else:
        print("Terjadi kesalahan ketika mengunduh.")


def main():
    print("Selamat datang di Download Manager Imelda")
    while True:
        print("================= MENU =================")
        print("1. Download")
        print("0. Exit")

        inputs = int(input("Masukkan menu: "))

        if inputs == 1:
            url = input("Masukkan URL yang ingin didownload: ")
            download_file(url)

            is_next = input("Apakah ingin mengunduh lagi? [y/n]: ")
            if is_next == "n" or is_next == "N":
                break
        else:
            break


main()
