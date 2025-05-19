import streamlit as st

# Fungsi Gronsfeld Cipher
def gronsfeld_encrypt(plaintext, key):
    ciphertext = ''
    key_digits = [int(k) for k in key]
    key_len = len(key_digits)
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            shift = key_digits[i % key_len]
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def gronsfeld_decrypt(ciphertext, key):
    plaintext = ''
    key_digits = [int(k) for k in key]
    key_len = len(key_digits)
    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            shift = key_digits[i % key_len]
            new_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

# Fungsi Atbash Cipher
def atbash_cipher(text):
    result = ''
    for char in text.upper():
        if char.isalpha():
            result += chr(90 - (ord(char) - 65))
        else:
            result += char
    return result

# Streamlit UI
st.title("🔐 Aplikasi Keamanan Data - Gronsfeld + Atbash Cipher")

menu = st.sidebar.selectbox("Pilih Operasi", ["Enkripsi", "Dekripsi"])

if menu == "Enkripsi":
    plaintext = st.text_area("Masukkan Plaintext")
    key = st.text_input("Masukkan Kunci Gronsfeld (angka)", max_chars=10)

    if st.button("Enkripsi"):
        if not key.isdigit():
            st.error("Kunci Gronsfeld harus berupa angka.")
        else:
            gronsfeld_result = gronsfeld_encrypt(plaintext, key)
            final_cipher = atbash_cipher(gronsfeld_result)
            st.success("Hasil Enkripsi:")
            st.code(final_cipher)

elif menu == "Dekripsi":
    ciphertext = st.text_area("Masukkan Ciphertext")
    key = st.text_input("Masukkan Kunci Gronsfeld (angka)", max_chars=10)

    if st.button("Dekripsi"):
        if not key.isdigit():
            st.error("Kunci Gronsfeld harus berupa angka.")
        else:
            after_atbash = atbash_cipher(ciphertext)
            final_plain = gronsfeld_decrypt(after_atbash, key)
            st.success("Hasil Dekripsi:")
            st.code(final_plain)

