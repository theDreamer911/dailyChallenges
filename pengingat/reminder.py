import time
from playsound import playsound

print('====== Pengingat ======')
banyak = int(input('Hendak berbunyi berapa kali: '))
interval = int(input('Hendak berbunyi setiap berapa detik: '))
print('\nProgram Berhasil di Jalankan\n')


def loop_forever():
    while True:
        n = banyak
        for i in range(n):
            time.sleep(interval)
            i += 1
            print(f'Bunyi ke-{i}')
            playsound('reminder.wav')
        if(i == banyak):
            return False


loop_forever()

print('\nSelesai\n')
