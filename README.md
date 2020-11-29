# bmkg-gempa

Pustaka Python untuk konversi data gempa bumi yang bersumber dari [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://www.bmkg.go.id/) dari XML ke JSON.

## Instalasi

```bash
pip3 install bmkg-gempa
```

## Contoh Program

### Gempa Bumi M 5.0+ Terkini

```python
from bmkg import Gempa

gempa = Gempa()

print(gempa.m_5_terkini())
```

### 60 Gempa Bumi M 5.0+

```python
from bmkg import Gempa

gempa = Gempa()

print(gempa.m_5())
```

### 20 Gempa Bumi Dirasakan

```python
from bmkg import Gempa

gempa = Gempa()

print(gempa.dirasakan())

```

### Gempa Bumi Berpotensi Tsunami Terkini

```python
from bmkg import Gempa

gempa = Gempa()

print(gempa.tsunami_terkini())
```

## Sumber Data

Data gempa bumi yang digunakan di pustaka ini diperoleh dari [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://www.bmkg.go.id/).

## Donasi

Jika kalian ingin berdonasi, silahkan menghubungi kami melalui jalur berikut ini:

- Email: moehammadhanif@gmail.com
- Telegram: [t.me/muhammad_hanif](https://t.me/muhammad_hanif)
