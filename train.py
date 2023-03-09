# import torch
import requests

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# uniq characters in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)

stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }

# encoder: take a string, output a list of integers
encode = lambda s: [stoi[c] for c in s]

# decoder: take a list of integers, output a string
decode = lambda l: ''.join([itos[i] for i in l])

# encode the entire text dataset and store into a torch.Tensor
# data = torch.tensor(encode(text), dtype=torch.long)
r  = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print (r.status_code)