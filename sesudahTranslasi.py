# Import modul-modul yang diperlukan untuk membuat game menggunakan Pygame
import pygame
import sys
import math
import random

# Inisialisasi Pygame. Harus dipanggil sebelum menggunakan sebagian besar fungsi Pygame.
pygame.init()

# Definisi warna yang akan digunakan dalam game
putih = (255, 255, 255)

matahari = (255, 167, 50)
bulan = (124, 129, 173)

gedung1_siang = (135, 196, 255)
gedung2_siang = (57, 167, 255)
gedung1_malam = (124, 129, 173)
gedung2_malam = (75, 82, 126)

tiang_listrik = (32, 32, 32)
lampu_off = (32, 32, 32)
lampu_on = (255, 255, 255)

pantai_siang = (255, 238, 217)
pantai_malam = (229, 195, 166)

laut_siang = (7, 102, 173)
laut_malam = (46, 67, 116)

langit_malam = (46, 67, 116)

# Muat gambar perahu dan skala gambar ke ukuran yang diinginkan
boat = pygame.image.load('D:/.Arya/.Perkuliahan/Semester 3/Grafika/tugasAkhir/boat.png')
boat = pygame.transform.scale(boat, (85, 85))
boat_rect = boat.get_rect(midbottom=(650, 600))

# Muat gambar langit dan skala gambar ke ukuran layar
langit = pygame.image.load('D:/.Arya/.Perkuliahan/Semester 3/Grafika/tugasAkhir/sky.jpeg')
langit = pygame.transform.scale(langit, (800, 600))
langit_rect = langit.get_rect(topleft=(0, 0))

# Muat gambar mobil dan skala gambar ke ukuran yang diinginkan
car_img = pygame.image.load('D:/.Arya/.Perkuliahan/Semester 3/Grafika/tugasAkhir/car.png')
car_img = pygame.transform.scale(car_img, (65, 65))
car_rect = car_img.get_rect(midbottom=(0, 520))

# Ukuran layar
lebar = 800
tinggi = 600

# Membuat layar
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Miami City")

# Inisialisasi koordinat dan sudut matahari
x_matahari = 500
y_matahari = 500
sudut_matahari = 0

# Inisialisasi kecepatan perahu 
kecepatan_perahu = 2

# Inisialisasi kecepatan translasi matahari dan radius putar matahari
kecepatan_matahari = 1
radius_matahari = 100

# Inisialisasi kecepatan mobil
kecepatan_mobil = 3

# Inisialisasi daftar bintang
bintang_list = []
for _ in range(50):
    # Random koordinat dan ukuran bintang
    x_bintang = random.randint(0, lebar)
    y_bintang = random.randint(0, tinggi - 500)  # Menghindari area laut
    ukuran_bintang = random.randint(2, 3)
    faktor_skala = random.uniform(0.5, 1.5)  # Faktor skala acak
    bintang_list.append((x_bintang, y_bintang, ukuran_bintang, faktor_skala))
    
# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Menggambar matahari
    x_matahari = int(lebar / 2 + radius_matahari * math.cos(math.radians(sudut_matahari)))
    y_matahari = int(tinggi / 2 + radius_matahari * math.sin(math.radians(sudut_matahari)))

    # Menggambar langit
    if x_matahari <= lebar / 2:
        layar.blit(langit, langit_rect)
    else:
        layar.fill(langit_malam)
        # Menggambar bintang-bintang
         # Menggambar dan menganimasikan bintang-bintang
        for i, (x, y, ukuran, faktor_skala) in enumerate(bintang_list):
            # Menghitung skala animasi (0.5 hingga faktor_skala)
            skala_animasi = 0.5 + 0.5 * math.sin(pygame.time.get_ticks() / 1000.0 + i)

            # Menggambar bintang dengan faktor skala animasi
            ukuran_animasi = int(ukuran * faktor_skala * skala_animasi)
            pygame.draw.circle(layar, putih, (x, y), ukuran_animasi) #p ukuran

    # Jika matahari berada di setengah kiri layar, gambarkan sebagai matahari
    if x_matahari <= lebar / 2:
        pygame.draw.circle(layar, matahari, (x_matahari, y_matahari), radius_matahari)
    # Jika matahari berada di setengah kanan layar, gambarkan sebagai bulan
    else:
        pygame.draw.circle(layar, bulan, (x_matahari, y_matahari), radius_matahari)

    if x_matahari <= lebar / 2:
        # Menggambar gedung siang hari
        # (x, y, width, height)
        pygame.draw.rect(layar, gedung2_siang, (0, 300, 50, 200))
        pygame.draw.rect(layar, gedung2_siang, (50, 175, 100, 200))
        pygame.draw.rect(layar, gedung2_siang, (150, 300, 100, 200))
        pygame.draw.rect(layar, gedung2_siang, (160, 250, 50, 200))
        pygame.draw.rect(layar, gedung2_siang, (240, 190, 100, 200))
        pygame.draw.rect(layar, gedung2_siang, (300, 250, 150, 250))
        pygame.draw.rect(layar, gedung2_siang, (400, 275, 100, 300))
        pygame.draw.rect(layar, gedung2_siang, (500, 200, 100, 300))
        pygame.draw.rect(layar, gedung2_siang, (600, 235, 100, 300))
        pygame.draw.rect(layar, gedung2_siang, (700, 300, 100, 300))

        pygame.draw.rect(layar, gedung1_siang, (0, 350, 75, 300))
        pygame.draw.rect(layar, gedung1_siang, (75, 275, 100, 300))
        pygame.draw.rect(layar, gedung1_siang, (180, 325, 50, 300))
        pygame.draw.rect(layar, gedung1_siang, (230, 400, 50, 300))
        # PENENGAH
        pygame.draw.rect(layar, gedung1_siang, (250, 200, 100, 300))
        pygame.draw.rect(layar, gedung1_siang, (450, 300, 100, 300))
        pygame.draw.rect(layar, gedung1_siang, (350, 350, 75, 200))
        pygame.draw.rect(layar, gedung1_siang, (550, 350, 10, 250))
        pygame.draw.rect(layar, gedung1_siang, (560, 250, 100, 300))
        pygame.draw.rect(layar, gedung1_siang, (600, 275, 150, 300))
        pygame.draw.rect(layar, gedung1_siang, (700, 350, 150, 300))
    else:
        # Menggambar gedung-gedung pada malam hari
        # (x, y, width, height)
        pygame.draw.rect(layar, gedung2_malam, (0, 300, 50, 200))
        pygame.draw.rect(layar, gedung2_malam, (50, 175, 100, 200))
        pygame.draw.rect(layar, gedung2_malam, (150, 300, 100, 200))
        pygame.draw.rect(layar, gedung2_malam, (160, 250, 50, 200))
        pygame.draw.rect(layar, gedung2_malam, (240, 190, 100, 200))
        pygame.draw.rect(layar, gedung2_malam, (300, 250, 150, 250))
        pygame.draw.rect(layar, gedung2_malam, (400, 275, 100, 300))
        pygame.draw.rect(layar, gedung2_malam, (500, 200, 100, 300))
        pygame.draw.rect(layar, gedung2_malam, (600, 235, 100, 300))
        pygame.draw.rect(layar, gedung2_malam, (700, 300, 100, 300))

        pygame.draw.rect(layar, gedung1_malam, (0, 350, 75, 300))
        pygame.draw.rect(layar, gedung1_malam, (75, 275, 100, 300))
        pygame.draw.rect(layar, gedung1_malam, (180, 325, 50, 300))
        pygame.draw.rect(layar, gedung1_malam, (230, 400, 50, 300))
        # PENENGAH
        pygame.draw.rect(layar, gedung1_malam, (250, 200, 100, 300))
        pygame.draw.rect(layar, gedung1_malam, (450, 300, 100, 300))
        pygame.draw.rect(layar, gedung1_malam, (350, 350, 75, 200))
        pygame.draw.rect(layar, gedung1_malam, (550, 350, 10, 250))
        pygame.draw.rect(layar, gedung1_malam, (560, 250, 100, 300))
        pygame.draw.rect(layar, gedung1_malam, (600, 275, 150, 300))
        pygame.draw.rect(layar, gedung1_malam, (700, 350, 150, 300))
        

    if x_matahari <= lebar / 2:
        # Menggambar tiang listrik pada siang hari
        pygame.draw.rect(layar, tiang_listrik, (20, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (20, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (100, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (100, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (180, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (180, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (260, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (260, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (340, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (340, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (420, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (420, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (500, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (500, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (580, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (580, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (660, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (660, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (740, 450, 5, 50))
        pygame.draw.rect(layar, lampu_off, (740, 450, 20, 2))
    else:
        # Menggambar tiang listrik pada malam hari
        pygame.draw.rect(layar, tiang_listrik, (20, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (20, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (100, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (100, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (180, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (180, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (260, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (260, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (340, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (340, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (420, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (420, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (500, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (500, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (580, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (580, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (660, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (660, 450, 20, 2))

        pygame.draw.rect(layar, tiang_listrik, (740, 450, 5, 50))
        pygame.draw.rect(layar, lampu_on, (740, 450, 20, 2))

    # Menggambar laut dan pantai pada siang hari
    if x_matahari <= lebar / 2:
        pygame.draw.rect(layar, laut_siang, (0, 500, lebar, tinggi - 500))
        pygame.draw.rect(layar, pantai_siang, (0, 500, lebar, tinggi - 570))
    else:
        # Menggambar laut dan pantai pada malam hari
        pygame.draw.rect(layar, laut_malam, (0, 500, lebar, tinggi - 500))
        pygame.draw.rect(layar, pantai_malam, (0, 500, lebar, tinggi - 570))
    
    # Menggambar mobil yang bergerak di atas pantai
    layar.blit(car_img, car_rect)
    car_rect.x += kecepatan_mobil #p

    # Membuat gambar refleksi mobil
    car_reflection_img = pygame.transform.flip(car_img, False, True)
    car_reflection_rect = car_reflection_img.get_rect(midbottom=(car_rect.centerx, 575))
    # Mengatur transparansi pada gambar refleksi
    car_reflection_img.set_alpha(100)  
    # Menggambar refleksi mobil di laut dengan efek transparansi
    layar.blit(car_reflection_img, car_reflection_rect)

    # Jika mobil mencapai batas layar, kembalikan ke posisi awal
    if car_rect.right >= lebar:
        car_rect.left = 0

    # Jika refleksi mencapai batas layar, kembalikan ke posisi awal
    if car_reflection_rect.right >= lebar:
        car_reflection_rect.left = 0

    # Jika perahu mencapai batas layar, balikkan arah pergerakannya
    if boat_rect.right >= lebar or boat_rect.left <= 600:
        kecepatan_perahu = -kecepatan_perahu
    # Memperbarui posisi perahu
    boat_rect.x += kecepatan_perahu #p

    # Membuat gambar refleksi perahu
    if kecepatan_perahu > 0:  # Perahu bergerak ke kanan
        boat_reflection_img = pygame.transform.flip(boat, False, False)
    else:  # Perahu bergerak ke kiri
        boat_reflection_img = pygame.transform.flip(boat, True, False)
    
    boat_reflection_rect = boat_rect.copy()
    boat_reflection_rect.y = 2 * (tinggi - boat_rect.bottom) + boat_rect.y
    # Menggambar refleksi perahu di laut dengan efek transparansi
    layar.blit(boat_reflection_img, boat_reflection_rect)
    
    # Memperbarui koordinat matahari untuk memberikan efek animasi rotasi
    sudut_matahari += kecepatan_matahari #p

    # Memperbarui layar
    pygame.display.flip()

    # Mengatur kecepatan frame
    pygame.time.Clock().tick(60)