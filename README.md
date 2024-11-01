# Micronas CDC3217G J-Link Commander "CommandFile" generator script
JLink command file generator python script for flashing Micronas CDC3217G with J-Link

Usage: python genJlinkCmdFile.py <inputFileName.bin> <outputFileName.jlink>

For example: python genJlinkCmdFile.py 8P0920983G.bin 983g.jlink
After generation, you should use it with J-Link commander like this:

./JLinkExe -CommandFile 983g.jlink

More info : https://wiki.segger.com/J-Link_Commander
