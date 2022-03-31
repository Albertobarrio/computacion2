with open('test.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    test_breeds = reader.readlines()
    print(test_breeds)

with open('test_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in test_breeds:
        writer.write(breed)

with open('choco.png','rb') as foto_byte:
    print(foto_byte.read(10))
    