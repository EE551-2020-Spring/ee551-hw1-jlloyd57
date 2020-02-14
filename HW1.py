#"""Python Core object Types"""
#Jennifer Lloyd EE551
#"I pledge my honor that I have abided by the Stevens Honor System- Jennifer Lloyd"
# Used stack Overflow for .split(), printing matrix, converting to ascii, .sort() - all suplemental to figure out the solutions
import math

def numbers_and_strings():
   # """ This is to review numbers and strings and basic operations. """
    # Assign a string "EE551" to a variable x
    x = "EE551"
    # Assign a string "Stevens" to a variable y
    y = "Stevens"
    # Repeat variable y 5 times
    z=y*5
    # What is the length of z?
    length = len(z)
    # Concatenate variable y with string " is good"
    m = " is good"
    m = y + m
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = y + " is awesome"    
    print(x, y, z, length, m, n)
    return x, y, z, length, m, n

def lists():
   # """This is to review basic operations with lists. """
	n = "Stevens is awesome"
    # Split variable n on a delimiter space into a list of substrings
	n = 'Stevens is awesome'.split()
#print(n)

    # Get all the items past the first of the third substring
	j = 'Stevens is awesome'.split()[2] #this assigns awesome to j
	j=list(j) #this splits j into a list of the letters of awesome
	j=j[1:] #this only prints the letters after a in awesome#
#print(j)
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
	A= [ ["1","4","5"], ["6", "10", "11"], ["12","17","38"]]
	print(A[0])
	print(A[1])
	print(A[2])

    # Collect the items in the last column of matrix A using list comprehension
	C=[A[0][2],A[1][2],A[2][2]]
    # Collect only the even items of the diagonal of matrix A using list comprehension- code to add  [0,0] [1,1], [2,2] 2D index 
	b= A[0][0], A[1][1], A[2][2]
	for num in b:
    		if int(num) % 2 ==0:
    			print (num)
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value-look up the chart)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
	h = 'stevens'
	for letter in h:
    # Get number that represents letter in ASCII.
		number = ord(letter)
		h=(letter,"=",number)
		print(h)

	print(n, j, num, h, C)
	return n, j, num, h, C

def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f = {"fruit":"apple", "quantity":4, "color":"green"}
    # Get the item in dictionary f that the key "fruit" maps to
    f["fruit"]
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    # actually add 1 to the quantity key to make it 5 
    a = f["quantity"]+1
    #print(p)
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    nested_dict = { 'name': {"first_name": "Grace", "last_name":"Hopper"}, 'jobs': ["scientist", "engineer"], 'age':85}
    print(nested_dict)
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    nested_dict["jobs"].append("programmer")
    #print(nested_dict['jobs'])
    # Get the third job Grace has that you recently added
    p=nested_dict["jobs"][2]
    # Use the sort() function to get sorted keys (age, jobs, name) of nested_dict in alphabetically ascending order
    k = [key for key in nested_dict.keys()]
    k.sort()
    #  print(k)
    print(a, f, p, k)
    return a, f, p, k 
    #i can name these whatever I want that I used- as long as it returns 4 
    
numbers_and_strings()
lists()
dictionaries()


