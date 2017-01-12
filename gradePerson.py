import sys
import operator
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
class GradePerson():
	"""
	first order by grade(field:2), then lastName(field:0), then firstName(field:1)
	"""
	def compOrd(self,pa,pb)	:
		if pa[2] > pb[2]: #desc gt
			return -1
		if pa[2] < pb[2]: #desc lt
			return 1
		if pa[0] > pb[0]: #asc gt
			return 1
		if pa[0] < pb[0]: #asc lt
			return -1	
		if pa[1] > pb[1]: #asc gt
			return 1
		if pa[1] < pb[1]: #asc lt
			return -1
		else:	#exact equality
			return 0

	"""
	file handling
	"""
	def grading(self):
		f = None
		infile = "names.txt"
		try:
			if len(sys.argv)==2 :
				filename = sys.argv[1] 
				print sys.argv[1]
				f = open(sys.argv[1], 'r')
			else:
				logging.debug("opeing %s hardcoded." % infile)
				f = open(infile, 'r')
		except IOError:
			logging.error("file %s not found, exiting program." % infile)
			f.close()

			sys.exit(0)
		try:
			arr = []
			for line in f:
				logging.debug(line)
				person = line.strip('\n').split(', ')
				person[2] = int(person[2])
				arr.append(person)
			logging.debug(arr)
			resList = sorted(arr, cmp=self.compOrd)

			fout = open("names-graded.txt", 'w')
			for person in resList:
				strout = "%s %s %s\n" % (person[0], person[1], str(person[2]))
				print  "%s %s %s\n" % (person[0], person[1], str(person[2]))
				fout.write(strout)
			fout.close()
			print "Finished: created names-graded.txt"
		except IndexError:
			logging.error("input file format error, check input formatting.")
			sys.exit(0)
		except ValueError:
			logging.error("cannot parse grade supplied in input file.")
			sys.exit(0)
		except IOError:
			logging.error("problem writing to file. check write-protected or other program using it.")
			sys.exit(0)

if __name__ == '__main__':
	gp = GradePerson()
	gp.grading()
