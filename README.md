LAN-it

LAN-it is a lightweight, fast, and modular CLI tool for transferring files over a local network without internet. It demonstrates discovery, networking, encryption, and chunked file transfer.

Features

- Device discovery (UDP broadcast)
- Fast local transfers over TCP
- Chunk-based file transfer (handles large files efficiently)
- Password-based encryption
- Modular architecture

How it works

Discovery → Connection → Key derivation → Chunking → Encrypted transfer → Reassembly

1. Devices discover each other via UDP broadcast
2. Sender connects to receiver using TCP
3. Both derive the same encryption key from a shared password
4. File is split into chunks
5. Each chunk is encrypted and sent
6. Receiver decrypts and reconstructs the file

Requirements

Python 3.8+

Dependencies

pip install -r requirements.txt

requirements.txt:
cryptography

Network

- Devices must be on the same local network
- No internet required

Ports used

- TCP: 5001 (file transfer)
- UDP: 9999 (discovery)

Make sure your firewall allows these ports.

Installation

1)git clone https://github.com/athrv03/LAN-it
2)cd LAN-it
3)pip install -e .

Usage

On receiver device
lanit receive <password>

Discover devices
lanit discover

On sender device
lanit send <ip> <file> <password>

Project structure

lanit/
├── cli.py
├── main.py
├── discovery/
├── network/
├── transfer/
├── crypto/
└── utils/

tests/

Security model
- Encryption key is derived from a shared password using SHA-256
- All chunks are encrypted before transmission
- Decryption happens on receiver side

This is a simple implementation.

Limitations

- Works only on same LAN
- No authentication (any device can connect if password is known)
- No resume support
- Basic key derivation (no salt)

Development Roadmap

- Resume interrupted transfers
- Progress bar and speed tracking
- ECDH + AES-GCM encryption
- mDNS-based discovery
- Adaptive chunk sizing
- GUI version

Contributing
Contributions are welcome. Open issues and submit pull requests.

License

MIT

Why LAN-it?
LAN-it is designed for learning how file transfer systems work and understanding networking and encryption fundamentals.
