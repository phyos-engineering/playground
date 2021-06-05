# !/usr/bin/env python
# title           :Human.py
# description     :Enter Description Here
# author          :Sebastian Maldonado
# date            :6/3/21
# version         :0.0
# usage           :SEE README.md
# notes           :Enter Notes Here
# python_version  :3.6.8
# conda_version   :4.8.3
# =================================================================================================================

"""
Add arbitrary class methods and push commits for review via pull requests to practice workflow.
"""


class Human:
	# Constructor
	def __init__(self, name, gender,age):
		self.name = name
		self.gender = gender
		self.age = age

	#Grow the human
	def grow(self, age):
		self.age = self.age + age
