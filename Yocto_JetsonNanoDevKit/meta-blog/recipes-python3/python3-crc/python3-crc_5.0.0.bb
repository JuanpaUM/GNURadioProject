
SUMMARY = "Library and CLI to calculate and verify all kinds of CRC checksums"
HOMEPAGE = "https://github.com/Nicoretti/crc"
AUTHOR = "Nicola Coretti <nico.coretti@gmail.com>"
LICENSE = "BSD-2-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=f94c07350a9f2e0ce3a246fed3b32353"

SRC_URI = "https://files.pythonhosted.org/packages/6a/bb/6464df2292a73168b14ebd5903d7a29261ca2bae722754f239be75d05177/crc-5.0.0.tar.gz"
SRC_URI[md5sum] = "954fdae74a572066a5be4c13e10bbcbd"
SRC_URI[sha256sum] = "e79316c848d67e94579c0cad7be9f704f85f2cf8472517e64132a3340b7297eb"

S = "${WORKDIR}/crc-5.0.0"

RDEPENDS_${PN} = ""

inherit setuptools3
