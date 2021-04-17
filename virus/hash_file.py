import hashlib


def hash_file(filename):
    h = hashlib.sha1()

# sha1
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

# md5
    i = hashlib.md5()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            i.update(chunk)

# sha256
    j = hashlib.sha256()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            j.update(chunk)

# sha384
    l = hashlib.sha384()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            l.update(chunk)

# sha512
    m = hashlib.sha512()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            m.update(chunk)

    return f"""File: {filename}
    ===Hasil hash===
mda5    : {j.hexdigest()}
sha-1   : {h.hexdigest()}
sha-256 : {j.hexdigest()}
sha-384 : {l.hexdigest()}
sha-512 : {m.hexdigest()}
    """


message = hash_file('Lab01-01.dll')
print(message)


# File: Lab01-02.exe
#     ===Hasil hash===
# mda5    : c876a332d7dd8da331cb8eee7ab7bf32752834d4b2b54eaa362674a2a48f64a6
# sha-1   : 5a016facbcb77e2009a01ea5c67b39af209c3fcb
# sha-256 : c876a332d7dd8da331cb8eee7ab7bf32752834d4b2b54eaa362674a2a48f64a6
# sha-384 : 97127e434621e60d4fda17c100feb567c12f695dde28dd0a31de2ebba6546192eced3fbbc0a9923ece87477a2589eb0a
# sha-512 : 0e2ceca7588462380d4c523dd59ffae8419f9ef0b5f9df4c319b0d6f076d3b5b31ec97ae979614b1557c846b2df4db5e07abd8885a95079cd68b24a02cda4979
