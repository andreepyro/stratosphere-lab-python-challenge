# stratosphere-lab-python-challenge

This repository contains a Python challenge for [Stratosphere Lab](https://www.stratosphereips.org/)

## Assignment

```text
Goal: To develop a python program that can add and read a text comment into a packet of a PCAPNG file.

Input when adding: PCAPNG file, a string of text, packet number
Output when adding: a new PCAPNG file with the comment inserted in the correct packet.

Input when reading: PCAPNG file, packet number.
Output when reading: a JSON text printed in the console with the content of the packet.

Please create your program and share with us your GitHub repository.
```

## Prerequisites

- [scapy](https://scapy.net/) (can be installed with: `pip install scapy`)

## Usage

Add a text comment to the packet in the given PCAPNG file:

  ```shell
  python3 program.py -f <filename> -p <packet_number> -t <text_comment>
  ```

Read the text comment from the packet in the given PCAPNG file:

```shell
python3 program.py -f <filename> -p <packet_number>
```
