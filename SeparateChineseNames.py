#!/usr/bin/python

import sys
import AddressBook

def is_cjk_char(x):
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return 1

    # Fullwidth Latin Characters
    if x >= 0xff00 and x <= 0xffef:
        return 1

    # CJK Unified Ideographs &
    # CJK Unified Ideographs Extension A
    if x >= 0x4e00 and x <= 0x9fbb:
        return 1
    # CJK Compatibility Ideographs
    if x >= 0xf900 and x <= 0xfad9:
        return 1

    # CJK Unified Ideographs Extension B
    if x >= 0x20000 and x <= 0x2a6d6:
        return 1

    # CJK Compatibility Supplement
    if x >= 0x2f8000 and x <= 0x2fa1d:
        return 1

    return 0

def all_cjk_char(line):
    # print "@: %s" % (line.encode("utf-8")) 

    for ch in line:
       if not is_cjk_char(ord(ch)):
           return 0

    return 1

def separate_name(person):
	first_name = person.valueForProperty_(AddressBook.kABFirstNameProperty)
	last_name = person.valueForProperty_(AddressBook.kABLastNameProperty)
	
	if first_name and not last_name and len(first_name) > 1 and len(first_name) < 4 and all_cjk_char(first_name):
		person.setValue_forProperty_(first_name[1:], AddressBook.kABFirstNameProperty)
		person.setValue_forProperty_(first_name[0], AddressBook.kABLastNameProperty)
		
		return (first_name, first_name[1:], first_name[0])
		
	return None

ab = AddressBook.ABAddressBook.sharedAddressBook()

for person in ab.people():
	result = separate_name(person)
	if result:
		print "%s => %s %s" % result	

print "Done."
ab.save()

