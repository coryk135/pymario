## Program to read in a word and print it out from console
		.data
str1:
		"
str2:
		"
str3:
		"
str4:
		"
String:
	
		
main:
		addiu $sp, $sp, -24	#increments the pc
		sw $ra, 20($sp)			#saves the return address up 20 bytes
		
		jal wherever you wanna go
		
		lw $ra, 20($sp)			#loads the sp into the return address
		addiu $sp, $sp, 24		#adds 24 to restore the sp