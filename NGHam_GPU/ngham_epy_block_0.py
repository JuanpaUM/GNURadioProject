"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import sys
sys.path.append('/home/jpv/proy/GNUradio/NGHam_GPU')

import numpy as np
from gnuradio import gr
import os
from enum import Enum
from rs import RS
from enum import Enum
from crc import Calculator, Configuration
from pyngham import PyNGHam
import time
import cProfile
import pstats

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
        with cProfile.Profile() as profile:
            path=os.getcwd()+"/20180512_231422z_436500000_43468_packets.log"
            print(path)
            with open(path, "rb") as f:
                for msg in f:
                    """ print("-------------Original Message-----------")
                    print(msg) """
                    start_time = time.time()

                    msg1=msg[0:220]
                    msg2=msg[220:]

                    pkt1 = x.encode(msg1)
                    pkt2 = x.encode(msg2)
                    #end_time = time.time()
                    """ print("-------------Chunk 1 Encoded msg-----------")
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
                    print(original_message) """
                    """ print("-----------Codification Time-----------------")
                    elapsed_time = end_time - start_time
                    print("Elapsed time: ", elapsed_time)  
                    print("---------------------------------------------") """
        
        results = pstats.Stats(profile)
        results.sort_stats(pstats.SortKey.TIME)
        results.print_stats()


