"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr
import os
from enum import Enum
from rs import RS
from enum import Enum
from crc import Calculator, Configuration
from pyngham import PyNGHam
import json


x = PyNGHam()

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='NGHam',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        self.handle_msg()

    def handle_msg(self):
            # Cantidad de mensajes
        lines=3
        carpeta_salida = "output_files"
            #msjs codificados con CPU
        patron= f"/input_files/NGHAM_Pkts_{lines}.json" 
        Orig_Msgs = f"{carpeta_salida}/Orig_Msgs_{lines}.log"    
            #msjs codificados por GPU
        patron= f"/input_files/NGHAM_GPU_Pkts_{lines}.json" 
        Orig_Msgs = f"{carpeta_salida}/Orig_Msgs_GPU_{lines}.log"

        path = os.getcwd() + patron
        print(path)
        original_msgs=[]
        # Abrir el archivo JSON en modo de lectura
        with open(path, "r") as file:
            # Cargar los datos del archivo JSON en una lista de pares de paquetes
            packet_pairs = json.load(file)

        # Iterar a través de los pares de paquetes y decodificarlos
        for pkt1, pkt2 in packet_pairs:

            decoded_data1, errors1, errors_pos1 = x.decode(pkt1)
            decoded_data2, errors2, errors_pos2 = x.decode(pkt2)
            byte_list = decoded_data1 + decoded_data2
            # Paso 2: Convertir la lista de enteros en una cadena de caracteres
            original_message = ''.join([chr(byte) for byte in byte_list])
            # Imprimir el mensaje original
            original_msgs.append(original_message)

        # Cierra el archivo
        file.close()

        
        with open(Orig_Msgs, "w") as file:
            for msg in original_msgs:
                file.write(msg)
        file.close()
        print(f"[INFO] Se ha creado el archivo {Orig_Msgs}  con los mensajes decodificados")