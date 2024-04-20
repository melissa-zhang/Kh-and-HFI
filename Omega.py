#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

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

# generators of the [Id] bimodule
# these are ragged arrays
FULLMOON = [I0, [I1, I0]]
NEWMOON = [I1, [I0, I1]]
ID_GEN = [FULLMOON, NEWMOON]


# generators of the [AZAZ] bimodule
AZAZ_GEN = []

# note that [I0,[a,b]] is a gen if 
# alg element a has I0 as left idem
# because this is actually [a^*,b]
def populate_AZAZ_GEN():
    for a in I0_LEFT_IDEM:
        for b in I1_LEFT_IDEM:
            AZAZ_GEN.append([I0,[a,b]])
    for a in I1_LEFT_IDEM:
        for b in I0_LEFT_IDEM:
            AZAZ_GEN.append([I1,[a,b]])

            

# records all arrows for AZAZ's delta_1
DELTA_1 = [
    # when spit out 1 as alg element (no left border)
    [[I0, [R12, I1 ]],  [I0, [I1,  R12]]],
    [[I1, [R23, I0 ]],  [I1, [I0,  R23]]],
    [[I0, [R34, I1 ]],  [I0, [I1,  R34]]],
    [[I0, [R12, R23]],  [I0, [I1,  R13]]],
    [[I0, [R12, R24]],  [I0, [I1,  R14]]],
    [[I1, [R23, R34]],  [I1, [I0,  R24]]],
    [[I1, [R13, I1 ]],  [I1, [R23, R12]]],
    [[I0, [R24, I0 ]],  [I0, [R34, R23]]],
    [[I0, [R14, I1 ]],  [I0, [I1,  R14]]],
    [[I0, [R14, I1 ]],  [I0, [R24, R12]]], # 2 arrows
    [[I1, [R13, R23]],  [I1, [R23, R13]]],
    [[I0, [R24, R34]],  [I0, [R34, R24]]],
    [[I0, [R14, R24]],  [I0, [R24, R14]]],
    [[I1, [R13, R24]],  [I1, [R23, R14]]],
    [[I0, [R14, R23]],  [I0, [R24, R13]]]
]

# when spit out a non idem coeff
def populate_DELTA_1():
    for a in [I1, R23, R24]:
        DELTA_1.append([[I0, [R12, a]], [R12, [I0,a]]])
        #
        DELTA_1.append([[I1, [R13, a]], [R13, [I0,a]]])
        DELTA_1.append([[I1, [R13, a]], [R23, [R12,a]]])
        #
        DELTA_1.append([[I0, [R14, a]], [R14, [I0,a]]])
        DELTA_1.append([[I0, [R14, a]], [R24, [R12,a]]])
        DELTA_1.append([[I0, [R14, a]], [R34, [R34,a]]])
        #
        DELTA_1.append([[I0, [R34, a]], [R34, [I0,a]]])
        ##
    for a in [I0, R12, R13, R14, R34]:
        DELTA_1.append([[I1, [R23, a]], [R23, [I1,a]]])
        #
        DELTA_1.append([[I0, [R24, a]], [R24, [I1,a]]])
        DELTA_1.append([[I0, [R24, a]], [R34, [R23,a]]])
        
# len(DELTA_1): 15 + 3*7 + 5*3 = 15+21+15 = 51.
    


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

def id_str(gen):
    if (np.array_equal(gen, ID_GEN[0])):
        return "I1*xI0"
    elif (np.array_equal(gen, ID_GEN[1])):
        return "I0*xI1"
    else:
        return "Error in ID_str."
    
# Entirely formal
# Doesn't check if gen is a real AZAZ_GEN
def azaz_gen_str(gen):
    name = "(" + alg_str(gen[0]) + " | " + alg_str(gen[1]) +")"
    return name

# prints any single-term element of AZAZ, with coefficient
# elt = [coeff, [gen]]
def azaz_str(elt):
    name = alg_str(elt[0]) + "*" + azaz_gen_str(elt[1])
    return name

populate_AZAZ_GEN()
populate_DELTA_1()
print("Initialized.")



# In[2]:


###########################
# STRUCTURE FUNCTIONS #####
###########################

# and checking dOmega_1, dOmega_2 = 0


# a_i in torus algebra
# input two alg elements (ints)
# output alg element (int) or 0
def mu(a_1, a_2):
    for i in range(len(MU)):
        if (a_1==MU[i][0] and a_2==MU[i][1]):
            return MU[i][2]
    return 0




# differential for the [Id] bimodule
# returns single-entry array of AZAZ elt
def partial_2(id_gen, a_1):
    if(np.array_equiv(id_gen, NEWMOON)):
        if (a_1==R23):
            return [[a_1, FULLMOON[1]]]
        if (a_1==R24):
            return [[a_1, NEWMOON[1]]]
    if(np.array_equiv(id_gen, FULLMOON)):
        if (a_1==R13):
            return [[a_1, FULLMOON[1]]]
        if (a_1 in [R12, R34, R14]):
            return [[a_1, NEWMOON[1]]]
    return []
                    
                    
    


# input is azaz elt, but with just a 1 or idempotent coeff
# image is a list of coeff'd gens
def delta_1(elt):
    image = []
    for arrow in DELTA_1:
        # compare without the coefficient
        if(np.array_equiv(arrow[0][1], elt[1])):
            image.append(arrow[1])
    return image




# delta_2 of AZAZ
# given by RIGHT MULTIPLICATION!
# input is azaz gen (with idempotent coeff!)
# output array of azaz_gen (only 0 or 1 elements possible)
def delta_2(azaz_gen, a_1):
    image = []
    if a_1 in KER:
        right = mu(azaz_gen[1][1], a_1)
        if (right != 0):
            # left idempotent doesn't change
            left = azaz_gen[0]
            # left module element doesn't change either
            image.append([left, [azaz_gen[1][0] ,right]])
    return image


# compare elements of structure of azaz elt
# elts are of the form [coeff, [left,right]]
# returns True (same) or False (different)
def azaz_compare(elt1, elt2):
    if (elt1[0] != elt2[0]): return False
    for i in range(2):
        if (elt1[1][i] != elt2[1][i]): return False
    return True


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
    


# takes in element of [Id]
# outputs coefficient and element of [AZAZ]
# a single element array of elts
def Omega_1(id_gen):
    # yes, this is silly but was the point
    # of this whole exercise
    return [id_gen]


# takes in element of [Id] and an alg element
# outputs array of [coefficient and element] of [AZAZ]
def Omega_2(id_gen, a_1):
    output = []
    # first check that we even have left idempotent 
    # to the left of the alg element
    if (id_gen[1][1]==I0):  
        if (a_1 == R12 or a_1 == R34):
            output.append([I0, [a_1, I1]])
        elif (a_1 == R13):
            output.append([I0, [R12, R23]])
            output.append([R12, [R23, I0]])
        elif (a_1 == R14):
            output.append([I0, [R12, R24]])
            output.append([R12, [R23, R34]])
            output.append([R13, [R34, I1]])
    if (id_gen[1][1]==I1):
        if (a_1 == R23):
            output.append([I1, [a_1, I0]])
        elif (a_1 == R24):
            output.append([I1, [R23, R34]])
            output.append([R23, [R34, I1]])    
    # if there is no output, e.g. put in idempotent, then return nothing.
    return output


# Omega_3 switches the endpoints of the chords
# so that a "crossing" is introduced
# input: id generator, plus 2 alg elts
# output: array of azaz elts
# actually really need idempotents on this one to capture the crossing
def Omega_3(id_gen, a_1, a_2):
    image = []
       
    if (id_gen[1][1] == I0):
        if (a_1 == R13):
            if (a_2 == R12): 
                image.append([R12, [R13, I1]])
            elif (a_2 == R13):
                image.append([R12, [R13, R23]])
            elif (a_2 == R14):
                image.append([R12, [R13, R24]])
        elif (a_1 == R14):
            if (a_2 == R23):
                image.append([R13, [R24, I0]])
            elif (a_2 == R24):
                image.append([R13, [R24, R34]])
        elif (a_1 == R34):
            if (a_2 == R23):
                image.append([I0, [R24, I0]])
            elif (a_2 == R24):
                image.append([I0, [R24, R34]])
    elif (id_gen[1][1] == I1):
        if (a_1 == R23):
            if (a_2 == R12):
                image.append([I1, [R13, I1]])
            elif (a_2 == R13):
                image.append([I1, [R13, R23]])
            elif (a_2 == R14):
                image.append([I1, [R13, R24]])
        if (a_1 == R24):
            if (a_2 == R23):
                image.append([R23, [R24, I0]])
            elif (a_2 == R24):
                image.append([R23, [R24, R34]])
                
    return image

    


# In[3]:


#################################################
# CALCULATIONS for checking dOmega_k = 0 ########
#################################################

# dOmega_2 on a possible input
def dOmega_2(id_elt, a_1):
    image = []
    
    # partial_2 -> Omega_1
    for x in partial_2(id_elt, a_1):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in Omega_1([left_idem, x[1]]):
            coeff = mu(x[0],y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])
            
    # Omega_1 -> delta_2
    for x in Omega_1(id_elt):
        # x should be same as id_elt
        for y in delta_2(x, a_1):
            coeff = mu(x[0],y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])
            
    # Omega_2 -> delta_1
    for x in Omega_2(id_elt, a_1):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in delta_1([left_idem, x[1]]):
            coeff = mu(x[0],y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])
    
    return image



# dOmega_3 on a possible input
# input: id elt, 2 alg in aug ideal
def dOmega_3(id_elt, a_1, a_2):
    image = []
    
    # partial_2 -> Omega_2
    for x in partial_2(id_elt, a_1):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in Omega_2([left_idem, x[1]], a_2):
            coeff = mu(x[0],y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])
   
    
    # Omega_2 -> delta_2
    for x in Omega_2(id_elt, a_1):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in delta_2([left_idem, x[1]], a_2):
            coeff = mu(x[0],y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])
    
    
    # mu -> Omega_2
    prod = mu(a_1, a_2)
    if (prod != 0):
        for x in Omega_2(id_elt, prod):
            image.append(x)
            

    # Omega_3 -> delta_1
    for x in Omega_3(id_elt, a_1, a_2):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in delta_1([left_idem, x[1]]): 
            coeff = mu(x[0], y[0])
            if (coeff != 0):
                image.append([coeff, y[1]])

        
    # return
    return image


# the first four terms of dOmega_4 for now
# input: id_gen and three alg elts
# output: array of azaz elts
def dOmega_4(id_elt, a_1, a_2, a_3):
    image = []
    
    # partial_2 -> Omega_3
    for x in partial_2(id_elt, a_1):
        for y in Omega_3(x[1], a_2, a_3):
            image.append(mu(x[0], y[0]), y[1])
            
    # Omega_3 -> delta_2
    for x in Omega_3(id_elt, a_1, a_2):
        left_idem = complement(alg_right_idem(x[1][0]))
        for y in delta_2([left_idem, x[1]], a_3):
            image.append(mu(x[0], y[0]), y[1])
            
    # (mu, 1) -> Omega_3
    # there's only one target per source for Omega_3
    # actually
    for x in Omega_3(id_elt, mu(a_1, a_2), a_3):
        image.append(x)
    for y in Omega_3(id_elt, a_1, mu(a_2, a_3)):
        image.append(y)
        
    return image


                              


# In[6]:


#####################################
# TEST FUNCTIONS ####################
#####################################


def test_dOmega_2():
    for x in ID_GEN:
        for a_1 in KER:
            image = dOmega_2(x, a_1)
            if (len(image)>0):
                print("dOmega_2 of (" + id_str(x) + "," + alg_str(a_1) + ") is:")
                for im in image:
                    print(azaz_str(im))
                                                         

def test_dOmega_3():
    for x in ID_GEN:
        for a_1 in KER:
            for a_2 in KER:
                image = dOmega_3(x, a_1, a_2)
                if (len(image)>0):
                    print("dOmega_3 of (" + id_str(x) + "," + alg_str(a_1) + "," 
                            + alg_str(a_2) + ") is:")
                    for im in image:
                        print(azaz_str(im))
                        

def test_dOmega_4():
    for x in ID_GEN:
        for a_1 in KER:
            for a_2 in KER:
                for a_3 in KER: 
                    image = dOmega_3(x, a_1, a_2)
                    if (len(image)>0):
                        print("dOmega_4 of (" + id_str(x) + "," + alg_str(a_1) + ","
                                + alg_str(a_2) + "," + alg_str(a_3) + ") is:")
                        for im in image:
                            print(azaz_str(im))
                            
                            
                            

                            


# In[ ]:





# In[ ]:





# In[ ]:



