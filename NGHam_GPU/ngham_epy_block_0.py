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
from pyngham_gpu import PyNGHam
import cProfile
import pstats
import json

x = PyNGHam()

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='NGHam_Encode_GPU',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        self.handle_msg()

    def handle_msg(self):
        # Carpeta de Salida de los archivos
        carpeta_salida = "output_files/"
        counter=0
        packet_1 = []
        packet_2 = []
        with cProfile.Profile() as profile:
            path=os.getcwd()+"/packets/3_packets.log"
            print("[INFO] Codificando los mensajes del archivo:" + path)
            with open(path, "rb") as f:
                for msg in f:
                    counter += 1

                    msg1=msg[0:220]
                    msg2=msg[220:]
                    pkt1 = x.encode(msg1)
                    pkt2 = x.encode(msg2)
                    packet_1.append(pkt1) 
                    packet_2.append(pkt2)

            f.close()
            pkt1_res=x.scramble_packet(packet_1,counter)
            pkt2_res=x.scramble_packet(packet_2,counter)
            profile.disable()

        # Archivo con los mensajes codificados
        packet_pairs = []
        if pkt1_res.shape[0] == pkt2_res.shape[0]:
            num_filas = pkt1_res.shape[0]
            # Combinar las filas en pares
            for i in range(num_filas):
                pkt1_row = pkt1_res[i, :].tolist()
                pkt2_row = pkt2_res[i, :].tolist()
                packet_pair = (pkt1_row, pkt2_row)
                packet_pairs.append(packet_pair)
        else:
            print("Las matrices tienen un número diferente de filas.") 
        # Guardar los datos en un archivo JSON
        NGHAM_Cod = f"{carpeta_salida}/NGHAM_Pkts_{counter}.json"
        with open(NGHAM_Cod, "w") as file:
            json.dump(packet_pairs, file) 
        print(f"[INFO] Se ha creado el archivo {NGHAM_Cod} con los mensajes codificados")

        # Archivo con las estadisticas de codificación
        NGHAM_Stats = f"{carpeta_salida}/NGHAM-GPU_EncodeStats_{counter}.txt"
        with open(NGHAM_Stats, 'w') as f:
            stats = pstats.Stats(profile, stream=f)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.print_stats()
        f.close()
        print(f"[INFO] Se ha creado el archivo {NGHAM_Stats} con las estadisticas de codificación")