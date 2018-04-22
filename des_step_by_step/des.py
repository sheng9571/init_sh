# -*- coding: utf-8 -*-

class des:

	key = None
	message = None
	iv = None
	mode = None
	debug = True

	def __init__(self, key, message, iv='', mode='ECB'):
		self.key = key
		self.message = message
		self.iv = iv
		self.mode = mode

	# string to hex
	def str_to_hex(self, aim):
		res = ''
		for i in aim:
			res += str(hex(ord(i))).replace('0x', '')

		return res

	# hex to string
	def hex_to_str(self, aim):
		res = ''
		for i in range(0, len(aim), 2):
			res += chr(int(aim[i] + aim[i + 1], 16))

		return res

	# hex to binary
	def hex_to_bin(self, aim):
		res = ''
		for i in range(0, len(aim), 2):
			res += str(bin(int(aim[i] + aim[i + 1], 16))).replace('0b', '').zfill(8)

		return res

	# bin to hex
	def bin_to_hex(self, aim):
		res = ''
		for i in range(0, len(aim), 8):
			tmp = ''
			for j in range(i, i + 8): tmp += aim[j]
			res += str(hex(int(tmp, 2))).replace('0x', '')

		return res


	# 1. confusion, initial permutation table
	def confusion(self, plaintext):
		if (self.debug):
			print '[*] 1. confusion, initial permutation table'

		# pre-defined
		init_p_table = ['58', '50', '42', '34', '26', '18', '10', '2', '60', '52', '44', '36', '28', '20', '12', '4', '62', '54', '46', '38', '30', '22', '14', '6',' 64', '56', '48', '40', '32', '24', '16', '8',	'57', '49', '41', '33', '25', '17', '9', '1', '59', '51', '43', '35', '27', '19', '11', '3','61', '53', '45', '37', '29', '21', '13', '5', '63', '55', '47', '39', '31', '23', '15', '7']

		permutated_m = ''
		for index in init_p_table:
			permutated_m += plaintext[int(index) - 1]

		return permutated_m


	def encrypt(self):
		if (self.debug):
			print '[*] original plaintext: %s' % self.message
			print '[+] convert it to binary ...'


		# convert plaintext to binary
		self.message = self.hex_to_bin(self.str_to_hex(self.message))

		if (self.debug):
			print '[*] plaintext in binary: %s' % self.message

		p_m = self.confusion(self.message)
		print p_m
