from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode
from base64 import b64decode


key = "01234567890123456"
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

with open ("Data.txt","rb") as entry:
  data = entry.read()
  cipher = AES.new(key,AES.MODE_CFB)
  ciphertext = cipher.encrypt(pad(data,AES.block_size))
  iv = b64encode(cipher.iv).decode('UTF-8')
  ciphertext = b64encode(ciphertext).decode('UTF-8')
  to_write = iv + ciphertext
entry.close()
with open("Data.txt"+'.enc','w+') as data:
  data.write(to_write)
data.close()


with open("Data.txt.enc",'r') as d:
  f=d.read()
print(f)
