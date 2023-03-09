# import torch
import torch 

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
# which essentially converts each character of text into an int
data = torch.tensor(encode(text), dtype=torch.long)

# get the first 1,000 characters in the text
# print(data[:1000])