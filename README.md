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
