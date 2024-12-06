# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrence	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group	 


import re

pattern = r"[A-Z]+yclone"
text = '''Upper level cyclones can exist without the presence of a surface low, 
and can pinch off from the base of the tropical upper tropospheric trough during the summer months in the Northern Hemisphere. 
Cyclones have Dyclone also been seen Pyclone on extraterrestrial planets, such as Mars, Jupiter, and Neptune.[7][8] Cyclogenesis is the process 
of cyclone formation and intensification.[9] Extratropical cyclones begin as waves in large regions of enhanced mid-latitude 
temperature contrasts called baroclinic zones. These zones contract and Tyclone form weather fronts as the cyclonic circulation closes 
and intensifies. Later in Zyclone their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and become 
cold core systems. A cyclone's track is guided over the course of its 2 to 6 day life cycle by the steering flow of the subtropical 
jet stream.'''

# match = re.search(pattern, text) # it is use for first occurence only
# print(match)
matches = re.finditer(pattern, text) 
for match in matches:
    print(text[match.span()[0]:match.span()[1]])

# https://regexr.com/