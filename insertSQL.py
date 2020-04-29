"""
Some conditions must be met for this script to work, They are as follows:

1) You must have a file containing the SQL insert queries you want populated.

e.g 
if you want to populate 2 Queries then you should have a file containing:

INSERT VALUES INTO STAFF();
INSERT VALUES INTO STAFF();

2) You must have a file that has the data that you want to insert into the
	 empty INSERT queries, and each value must be seperated by a space ' '.
	 The end of the line signifies the start of a new INSERT query

e.g 
if you want to insert 2 lines of data into the 2 queries you should have
a file containing this:

Dan Smith 23 185
Kate Casey 32 167

The result of the two examples will be:

INSERT VALUES INTO STAFF('Dan', 'Smith', '23', '185');
INSERT VALUES INTO STAFF('Kate', 'Casey', '32', '167');
"""

import re
def insertSQL(sql, data, newFile, lines):
	f1 = open(data)
	f2 = open(sql)
	f3 = open(newFile, 'w+')

	for i in range(lines):
		line = f1.readline()
		line = line.split()

		for i in range(len(line)):
			line[i] = '\'' + line[i] + '\''

		template = f2.readline()
		values = ', '.join(line)
		newLine = re.sub('\(\)', '(' + values + ')', template)
		f3.write(newLine)

	f1.close()
	f2.close()
	f3.close()

fin = False
while fin == False:
	try:
		sql = input('\nFile containing empty INSERT statements: ')
		data = input('File containing data to be inserted: ')
		newFile = input('New file: ')
		lines = int(input('Lines: '))
		insertSQL(sql, data, newFile, lines)

	except FileNotFoundError:
		print('\nCannot find file with that filename.', sep='')
		print('Please enter a valid filename.')
	except ValueError:
		print('\nPlease enter a valid whole number.\n')

	while True:
		yesOrNo = input('\nWould you like to do it again? Y/N: ')

		if yesOrNo == 'Y' or yesOrNo == 'y':
			break

		elif yesOrNo == 'N' or yesOrNo == 'n':
			fin = True
			break

		else:
			print('\nPlease enter Y or N')
