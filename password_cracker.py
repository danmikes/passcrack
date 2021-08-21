import hashlib

def crack(word):
  enc_word = word.encode()
  hash_obj = hashlib.sha1(enc_word)
  hex_val = hash_obj.hexdigest()
  return hex_val

def crack_sha1_hash(hash, use_salts=False):
  # open top-10000-passwords.txt:
  with open('top-10000-passwords.txt','r') as file:
    # read each password
    for line in file:
      word = line.rstrip()
      if use_salts == False:
        secret = crack(word)
        # compare with hash
        if secret == hash:
          return word
      elif use_salts == True:
        with open('known-salts.txt','r') as salts:
          # read each salt
          for line in salts:
            salt = line.rstrip()
            # prepend salt
            salt_word = salt + word
            secret = crack(salt_word)
            # compare with hash
            if secret == hash:
              return word
            # append salt
            word_salt = word + salt
            secret = crack(word_salt)
            if secret == hash:
              return word
    file.close()
  return "PASSWORD NOT IN DATABASE"
