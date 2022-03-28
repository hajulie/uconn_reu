import b4_main_tree
from b4_main_tree import build_db

"""
Following test is an example of a test on a random dataset 
"""

if __name__ == '__main__':
    import random

    # n = 100
    branching_factor = 2
    fpr = 0.0001 
    temp_l = 2

    try_nums = [2] #tries multiple size dbs 

    for n in try_nums: 
        print('\n--- size of database = %i ---' %n )
        try_data = ([[random.getrandbits(1) for i in range(1024)] for i in range(n)])

        t, data = build_db(branching_factor, fpr, try_data, l = temp_l) # builds the database 

        print("tree built")
        print("sub trees:\n", t.subtrees )
        
        try_search = random.randint(0,n-1)
        attempt = try_data[try_search]
        
        print("Search for Iris %i, No noise" % try_search) # searching with no noise 
        s = t.search(attempt)
        
        print("All nodes visited:", s[0])
        print("Matched leaf nodes:", s[1])
        print("Matched Irises:", s[2])