import argparse

from scapy.all import rdpcap, wrpcapng

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A python program that can add and read a text comment into a packet of a PCAPNG file.')
    parser.add_argument('-f', '--file', help='PCAPNG file', required=True, type=str)
    parser.add_argument('-p', '--packet', help='packet number', required=True, type=int)
    parser.add_argument('-t', '--text', help='text to be encoded', required=False, type=str)
    args = parser.parse_args()

    packets = rdpcap(args.file)

    if args.packet >= len(packets):
        print(f"requested packet number ({args.packet}) is larger than the number of packets in the given PCAPNG file ({len(packets)})")
        exit(-1)

    if args.text is not None:
        packets[args.packet].comment = args.text
        new_file_name = f"new_{args.file}"
        wrpcapng(new_file_name, packets)
        print(new_file_name, "packets")
    else:
        comment = packets[args.packet].comment.decode()
        # according to the assignment, this should be "a JSON text printed in the console with the content of the packet"
        # let's make it JSON then
        print(f"{{\"comment\": \"{comment}\"}}")
