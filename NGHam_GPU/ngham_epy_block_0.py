"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import sys
sys.path.append('/home/jpv/proy/ProyGit/GNURadioProject/NGHam_GPU')

import numpy as np
from gnuradio import gr
import os
from enum import Enum
from rs import RS
from enum import Enum
from crc import Calculator, Configuration
from pyngham import PyNGHam
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
            name='NGHam',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        self.handle_msg()

    def handle_msg(self):
        counter=0
        packet_pairs = []
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
                    packet_pairs.append((pkt1, pkt2))
        profile.disable()

        # Nombre del archivo con las estadisticas de codificación
        carpeta_salida = "output_files"
        NGHAM_Stats = f"{carpeta_salida}/NGHAM-GPU_EncodeStats_{counter}.txt"

        with open(NGHAM_Stats, 'w') as f:
            # Redirige la salida al archivo
            stats = pstats.Stats(profile, stream=f)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.print_stats()
        f.close()
        print(f"[INFO] Se ha creado el archivo {NGHAM_Stats} con las estadisticas de codificación")

        # Nombre del archivo con los mensajes codificados
        NGHAM_Cod = f"{carpeta_salida}/NGHAM_Pkts_{counter}.json"
        json_data = json.dumps(packet_pairs, default=lambda x: int(x))
        with open(NGHAM_Cod, "w") as file:
            file.write(json_data)
        file.close()
        print(f"[INFO] Se ha creado el archivo {NGHAM_Cod}  con los mensajes codificados")