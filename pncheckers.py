# Coded By Haket
# Owned By Haket
# ©Haket - 2024 - 2026
import sys
import pytz
import pycountry
import phonenumbers
from os import system
from datetime import datetime
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from geopy.geocoders import Nominatim
from phonenumbers import PhoneNumberType, number_type

# Membersihkan Layar Terminal
system("clear")

# Pemasukkan Nomor
input_nomor = input("Masukkan Nomor: ")
if input_nomor == "":
   sys.exit()
system("clear")

# Ekstrak Nomor
nomor = phonenumbers.parse(input_nomor, None)

# Cek Validasi Nomor || Teknik F-String
valid = "Ya" if phonenumbers.is_valid_number(nomor) else "Tidak"

# Negara
negara = geocoder.description_for_number(nomor, "id")

# Koordinat Zona Waktu || Hanya Bisa Saat Online
# geolokasi = Nominatim(user_agent="geoapi")
# alamat = "Jakarta, Indonesia"
# lokasi = geolokasi.geocode(alamat)

# Zona Waktu
zona_waktu = timezone.time_zones_for_number(nomor)

# Tipe Nomor || Teknik F-String1
tipe = number_type(nomor)
tipe_nomor = ""
if tipe == PhoneNumberType.MOBILE:
   tipe_nomor = "Nomor Handphone"
elif tipe == PhoneNumberType.FIXED_LINE:
   tipe_nomor = "Nomor Tetap"
else:
   tipe_nomor = "Nomor Lain"

# Kode Negara
kode_negara = phonenumbers.region_code_for_number(nomor)

# Nomor Negara
nomor_negara = f"{nomor.country_code}"

# Cek Operator Jaringan Nomor
operator = carrier.name_for_number(nomor, "id")
if not operator:
   operator = "Tidak Ada"

# Format Negara Alpha 3
nama_negara = pycountry.countries.get(alpha_2=kode_negara)
negara_format_tiga = ""
if nama_negara:
   negara_format_tiga = nama_negara.alpha_3
else:
   negara_format_tiga = "Tidak Ditemukan"

# Nomor Nasional
nomor_nasional = nomor.national_number

# Format Nomor Nasional
format_nomor_nasional = phonenumbers.format_number(nomor, phonenumbers.PhoneNumberFormat.NATIONAL)

# Format Nomor Internasional
format_nomor_internasional = phonenumbers.format_number(nomor, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

# Cek Nomor Dari Wilayah Geografis True/False
nomor_geografis = phonenumbers.is_number_geographical(nomor)

# Waktu Zona Waktu
setel_waktu = pytz.timezone(zona_waktu[0])
waktu_sekarang = datetime.utcnow()
waktu = pytz.utc.localize(waktu_sekarang).astimezone(setel_waktu)

# Hasil
print(f"Nomor               : {input_nomor}")
print(f"Valid               : {valid}")
print(f"Negara              : {negara}")
# print(f"Koordinat           : {lokasi.latitude} {lokasi.longitude}") || Hanya Bisa Saat Online
print(f"Zona Waktu          : {', '.join(zona_waktu)}")
print(f"Tipe Nomor          : {tipe_nomor}")
print(f"Kode Negara         : {kode_negara}")
print(f"Nomor Negara        : (+{nomor_negara})")
print(f"Nama Operator       : {operator}")
#print(f"Nomor Numerik       : {
print(f"Negara Alpha-3      : {negara_format_tiga}")
print(f"Nomor Nasional      : {nomor_nasional}")
print(f"Format Nasional     : {format_nomor_nasional}")
print(f"Format Internasional: {format_nomor_internasional}")
print(f"Waktu {', '.join(zona_waktu)}  : {waktu.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Nomor Dari Wilayah Geografis: {nomor_geografis}")
