#!/usr/bin/env python
# coding: utf-8

# In[6]:


###########################
# CONSTANTS ###############
###########################

# Torus algebra elements stored as single integers
# 0,1 reserved for actual 0,1
# if start at 1, int is the end
# if start at 2 or 3, int is sum of start and end
# idempotents are 10 and 11 
I0 = 10
I1 = 11
R12 = 2
R13 = 3
R14 = 4
R23 = 5
R24 = 6
R34 = 7

# whole algebra as list, except 1
ALG = [I0, I1, R12, R13, R14, R23, R24, R34]

# augmentation ideal
KER = [R12, R13, R14, R23, R24, R34]

# classify algebra elements by left and right idempotents
I0_LEFT_IDEM = [I0, R12, R13, R14, R34]
I1_LEFT_IDEM = [I1, R23, R24]
I0_RIGHT_IDEM = [I0, R13, R23]
I1_RIGHT_IDEM = [I1, R12, R14, R24, R34]

# Torus algebra names stored in array
STR_ALG = [
    ["I0", 10],
    ["I1", 11],
    ["R12", 2],
    ["R13", 3],
    ["R14", 4],
    ["R23", 5],
    ["R24", 6],
    ["R34", 7],
    ["0", 0],
    ["1", 1]
]

# Torus algebra multiplication stored as array
# Only nonzero results recorded
# Pattern: [A,B,AB]
MU = [
    # identity (times 1)
    [1, 1, 1],
    [1, I0, I0],
    [1, I1, I1],
    [1, R12, R12],
    [1, R13, R13],
    [1, R14, R14],
    [1, R23, R23],
    [1, R24, R24],
    [1, R34, R34],
    [I0, 1, I0],
    [I1, 1, I1],
    [R12, 1, R12],
    [R13, 1, R13],
    [R14, 1, R14],
    [R23, 1, R23],
    [R24, 1, R24],
    [R34, 1, R34], 
    # idempotents
    [I0, I0, I0],
    [I1, I1, I1],
    # left idem 
    [I0, R12, R12],
    [I0, R13, R13],
    [I0, R14, R14],
    [I0, R34, R34],
    [I1, R23, R23],
    [I1, R24, R24],
    # right idem 
    [R12, I1, R12],
    [R13, I0, R13],
    [R14, I1, R14],
    [R34, I1, R34],
    [R23, I0, R23],
    [R24, I1, R24],
    # concatenation
    [R12, R23, R13],
    [R12, R24, R14],
    [R13, R34, R14],
    [R23, R34, R24]
]

    


###########################
# TO STRING ###############
###########################


# algebra element to string
# returns string assoc to alg element
# or 0
# alg elts are recorded as ints (primitive)
def alg_str(a):
    for i in range(len(STR_ALG)):
        if (a==STR_ALG[i][1]):
            return STR_ALG[i][0]
    return "Error in alg_str."


# In[7]:



###########################
# STRUCTURE FUNCTIONS #####
###########################


# a_i in torus algebra
# input two alg elements (ints)
# output alg element (int) or 0
def mu(a_1, a_2):
    for i in range(len(MU)):
        if (a_1==MU[i][0] and a_2==MU[i][1]):
            return MU[i][2]
    return 0


# decomposes algebra element into elementary strings
def decompose_alg(a):
    if (a == R13):
        return [R12, R23]
    elif (a == R24):
        return [R23, R34]
    elif (a == R14):
        return [R12, R23, R34]
    return [a]

# returns complement of given idempotent; otherwise nothing
def complement(idem):
    if (idem == I0):
        return I1
    elif (idem == I1):
        return I0
    # otherwise, input was not I0 or I1
    print("Error in complement(idem).")
    
# returns left idem for alg elt a
def alg_left_idem(a):
    if (a in I0_LEFT_IDEM):
        return I0
    elif (a in I1_LEFT_IDEM):
        return I1
    # otherwise, error
    print("Error in alg_left_idem.")

    
# return right idem for alg elt a
def alg_right_idem(a):
    if (a in I1_RIGHT_IDEM):
        return I1
    elif (a in I0_RIGHT_IDEM):
        return I0
    # otherwise, error
    print("Error in alg_right_idem.")   
    


# In[8]:


#################################################
# CANDIDATE h MAPS ##############################
#################################################

# H-double-bar module
# generators: A, B, R, stored as ints
# default return 0 means nothing comes out of a function
A = 1
B = 2


H_GENS = [A,B]
H_GEN_STRS = [
    [A, "A"],
    [B, "B"],
]
def H_gen_str(hgen):
    for arrow in H_GEN_STRS:
        if (hgen==arrow[0]):
            return arrow[1]
    return ""

# m_1 on H
# output is array of images
# there is no m_1 in this case
def H_m1(hgen):
    return []

# m_2 on H
# output is array of images
def H_m2(hgen,a):
    output = []
    if (hgen==B):
        if (a==R12 or a==R34):
            output.append(A)
    return output

# AZ-bar module
AZBAR_GENS = [I0, I1, R12, R13, R14, R23, R24, R34]
# I just copied this from ALG


# H-double-bar box AZ-bar module
# generators: [H-gen,AZbar-gen]
HAZBAR_GENS = [
    [A, I0],
    [A, R13],
    [A, R23],
    [B, I1],
    [B, R12],
    [B, R14],
    [B, R24],
    [B, R34]
]
# To string
HAZBAR_GEN_STRS = [
    [[A, I0], "[A, I0]"],
    [[A, R13], "[A, R13]"],
    [[A, R23], "[A, R23]"],
    [[B, I1],  "[B, I1]"],
    [[B, R12], "[B, R12]"],
    [[B, R14], "[B, R14]"],
    [[B, R24], "[B, R24]"],
    [[B, R34], "[B, R34]"]
]
def hazbar_gen_str(hazgen):
    for arrow in HAZBAR_GEN_STRS:
        if (hazgen==arrow[0]):
            return arrow[1]
    return ""

# m_1 stored as [gen, outgen]
HAZBAR_M_1 = [
    [[B, R12], [A, I0] ],
    [[B, R14], [A, R13]],
    [[B, R24], [A, R23]],
    [[B, R34], [A, I0] ]
]
# callable hazbar_m1
# output: array of hazbar-gens
def hazbar_m1(hazgen):
    output = []
    for arrow in HAZBAR_M_1:
        if (hazgen==arrow[0]): 
            output.append(arrow[1])
    return output

# m_2 stored as [gen, alg, outgen]
HAZBAR_M_2 = [
    [[A, R13], R13, [A, I0] ],
    [[A, R13], R12, [A, R23]],
    [[A, R23], R23, [A, I0] ],
    [[B, R12], R12, [B, I1] ],
    [[B, R14], R12, [B, R24]],
    [[B, R14], R13, [B, R34]],
    [[B, R14], R14, [B, I1] ],
    [[B, R24], R24, [B, I1] ],
    [[B, R24], R23, [B, R34]],
    [[B, R34], R34, [B, I1] ],
]
# callable hazbar_m2
# output: array of hazbar-gens
def hazbar_m2(hazgen, a):
    output = []
    for arrow in HAZBAR_M_2:
        if (hazgen==arrow[0] and a==arrow[1]):
            output.append(arrow[2])
    return output


     
# CANDIDATE h MAPS
     
    
# input: hazbar-gen
# output: single H-gen
def h_1(hazgen):
    if (hazgen==[B,R34]): return B
    elif (hazgen==[B,I1]): return A
    return 0 # means zero map


# input: [hazbar-gen, alg-elt]
# output: single H_gen 
# (yes, not very robust but it's all we need right now)
def h_2(hazgen, a):
    if (hazgen==[A, R13]):
        if (a==R13): return B
        elif (a==R14): return A
    elif (hazgen==[A, R23]):
        if (a==R23): return B
        elif (a==R24): return A
    elif (hazgen==[A, I0] and a==R12): return A
    return 0
    


# In[9]:


#####################################
# TEST FUNCTIONS ####################
#####################################

# test that (dh)_1 = 0
# input: hazgen
# output: array of H-gen
def dh_1(hazgen):
    output = []
    # hazbar_m1 --> h_1
    for x in hazbar_m1(hazgen):
        output.append(h_1(x))
    # h_1 --> H_m1
    for y in H_m1(h_1(hazgen)):
        output.append(y)
    
    # remove 0s
    output = [x for x in output if x != 0]
    return output

# test that (dh)_2 = 0
# input: hazgen, alg elt a
# output: array of H-gens
def dh_2(hazgen, a):
    output = []
    
    # hazbar_m1 --> h_2
    for x in hazbar_m1(hazgen):
        #print("H_m1 --> h_2")
        #print(x)
        output.append(h_2(x,a))
    
    # hazbar_m2 --> h_1
    for x in hazbar_m2(hazgen, a):
        #print("H_m2 --> h_1")
        #print(x)
        output.append(h_1(x))
    
    # h_1 --> H_m2
    img = h_1(hazgen)
    #print("h_1 --> hazbar_m2")
    #print(img)
    for x in H_m2(img, a):
        output.append(x)
    
    # h_2 --> H_m1
    img = h_2(hazgen, a)
    #print("h_2 --> hazbar_m1")
    #print(img)
    for x in H_m1(img):
        output.append(x)
    
    # remove 0s
    output = [x for x in output if x != 0]
    return output

# test that (dh)_3 = 0
# assuming h_i=0 for i \geq 3
# input: hazgen, alg elts a1, a2
# output: array of H-gens
def dh_3(hazgen, a1, a2):
    output = []
    
    # hazbar_m2 --> h_2
    for x in hazbar_m2(hazgen, a1):
        output.append(h_2(x,a2))
    
    # h_2 --> H_m2
    img = h_2(hazgen,a1)
    for x in H_m2(img,a2):
        output.append(x)
    
    # mu --> h_2
    output.append(h_2(hazgen, mu(a1,a2)))
    
    # remove 0s
    output = [x for x in output if x != 0]
    return output
    


# In[10]:


#################################
### TEST FUNCTIONS ##############
#################################


def test_dh_1():
    print("----------------------------")
    print("To show that dh_1 = 0:")
    print("----------------------------")
    for gen in HAZBAR_GENS:
        images = dh_1(gen)
        if (len(images) > 0):
            print("Input: " + hazbar_gen_str(gen))
            print("Output: ")
            for x in images:
                print(H_gen_str(x))

def test_dh_2():
    print("----------------------------")
    print("To show that dh_2 = 0:")
    print("----------------------------")
    for gen in HAZBAR_GENS:
        for a in KER:
            images = dh_2(gen, a)
            if (len(images) > 0):
                print("Input: " + hazbar_gen_str(gen) + ", " + alg_str(a))
                print("Output: ")
                for x in images:
                    print(H_gen_str(x))
    
def test_dh_3():
    print("----------------------------")
    print("To show that dh_3 = 0:")
    print("----------------------------")
    for gen in HAZBAR_GENS:
        for a1 in KER:
            for a2 in KER:
                # print only the cancelling ones
                    images = dh_3(gen, a1, a2)
                    if (len(images) > 0):
                        print("Input: " + hazbar_gen_str(gen) + ", " 
                                + alg_str(a1) + ", " + alg_str(a2))
                        print("Output: ")
                        for x in images:
                            print(H_gen_str(x))

# Run test functions
# Input / Output only printed when
# there are nonzero outputs
                            
test_dh_1()
test_dh_2()
test_dh_3()


# In[ ]:





# In[ ]:



