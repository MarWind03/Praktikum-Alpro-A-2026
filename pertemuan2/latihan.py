# NO 1
def fizzbuzz_plus(n):
    for i in range(1, n+1):
        if  i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz" , end = "")
        elif i % 3 == 0:
            print("Fizz", end = "")
            if i % 7 == 0:
                print("Seven", end = "")
        elif i % 5 == 0:
            print("Buzz", end = "")
            if i % 7 == 0:
                print("Seven", end = "")
        elif i % 7 == 0:
            print("Seven" , end = "")
        else:
            print(i, end = "")
        print('')
# fizzbuzz_plus(21)

# NO 2
def is_password_valid(password):
    panjang = len(password)
    kapital = False
    angka = False
    spasi = True
    for c in password:
        if c >= 'A' and c <= 'Z':
            kapital = True
        if c >= '0' and c <= '9':
            angka = True
        if c == ' ':
            spasi = False
    if kapital and angka and spasi and panjang >= 8:
        return True
    else:
        return False
    
# print(is_password_valid("Password123")) # True
# print(is_password_valid("password")) # False
# print(is_password_valid("Pass 123")) # False

# NO 3
def hitung_nilai(tugas, uts, uas):
    nilai = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas) 
    print("Nilai :", nilai)
    print("Grade : " , end="")

    if nilai >= 85:
        print("A")
    elif nilai >= 70:
        print("B")
    elif nilai >= 55:
        print("C")
    elif nilai >= 40:
        print("D")
    else:
        print("E")


hitung_nilai(90, 90, 90)