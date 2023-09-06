def oyun_tahtasi_goster(oyun_tahtasi):
    for satir in oyun_tahtasi:
        print(" | ".join(satir))
        print("-" * 9)

def oyun_tahtasi_olustur():
    return [[" " for _ in range(3)] for _ in range(3)]

def hamle_yap(oyun_tahtasi, oyuncu, satir, sutun):
    if oyun_tahtasi[satir][sutun] == " ":
        oyun_tahtasi[satir][sutun] = oyuncu
        return True
    else:
        print("Bu alan zaten dolu.")
        return False

def kazanan_mi(oyun_tahtasi, oyuncu):
    for i in range(3):
        if all(oyun_tahtasi[i][j] == oyuncu for j in range(3)):
            return True

    for j in range(3):
        if all(oyun_tahtasi[i][j] == oyuncu for i in range(3)):
            return True

    if all(oyun_tahtasi[i][i] == oyuncu for i in range(3)) or all(oyun_tahtasi[i][2 - i] == oyuncu for i in range(3)):
        return True

    return False

def oyun():
    oyun_tahtasi = oyun_tahtasi_olustur()
    sira = "X"
    kazanan = None

    while True:
        oyun_tahtasi_goster(oyun_tahtasi)
        print(f"Sıra: {sira}")
        satir = int(input("Satır seçin (0, 1, 2): "))
        sutun = int(input("Sütun seçin (0, 1, 2): "))

        if satir < 0 or satir > 2 or sutun < 0 or sutun > 2:
            print("Geçersiz hamle! Satır ve sütun 0, 1 veya 2 olmalı.")
            continue

        if hamle_yap(oyun_tahtasi, sira, satir, sutun):
            if kazanan_mi(oyun_tahtasi, sira):
                kazanan = sira
                break
            elif " " not in [satir for sutun in oyun_tahtasi for satir in sutun]:
                break
            sira = "O" if sira == "X" else "X"

    oyun_tahtasi_goster(oyun_tahtasi)
    if kazanan:
        print(f"{kazanan} kazandı!")
    else:
        print("Oyun berabere!")

if __name__ == "__main__":
    oyun()
