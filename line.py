import sentence
#import inference
import proof

class Line:
	'''
	A line of a Proof
	'''

	def __init__(self, proof):
		import weakref
		
		# The proof that this line is in as a weak ref
		self._proof = weakref.ref(proof)
		
		# The sentenc at this line
		self._sentence = None
		
		# The inference rule used at this line
		self._inference = None
		
		# A set of weak refs to the lines that support this line
		self._support = set([])
		
		# The current line number. Used for printing
		self._num = None
		
		# Other data that this line may have
		self._data = None

	def __iadd__(self, other):
		'''
		Adds something to this line
		
		Acts as a shortcut to setSentence, addSupport, and setInference
		'''
		if isinstance(other, sentence.Sentence):
			# If we add a sentence, add it as a sentence
			self.setSentence(other)
		elif isinstance(other, Line):
			# If it is a line add it as a support step
			self.addSupport(other)  
		elif isinstance(other, (int, long)):
			# If it is an int or long get that line and add it to the support set
			self.addSupport(self._proof()[other]) 
		elif isinstance(other, proof.Proof):
			# If it is an inference rule or proof
			infs = self._proof()._inferences
			
			# Check to see if it is in the proof's inference dict
			if other.name not in infs:
				# If it is new, add it to the dict
				infs[other.name] = other
				
			# set the inference
			self.setInference(other)
		elif isinstance(other, str):
			# If it is a string, search for it in the proof's inference rules and add that rule to this line
			self.setInference(self._proof()._inferences[other])
		else:
			# Otherwise we don't know how to deal with this
			raise TypeError('other is a ' + str(type(other)))
		return self

	def __str__(self):
		# Obtain the support line numbers
		supportLines = [i()._num for i in self._support]
		
		# Arrange the support line numbers in some order
		supportLines.sort()
		
		# Get the numbering scheme from the proof
		numbering = self._proof()._numbering
		
		# get this line number from the numbering scheme
		lineNum = numbering(self._num)
		
		# start the result as the line number and a tab then the sentence
		ret = str(lineNum) + '\t' + str(self._sentence)
		
		if self._inference is not None:
			# If the inference is set then add it's name
			ret += '\t' + str(self._inference.name)
		else:
			# Otherwise add ??? to denote it has not been set
			ret += '\t' + '???'

		# Only add the supportLines if there are 1 or more
		if len(supportLines) > 0:
			ret += '\t'
			for supportLine in supportLines:
				# For each support number get its printed value via numbering
				ret += str(numbering(supportLine)) + ', '
			# Delete the last ', '
			ret = ret[:-2]

		return ret

	def __hash__(self):
		# The hash is the hash of its string reprenstation
		return hash(str(self))

	def setSentence(self, sen):
		'''
		Set the sentence of this line
		'''
		# Reset the line number. Used for verification
		self._num = None
		
		# set the sentence
		self._sentence = sen

	def getSentence(self):
		return self._sentence

	def setInference(self, inf):
		self._num = None
		self._inference = inf

	def getInference(self):
		return self._inference

	def addSupport(self, line):
		import weakref
		# Reset the line number. Used for verification
		self._num = None
		
		# Add the lines as a weak reference
		self._support.add(weakref.ref(line))

	def discardSuppprt(self, line):
		# Reset the line number. Used for verification
		self._num = None
		
		# discard the line from the set
		self._support.discard(line)

	def getSuppprt(self):
		return self._support

