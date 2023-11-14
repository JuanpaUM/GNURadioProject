#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <arm_neon.h>

namespace py = pybind11;

py::array_t<uint8_t> scramble_packet_neon(py::array_t<uint8_t> pkt, py::array_t<uint8_t> poly) {
    auto pkt_rw = pkt.mutable_unchecked<1>();  // Read-write view of the packet array
    auto poly_rw = poly.unchecked<1>();  // Read-only view of the poly array
    size_t size = pkt_rw.size();

    size_t i;
    for (i = 0; i + 16 <= size; i += 16) {
        uint8x16_t pkt_neon = vld1q_u8(pkt_rw.mutable_data(0) + 11 + i);
        uint8x16_t poly_neon = vld1q_u8(poly_rw.data(0) + i);
        uint8x16_t result = veorq_u8(pkt_neon, poly_neon);
        vst1q_u8(pkt_rw.mutable_data(0) + 11 + i, result);
    }

    // Procesar los elementos restantes de forma secuencial
    for (; i < size; ++i) {
        pkt_rw.mutable_data(0)[11 + i] = pkt_rw.data(0)[11 + i] ^ poly_rw.data(0)[i];
    }

    // Devolver el array modificado
    return pkt;
}

PYBIND11_MODULE(scrambler, m) {
    m.def("scramble_packet_neon", &scramble_packet_neon, "Scramble the packet using Neon intrinsics");
}

