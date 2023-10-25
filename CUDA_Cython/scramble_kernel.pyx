# scramble_kernel.pyx
#cython: language_level=3

cdef extern from "cuda.h":
    void cudaSetDevice(int device)
    void cudaDeviceSynchronize()
    void cudaFree(void* devPtr)
    int cudaMalloc(void** devPtr, size_t size)
    void cudaMemcpy(void* dst, void* src, size_t count, int kind)
    void cudaMemcpyHostToDevice
    void cudaMemcpyDeviceToHost
    void cudaMemset(void* devPtr, int value, size_t count)
    
cdef extern from "scramble_kernel.cu":
    void scramble_kernel(unsigned char* pkt, int codeword_start, int size_nr, unsigned char* poly, int pl_par_sizes)
