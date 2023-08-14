import hashlib

prefix = "oGKlnMXRHQ"
target = "e536047"

def find_matching_hash():
    counter = 19894263
    while True:
        guess = str(counter)
        data = prefix + guess
        md5_hash = hashlib.md5(data.encode()).hexdigest()

        if md5_hash.startswith(target):
            print(md5_hash)
            return guess
        
        counter += 1

if __name__ == "__main__":
    matching_guess = find_matching_hash()
    print("Matching guess:", matching_guess)
