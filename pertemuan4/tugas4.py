class NamaError(Exception):
    pass

class NamaPendek(NamaError):
    def __init__(self):
        super().__init__("Nama terlalu pendek! Minimal 3 karakter.")

class NamaBukanHuruf(NamaError):
    def __init__(self):
        super().__init__("Nama hanya mengandung huruf atau spasi.")

class UmurError(Exception):
    pass

class UmurTidakValid(UmurError):
    def __init__(self):
        super().__init__("Umur tidak memenuhi syarat (17-60 tahun).")
    
class UmurBukanAngka(UmurError):
    def __init__(self):
        super().__init__("Umur hanya mengandung angka.")
    
class EmailTidakValid(Exception):
    def __init__(self):
        super().__init__("Email tidak valid! Harus mengandung '@'.")
    
class NomorError(Exception):
    pass

class NomorBukanAngka(NomorError):
    def __init__(self):
        super().__init__("No HP hanya mengandung angka.")

class NomorTidakValid(NomorError):
    def __init__(self):
        super().__init__("No HP tidak valid! Harus 10-13 digit angka.")

def input_nama(pesan):
    while True:
        try:
            nama = input(pesan)
            if not nama.replace(" ", "").isalpha():
                raise NamaBukanHuruf()
            if len(nama) < 3:
                raise NamaPendek()
            return nama
        except NamaError as e:
            print(f" [ERROR] {e}")

def input_umur(pesan):
    while True:
        try:
            umur = input(pesan)
            if not umur.isdigit():
                raise UmurBukanAngka()
            if int(umur) < 17 or int(umur) > 60:
                raise UmurTidakValid()
            return int(umur)
        except UmurError as e:
            print(f" [ERROR] {e}")

def input_email(pesan):
    while True:
        try:
            email = input(pesan)
            if '@' not in email:
                raise EmailTidakValid()
            return email
        except EmailTidakValid as e:
            print(f" [ERROR] {e}")

def input_nomor(pesan):
    while True:
        try:
            nomor = input(pesan)
            if not nomor.isdigit():
                raise NomorBukanAngka()
            if len(nomor) < 10 or len(nomor) > 13:
                raise NomorTidakValid()
            return nomor
        except NomorError as e:
            print(f" [ERROR] {e}")


def registrasi():
    print("=== REGISTRASI PESERTA SEMINAR ===")
    nama = umur = email = nomor = None
    try:
        nama = input_nama("Nama lengkap: ")
        umur = input_umur("Umur: ")
        email = input_email("Email: ")
        nomor = input_nomor("No HP: ")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print("Proses input selesai.\n")
    
    print("=== DATA PESERTA ===")
    print(f"Nama   : {nama}")
    print(f"Umur   : {umur} tahun")
    print(f"Email  : {email}")
    print(f"No HP  : {nomor}")
    print(f"Status : TERDAFTAR")


registrasi()