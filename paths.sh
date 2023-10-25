#!/bin/bash
export CUDA_HOME=/usr/local/cuda-10.2
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64
export PATH=$PATH:$CUDA_HOME/bin
