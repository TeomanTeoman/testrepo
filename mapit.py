#! python3
#this program search a location in google maps
import webbrowser, sys, re

print("Tell me the location you would like the search.")
place = input()
lplace = place.split()
pplace = "+".join(lplace)
webbrowser.open("https://www.google.com/maps/search/"+ pplace)
