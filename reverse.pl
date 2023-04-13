#!/usr/bin/perl
print "Enter some lines, then press Ctrl-D to excit:\n"; 
# or maybe Ctrl-Z 
@lines = <STDIN>; 
@reverse_lines = reverse @lines; 
print ("your reverse is\n @reverse_lines");
