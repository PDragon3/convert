# Easy one
The key is always the same.

```
a162b3d8aa2f0b1adeed785e56735ace4c9db54b86b7df6c4ddeeddc168a04da440ae6cf0552cb99b3e1988090f4bdd2962193e781cf7857385af5757cfd608af2c5a9fb12807110c1c2e429f0458f7f66a776a2bf4767f332ae3553b1eafd08c0ccf77ca8e95b62c0beac4679b906534959e4ad4128c0715ef603b652a90d09
```

## Requirements
- Python 3
- ``pip install pycryptodome``
## Usage
```
python3 convert.py # Interactive mode
```
```
python3 convert.py [mode] [key] [message] # Direct mode
```

## Example
```bash
python3 convert.py 1 14071997 'Hello, World!' 
python3 convert.py 2 14071997 93238cb038636931fcc895e3021bfa5eb0355afdf640717e00446fc2142e456b 
```
# TODO :
- Update readme
- Add nickname feature
- Improve client cli
