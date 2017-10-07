#from pynq.lib.logictools.waveform import draw_wavedrom

string1 = "h..l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.h." + \
          "llh.l.l....l...h.l.h.l.h.l.h.l.h.l." + \
          "h.l.h.l.h.l.lh.l.l....l...h.l.h.l.h" + \
          ".l.h.l.h.l.h.l.h.l.h.l.lh.l.l....l." + \
          "..h.l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.l" + \
          "h.l.l....l...h.l.h.l.h.l.h.l.h.l.h." + \
          "l.h.l.h.l.lh.l.l....l...h.l.h.l.h.l" + \
          ".h.l.h.l.h.l.h.l.h.l.lh.l.l....l..." + \
          "h.l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh." + \
          "l.l....l...h.l.h.l.h.l.h.l.h.l.h.l." + \
          "h.l.h.l.lh.l.l....l...h.l.h.l.h.l.h" + \
          ".l.h.l.h.l.h.l.h.l.lh.l.l....l...h." + \
          "l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l." + \
          "l....l...h.l.h.l.h.l.h.l.h.l.h.l.h." + \
          "l.h.l.lh.l.l....l...h.l.h.l.h.l.h.l" + \
          ".h.l.h.l.h.l.h.l.lh.l.l....l...h.l." + \
          "h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l." + \
          "...l...h.l.h.l.h.l.h.l.h.l.h.l.h.l." + \
          "h.l.lh.l.l....l...h.l.h.l.h.l.h.l.h" + \
          ".l.h.l.h.l.h.l.lh.l.l....l...h.l.h." + \
          "l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l..." + \
          ".l...h.l.h.l.h.l.h.l.h.l.h.l.h.l.h." + \
          "l.lh.l.l....l...h.l.h.l.h.l.h.l.h.l" + \
          ".h.l.h.l.h.l.lh.l.l....l...h.l.h.l." + \
          "h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l....l" + \
          "...h.l.h.l.h.l.h.l.h.l.h.l.h.l.h.l." + \
          "lh.l.l....l...h.l.h.l.h.l.h.l.h.l.h" + \
          ".l.h.l.h.l.lh.l.l....l...h.l.h.l.h." + \
          "l.h.l.h.l.h.l.h.l.h.l.lh.l.l....l.." + \
          ".h.l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh" + \
          ".l.l....l...h.l.h.l.h.l.h.l.h.l.h.l" + \
          ".h.l.h.l.lh.l.l....l...h.l.h.l.h.l." + \
          "h.l.h.l.h.l.h.l.h.l.lh.l.l....l...h" + \
          ".l.h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l" + \
          ".l....l...h.l.h.l.h.l.h.l.h.l.h.l.h" + \
          ".l.h.l.lh.l.l....l...h.l.h.l.h.l.h." + \
          "l.h.l.h.l.h.l.h.l.lh.l.l....l...h.l" + \
          ".h.l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l" + \
          "....l...h.l.h.l.h.l.h.l.h.l.h.l.h.l" + \
          ".h.l.lh.l.l....l...h.l.h.l.h.l.h.l." + \
          "h.l.h.l.h.l.h.l.lh.l.l....l...h.l.h" + \
          ".l.h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l.." + \
          "..l...h.l.h.l.h.l.h.l.h.l.h.l.h.l.h" + \
          ".l.lh.l.l....l...h.l.h.l.h.l.h.l.h." + \
          "l.h.l.h.l.h.l.lh.l.l....l...h.l.h.l" + \
          ".h.l.h.l.h.l.h.l.h.l.h.l.lh.l.l...."
            

string2 = "h.l..h..l....h..l....h..l....h..l.." + \
          ".l....lh...hl..l...h......l....h..l" + \
          "............l....lh...hl..l...h...." + \
          ".......l...h...l.......l....lh...hl" + \
          "..l...h...........l...h...l.......l" + \
          "....lh...hl..l...h...........l....." + \
          "..........l....lh...hl..l...h......" + \
          ".....l.......h.......l....lh...hl.." + \
          "l.......h...........l...h...l...l.." + \
          "..lh...hl..l.......h...l...h......." + \
          "........l....lh...hl..l.......h...l" + \
          "...h...............l....lh...hl..l." + \
          "..h.......l.......h...........l...." + \
          "lh...hl..l...h.......l...h...l....." + \
          "..h...l....lh...hl..l...h.........." + \
          ".l...h...l.......l....lh...hl..l..." + \
          "h.......l...h...l.......l...l....lh" + \
          "...hl..l...h...........l...h...l..." + \
          "h...l....lh...hl..l...h.......l...." + \
          ".......h...l...l....lh...hl..l....." + \
          "..h...l...h...........l...l....lh.." + \
          ".hl..l...h.......l...........h....." + \
          "..l....lh...hl..l...h.......l...h.." + \
          ".............l....lh...hl..l...h..." + \
          "....l...h.......l...h...l....lh...h" + \
          "l..l.......h...l...h..............." + \
          "l....lh...hl..l...h...l............" + \
          ".......h...l....lh...hl..l...h...l." + \
          "..h...l...h...........l....lh...hl." + \
          ".l...h.......l.......h...l.......l." + \
          "...lh...hl..l...h...l.......h......" + \
          ".....l...l....lh...hl..l...h...l..." + \
          "h...l...h...l...h...l....lh...hl..l" + \
          "...h...l...............h...l...l..." + \
          ".lh...hl..l...h...l...h...l...h...." + \
          ".......l....lh...hl..l...h...l....." + \
          "..h...........l...l....lh...hl..l.." + \
          ".....h.......h...l...........l....l" + \
          "h...hl..l...h.......l...h.........." + \
          ".....l....lh...hl..l.......h...l..." + \
          "h...............l....lh...hl..l...h" + \
          "...........l...h...l.......l....lh." + \
          "..hl..l...h...........l...h...l...h" + \
          "...l....lh...hl..l...h.......l...h." + \
          "..........l...l....lh...hl..l...h.." + \
          ".....l.......h...l...h...l....lh..."

pattern = {'signal': [{'name': 'string1', 'wave': string1},
                      {'name': 'string2', 'wave': string2}],
           'foot': {'tock': 1}}

def convert_chunk(chunk):
    bit = 1
    bitstream = []
    for c in chunk:
        if c == 'h':
            bit = 1
        elif c == 'l':
            bit = 0
        bitstream.append(bit)
    return chr(int(''.join([str(i) for i in bitstream[0::4]]), 2))
    
#draw_wavedrom(pattern)
print(string1[:50])
string1 = string1[50:]

print(string2[:50])
string2 = string2[50:]

ans = ""
while string1:
    '''
    chunk1 = string1[:32]
    
    print(convert_chunk(chunk1))
    string1 = string1[46:]
    '''
    chunk2 = string2[:32]
    print(convert_chunk(chunk2), end='')
    string2 = string2[46:]
    
