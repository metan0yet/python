#!root/bin

#lists

#25
#0
#21
#145
#3.5355
#0.5
#center
#31.82  m^2
#-5
#A7EBO
questions = ['[1] calculate this : (5 * 5)','[2] solve it [5*5+12/3-5/12-2] ','[3] What is the sum of all dots in a regular die?','[4] Solve it [(5 * 9) + 10% * 1000]','[5] If you have a triangle inside a circle \n its diameter equal 5 meters \n and the angles between the side of the triangle and the diameter is 45 degrees \n Calculate the length of the side of the triangle','[6] Calculate this [sin(30)^2 * cos(60)^2]','[7] The center of gravity of a plate in the form of a regular triangle is located in:','[8] Hexagon shape with a side length equal to 3.5 meters whose area is equal to:','[9] calculate this [196/14+14-28-5]','[10] how many supporter in ultras ahlawy']

   #logo

print('''
	***********  Python 3.7.3 Used   **************
	*                                             *
	* math_challenge is an open source game       *
	* that coded by hossam hamdy @MetaNoYet       *
	* this challenge in (Beta) mode               *
	* so if you have any notice tell me           *
	* ho55amhamdy.cyber@gmail.com                 *
	* i will be so happy to tell me your opinion  *
	* Thak you For Using it                       *
	*                                             *
	*   -Hossam Hamdy                             *
	*                                             *
	**************   Have Fun ! <3  *************** ''')

logo = '''
    \t|--------------MetaNoYet---------------|
	\t|mmmmmmmmmmmm aaaaaaa tttttttttt hh  hh|
	\t|mmmmmmmmmmmm aaaaaaa tttttttttt hh  hh|
	\t|mm   mm   mm aa   aa     tt     hhhhhh|
	\t|mm   mm   mm aaaaaaa     tt     hhhhhh|
	\t|mm   mm   mm aaaaaaa     tt     hh  hh|
	\t|mm   mm   mm aa   aa     tt     hh  hh|
	\t|mm   mm   mm aa   aa     tt     hh  hh|
	\t|--------------------------------------|
	\t\t\tver 0.1 beta	'''


#Variable
user_name = str(input('\nEnter Your Name : '))
print(logo)
certificate= f'''
 *______________________________________________
 |                                                                       
 |Certificate From MetaNoYet To : {user_name.title()}              
 |______________________________________________
\n\n
 *----------------------*
 |----Congratulation----|
 *----------------------*\n\n
 Thank You {user_name.title()}\n
 To Complet My Math  Challenge\n                 	
 That Is Mean You Are Great With Math !\n	 
 I Think You Will Have A Good IT Job In The Feuture\n 	
 So If You Want To Practise Your Mathmatic Skills\n
 Contact Me !\n	
 I'm Online Most Of My Day,\n
 I Will Be Happy To Help You <3\n
 Have A Good Day Mr : {user_name.title()}\n
 -MetaNoYet\n
 ************************************************
'''

msg_1 = '''\n\t\t
*----------------------*
|Good You Are Perfect !|
*----------------------*\n\n'''                 


msg_0 = '''\n\t\t
*---------------------*
|Sorry , That's Wrong |
*---------------------*\n\n'''


                                 #method

#Q1----------------
print(questions[0])
print('''\n
[1]20\t\t[2]40
[3]25\t\t[4]50 
''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 3:
	print(msg_1)
else:
	print(msg_0)
#-----------------
#Q2---------------
print(questions[1])
print('''\n
[1]10\t\t[2]0
[3]-1\t\t[4]9
			  ''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 2:
	print(msg_1)
else:
	print(msg_0)
#--------------------------
#Q3
print(questions[2])
print('''\n
[1]22\t\t[2]21
[3]23\t\t[4]14
	''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 2:
	print(msg_1)
else:
	print(msg_0)
#-------------------------
#Q4
print(questions[3])
print('''\n
[1]144\t\t[2]211
[3]169\t\t[4]145
			  ''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 4:
	print(msg_1)
else:
	print(msg_0)
#----------------------
#----------------------
#Q5
print(questions[4])
print('''\n
[1]3.5355\t\t[2]3.5654
[3]3.5312\t\t[4]4
	''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 1:
	print(msg_1)
else:
	print(msg_0)
#------------------------
#Q6
print(questions[5])
print('''\n
[1]0.25\t\t[2]0
[3]0001\t\t[4]0.5
					''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 4:
	print(msg_1)
else:
	rint(msg_0)
#------------------------------
#Q7
print(questions[6])
print('''\n
[1] inside\t\t[2]center
[3]outside\t\t[4]zero
	''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 2:
	print(msg_1)
else:
	print(msg_0)
#------------------------------
#Q8
print(questions[7])
print('''\n
[1]30.50 m^2\t\t[2]30  m^2
[3]31.82 m^2\t\t[4]114 m^2
				''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 3:
	print(msg_1)
else:
	print(msg_0)
#----------------------------
#Q9
print(questions[8])
print('''\n
[1]-1\t\t[2]-5
[3]10\t\t[4]12
	''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 2:
	print(msg_1)
else:
	print(msg_0)
#---------------------------------------------------------
#Q10
print(questions[9])
print('''\n
[1]10000000\t\t[2]a7ebo4
[3]14000000\t\t[4]5
					''')
entred_answer = int(input("The Correct Answer Is : "))
if entred_answer == 2:
	print(msg_1)
else:
	print(msg_0)
#-----------------------------------------------------------
print(f"""
Hi Mr : {user_name} <3\n\nPlease wait a moment while the certificate is prepared\n\nThank Your For Competing Our Math Challenge\n\nHave Fun \n\n""")
print(f"\n\n\n" + certificate +"\n\n\n\n")
#Coded By Hossam Hamdy