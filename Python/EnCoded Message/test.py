import sys, time
def dothisnow():
    st = str(input("Type your message here"))
    print("Encoding '", st, "' ...",)
    return st
    encode(st)

def encode(sti):
    ' '.join(format(ord(x), 'b') for x in sti)
    print(sti)
    print("done, printing encoded message:")
    print(sti)
    time.sleep(.5)
    dothisnow()


dothisnow()
