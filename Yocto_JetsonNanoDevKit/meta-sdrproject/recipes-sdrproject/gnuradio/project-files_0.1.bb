#SUMMARY = "GNURAdio packages"
#DESCRIPTION = "TFG"
#HOMEPAGE = ""
LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

SRCREV = "${AUTOREV}"
PV = "1.0+git${SRCPV}"

SRC_URI = "git://github.com/JuanpaUM/GNURadioProject.git;protocol=https;branch=main"

S = "${WORKDIR}/git"

do_install () {
   install -d ${D}${bindir}/PROJECT
   install -d ${D}${bindir}/PROJECT/NGHam
   install -d ${D}${bindir}/PROJECT/NGHam_GPU
   install -d ${D}${bindir}/PROJECT/NGHam_NEON
   install -d ${D}${bindir}/PROJECT/NGHam/packets
   install -d ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -d ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -d ${D}${bindir}/PROJECT/NGHam/output_files
   install -d ${D}${bindir}/PROJECT/NGHam_GPU/output_files
   install -d ${D}${bindir}/PROJECT/NGHam_NEON/output_files

   install -m 0755 ${S}/NGHam/ngham.py ${D}${bindir}/PROJECT/NGHam
   install -m 0755 ${S}/NGHam/ngham_epy_block_0.py ${D}${bindir}/PROJECT/NGHam
   install -m 0755 ${S}/NGHam/pyngham.py ${D}${bindir}/PROJECT/NGHam
   install -m 0755 ${S}/NGHam/rs.py ${D}${bindir}/PROJECT/NGHam
   install -m 0755 ${S}/NGHam/ngham.grc ${D}${bindir}/PROJECT/NGHam

   install -m 0755 ${S}/NGHam_GPU/ngham.py ${D}${bindir}/PROJECT/NGHam_GPU
   install -m 0755 ${S}/NGHam_GPU/ngham_epy_block_0.py ${D}${bindir}/PROJECT/NGHam_GPU
   install -m 0755 ${S}/NGHam_GPU/pyngham_gpu.py ${D}${bindir}/PROJECT/NGHam_GPU
   install -m 0755 ${S}/NGHam_GPU/rs.py ${D}${bindir}/PROJECT/NGHam_GPU
   install -m 0755 ${S}/NGHam_GPU/ngham.grc ${D}${bindir}/PROJECT/NGHam_GPU

   install -m 0755 ${S}/NGHam_NEON/ngham.py ${D}${bindir}/PROJECT/NGHam_NEON
   install -m 0755 ${S}/NGHam_NEON/ngham_epy_block_0.py ${D}${bindir}/PROJECT/NGHam_NEON
   install -m 0755 ${S}/NGHam_NEON/pyngham_neon.py ${D}${bindir}/PROJECT/NGHam_NEON
   install -m 0755 ${S}/NGHam_NEON/rs.py ${D}${bindir}/PROJECT/NGHam_NEON
   install -m 0755 ${S}/NGHam_NEON/ngham.grc ${D}${bindir}/PROJECT/NGHam_NEON
   install -m 0755 ${S}/NGHam_NEON/scrambler.cpp ${D}${bindir}/PROJECT/NGHam_NEON

   install -m 0755 ${S}/NGHam/packets/3_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/102_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/1002_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/5001_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/10002_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/50002_packets.log ${D}${bindir}/PROJECT/NGHam/packets
   install -m 0755 ${S}/NGHam/packets/100001_packets.log ${D}${bindir}/PROJECT/NGHam/packets

   install -m 0755 ${S}/NGHam_GPU/packets/3_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/102_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/1002_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/5001_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/10002_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/50002_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets
   install -m 0755 ${S}/NGHam_GPU/packets/100001_packets.log ${D}${bindir}/PROJECT/NGHam_GPU/packets

   install -m 0755 ${S}/NGHam_NEON/packets/3_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/102_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/1002_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/5001_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/10002_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/50002_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
   install -m 0755 ${S}/NGHam_NEON/packets/100001_packets.log ${D}${bindir}/PROJECT/NGHam_NEON/packets
}
