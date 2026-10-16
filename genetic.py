import ctypes

C_library = ctypes.CDLL("libgenetic.so")

encode = C_library.encoding
encode.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]
encode.restype = ctypes.c_char_p

decode = C_library.decoding
decode.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
decode.restype = ctypes.c_double

selection = C_library.selection
selection.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
selection.restype = ctypes.POINTER(ctypes.c_double)

cross = C_library.crossover
cross.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
cross.restype = ctypes.POINTER(ctypes.c_char_p)

mut = C_library.mutation
mut.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
mut.restype = ctypes.c_char_p

fit = C_library.fitness
fit.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]
fit.restype = ctypes.c_double

def encoding(a,b,pres,num):
    return encode(a,b,pres, num).decode('utf-8')

def decoding(a,b,precision, st):
    st = st.encode('utf-8')
    return decode(a,b,precision,st)

def select(a, b, c, length, array):
    double_arr = ctypes.c_double * len(array)
    double_arr = double_arr(*array) # * unpacks the array
    ptr = selection(a,b,c,length, double_arr)
    arr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double * (length + 1))).contents
    return list(arr)

def crossover(l, pos, c1, c2):
    c1 = c1.encode('utf-8')
    c2 = c2.encode('utf-8')
    ptr = cross(l, pos, c1, c2)
    arr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_char_p * 2)).contents
    return [ a.decode('ascii') for a in list(arr)]

def mutation(length, position, ch, positions):
    pos_arr = ctypes.c_int * len(positions)
    pos_arr = pos_arr(*positions)
    ch = ch.encode('utf-8')
    return mut(length, position, ch, pos_arr).decode('ascii') 

