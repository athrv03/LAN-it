# ⚡ LAN-it: The Local Network Transfer Engine

<p align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" height="44"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CLI-Tool-000000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Encryption-Password--Based-555555?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Network-LAN-4CAF50?style=for-the-badge"/>
</p>

LAN-it is a lightweight, fast, and modular CLI tool for transferring files over a local network without requiring internet access. It is designed to demonstrate how discovery, networking, encryption, and chunked file transfer work together in a real system.

---

## Features

* Device discovery using UDP broadcast
* Fast local file transfer over TCP
* Adaptive chunk-based transfer based on measured throughput
* Password-based encryption
* Modular and extensible architecture

---

## How It Works

```
Discovery → Connection → Key Derivation → Chunking → Encrypted Transfer → Reassembly
```

1. Devices discover each other via UDP broadcast
2. The sender connects to the receiver using TCP
3. Both devices derive the same encryption key from a shared password
4. The file is split into dynamic chunks (auto-tuned to network speed)
5. Each chunk is encrypted and transmitted
6. The receiver decrypts and reconstructs the original file

---

## Requirements

### Python

* Python 3.8 or higher

### Dependencies

Install dependencies using:

```
pip install -r requirements.txt
```

`requirements.txt`:

```
cryptography
```

---

## Network Requirements

* Devices must be connected to the same local network
* Internet access is not required

---

## Ports Used

* TCP: `5001` (file transfer)
* UDP: `9999` (device discovery)

Ensure that your firewall allows traffic on these ports.

---

## Installation

```
git clone https://github.com/athrv03/LAN-it
cd LAN-it
pip install -e .
```

---

## Usage

### Start Receiver

```
lanit receive <password>
```

---

### Discover Devices

```
lanit discover
```

---

### Send File

```
lanit send <ip> "<file>" <password>
```

Chunk sizing is automatic.  
Example: on a ~10 MB/s link, a 100MB file is sent in roughly 10 chunks.

---

## Project Structure

```
lanit/
├── cli.py
├── main.py
├── discovery/
├── network/
├── transfer/
├── crypto/
└── utils/

tests/
```

---

## Security Model

* Encryption keys are derived from a shared password using SHA-256
* All file chunks are encrypted before transmission
* Decryption occurs on the receiver side

Note: This is a basic implementation intended for learning purposes.

---

## Limitations

* Works only within the same local network
* No authentication mechanism beyond shared password
* No support for resuming interrupted transfers
* Basic key derivation without salt

---

## Development Roadmap

* Resume interrupted transfers
* Progress bar and transfer speed tracking
* ECDH + AES-GCM encryption
* mDNS-based discovery
* Graphical user interface

---

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

## License

None

---

## Why LAN-it

LAN-it is designed as a practical learning project to understand how modern file transfer systems work, including networking, encryption, and system design principles.
