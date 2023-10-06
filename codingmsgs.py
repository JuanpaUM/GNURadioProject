from pyngham import PyNGHam

x = PyNGHam()

path="20180512_231422z_436500000_43468_packets.log"
with open(path, "rb") as f:
    for msg in f:
        print("-------------Original Message-----------")
        print(msg)
        msg1=msg[0:220]
        msg2=msg[220:]

        pkt1 = x.encode(msg1)
        pkt2 = x.encode(msg2)
        print("-------------Chunk 1 Encoded msg-----------")
        print(pkt1)
        #pkt[30] = 5
        print("-------------Chunk 2 Encoded msg-----------")
        print(pkt1)

        print("-------------Chunk 1 Decoded msg-----------")
        decoded_data1, errors1, errors_pos1 = x.decode(pkt1)

        print("Decoded data:", decoded_data1)
        print("Number of errors:", errors1)
        print("Errors positions:", errors_pos1)

        print("-------------Chunk 2 Decoded msg-----------")
        decoded_data2, errors2, errors_pos2 = x.decode(pkt2)

        print("Decoded data:", decoded_data2)
        print("Number of errors:", errors2)
        print("Errors positions:", errors_pos2)

        print("-------------Get Original Message-----------")
        byte_list = decoded_data1 + decoded_data2
        # Paso 2: Convertir la lista de enteros en una cadena de caracteres
        original_message = ''.join([chr(byte) for byte in byte_list])
        # Imprimir el mensaje original
        print(original_message)
        print("---------------------------------------------")


