# Split Alignment Test Harness
Evaluate email service providers for security and deliverability under the Split Alignment configuration.

## Generating DKIM Keys

Private Key:
```bash
openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:1024
```

Public Key:
```bash
openssl rsa -in private.key -pubout -out public.key
```

# Cite this paper

```
@inproceedings{hamza2026splitalignment,
  author    = {Muhammad Hamza and Mattijs Jonker and Raffaele Sommese and Simon Fernandez and Olivier Hureau and Eric Pauley and Taejoong Chung},
  title     = {{Split Alignment: Diffusing SPF Vulnerabilities With DMARC}},
  booktitle = {Proceedings of the 2026 ACM Internet Measurement Conference},
  series    = {IMC '26},
  address   = {Karlsruhe, Germany},
  year      = {2026}
  publisher = {ACM},
  doi       = {10.1145/3777912.3809146}
}
```
