print ("@@@@@@     @@@  @@@@@@@@  @@@@@@@@@ @@@ ")
print ("@   @      @@@  @         @       @ @@@ ")
print ("@    @     @@@  @         @       @ @@@ ")
print ("@     @    @@@  @         @       @ @@@ ")
print ("@      @   @@@  @         @       @ @@@ ")
print ("@     @    @@@  @@@@@@@@  @       @ @@@ ")
print ("@    @     @@@  @         @       @ @@@ ")
print ("@  @       @@@  @         @       @ @@@ ")
print ("@   @      @@@  @         @@@@@@@@@ @@@ ")
print ("@    @     @@@  @               @   @@@ ")
print ("@     @    @@@  @                @  @@@ ") 
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

jumlah_hari = 0

hari_per_bulan = {
    1: 31,
    2: 28 if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) else 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

while bulan < 1 or bulan > 12:
    bulan = int(input("Masukkan bulan yang valid (1-12): "))

jumlah_hari = hari_per_bulan[bulan]

print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")
