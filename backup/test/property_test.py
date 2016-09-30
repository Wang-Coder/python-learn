#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height




s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
