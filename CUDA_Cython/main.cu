// main.cu
#include <iostream>

extern "C" void scramble_kernel(unsigned char* pkt, int codeword_start, int size_nr, unsigned char* poly, int pl_par_sizes);

int main() {
    const int N = 256;
    unsigned char pkt[N];
    unsigned char poly[N];

    // Inicializa pkt y poly

    scramble_kernel(pkt, 0, N, poly, N);

    // Realiza otras operaciones si es necesario

    std::cout << "Kernel ejecutado con éxito" << std::endl;

    return 0;
}