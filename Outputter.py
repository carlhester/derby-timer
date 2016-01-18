
class Outputter:
	def writeToTemplate(self, template, data, saveas):
		f = open(str(saveas) + ".html" , 'w')
		f.write(data)
		f.close()

