import cv2
import os
import vigenere

def lsb1_stegano_with_vigenere(image_path, message, password):
    encrypted_message = vigenere.vigenere(message, password, True)
    lsb1_stegano(image_path, encrypted_message)

def lsb1_extract_message_with_vigenere(watermarked_image_path, password):
    hidden_message = lsb1_extract_message(watermarked_image_path)
    decrypted_message = vigenere.vigenere(hidden_message, password, False)
    return decrypted_message

def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path)
    image_array = image_array - image_array % 2
    binary_message = ''.join(format(ord(carac), '08b') for carac in message)

    if len(binary_message) > image_array.size:
        raise Exception("La taille du message est supérieure aux nombres de pixels présent dans l'image")

    nb_rows, nb_cols, nb_canals = image_array.shape
    index_binary_message = 0
    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            for index_canal in range(nb_canals):
                if index_binary_message < len(binary_message):
                    image_array[index_row, index_col, index_canal] += int(binary_message[index_binary_message])
                    index_binary_message += 1
                else:
                    break

    cv2.imwrite("../watermarked_image.png", image_array)

def lsb1_extract_message(watermarked_image_path):
    watermarked_image_array = cv2.imread(watermarked_image_path)
    binary_array_message = watermarked_image_array % 2

    nb_rows, nb_cols, nb_canals = binary_array_message.shape

    binary_message_list = []

    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            for index_canal in range(nb_canals):
                binary_message_list.append(str(binary_array_message[index_row, index_col, index_canal]))

    for index_binary_char in range(0, nb_rows * nb_cols * nb_canals, 8):
        if binary_message_list[index_binary_char: index_binary_char + 8] == ["0"] * 8:
            binary_message_list = binary_message_list[:index_binary_char]
            break

    binary_message = "".join(binary_message_list)
    hidden_message = "".join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])

    return hidden_message