import test #importing test file

A = test.finalOutput(); #A is the array returned by the test file (song, genre, artist)

def runningConverter():
	with open("dataToWebDev/templates/dataSets/outputFromPyFile.html", "w") as my_file: #opening file and writing data to the .html file
	  my_file.write("<html><body><div>")
	  my_file.write(' '.join(map(str, A))) #mappoing Array A to the string
	  my_file.write("</div></body></html>")
