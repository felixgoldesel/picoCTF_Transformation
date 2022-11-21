message = input()


enc = message.split()

for i in range(0, len(enc), 2):

    print(chr((ord(enc[i]) << 8) + ord(enc[i + 1])))

