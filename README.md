# Token
The key is always the same.

```
3dc90fdb6fd9cc47fb419122b695375903f3dcf40526df7d66e31e09ca44c5826dcbabc7ca996f007d86b38f822d094a02d9ceae7186d52c5450bfc8bcb545dd69547b93335811e3aa8a373f4b16955b34bb8d9951074bc57d096f14cab5011ff595871101d3ecdf3e92fc9912e9809978a9e8d6e055597095e0b28cf73a20c3
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
