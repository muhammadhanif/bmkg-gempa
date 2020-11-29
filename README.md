# bmkg-gempa

A simple python library for converting [earthquake data](https://data.bmkg.go.id/gempabumi/) of [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://www.bmkg.go.id/) from XML to JSON.

## Installation

```bash
pip3 install bmkg-gempa
```

## Example

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

## Data Source

The earthquake data used in the library is obtained from [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://www.bmkg.go.id/)
