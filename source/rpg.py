#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_genertor():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size,20))

def random_password_genertor_ico():
	random_password_genertor_ico = """
	#############################################################
	# PYTHON - Random Password Generetor (RPG) - GH0ST S0FTWARE #
	############################################################# 
	#                         CONTACT                           #
	#############################################################
	#               DEVELOPER : İSMAİL TAŞDELEN                 #
	#          Mail Address : pentestdatabase@gmail.com         #
	#   LINKEDIN : https://www.linkedin.com/in/ismailtasdelen   #
	#              Whatsapp : + 90 534 295 94 31                #
	#############################################################
	"""
	print random_password_genertor_ico

random_password_genertor_ico()
print("Password : " + random_password_genertor())
