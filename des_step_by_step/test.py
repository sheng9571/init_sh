# -*- coding: utf-8 -*-

from des import des

key = '1'
message = '0123456789ABCDEF'


des = des(key, message)
des.encrypt()
