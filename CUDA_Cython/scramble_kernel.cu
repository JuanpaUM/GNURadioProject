// scramble_kernel.cu
__global__ void scramble_kernel(unsigned char* pkt, int codeword_start, int size_nr, unsigned char* poly, int pl_par_sizes) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < pl_par_sizes) {
        pkt[codeword_start + idx] ^= poly[idx];
    }
}
