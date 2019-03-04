# -*-coding:Latin-1-*

class DicoOrdonne:

	def __init__(self,dico2=None,**kwargs):
		self.index=-1
		listecle=[]
		listevaleur=[]
		self.listecle=listecle
		self.listevaleur=listevaleur

		if kwargs is None:
			self._dictionnaire = {}
		if len(kwargs)>0:
			for cle,valeur in kwargs.items():
				listecle.append(cle)
				listevaleur.append(valeur)
		dico24=dict(zip(listecle,listevaleur))
		self._dictionnaire = dico24

		if dico2 is not None:					
			self._dictionnaire= dico2

	def __repr__(self):
		return("{}".format(self._dictionnaire))

	def __getitem__(self,cle):
		return self._dictionnaire[cle]

	def __setitem__(self,cle,valeur):
		if cle in self._dictionnaire.keys():
			index=self.listecle.index(cle)
			self.listevaleur[index]=valeur
			dico24=dict(zip(self.listecle,self.listevaleur))
			self._dictionnaire=dico24
		else:
			self.listecle.append(cle)
			self.listevaleur.append(valeur)
			dico24=dict(zip(self.listecle,self.listevaleur))
			self._dictionnaire=dico24

	def __delitem__(self,cle):
		index = int(self.listecle.index(cle))
		del self.listecle[index]
		del self.listevaleur[index]
		dico24 = dict(zip(self.listecle,self.listevaleur))
		self._dictionnaire = dico24

	def __contains__(self,cle_averif):
		return self.listecle.__contains__(cle_averif)

	def __len__(self):
		return self._dictionnaire.__len__()

	def sort(self):
		listetuples=list(zip(self.listecle,self.listevaleur))
		del self.listecle[:]
		del self.listevaleur[:]
		listetuples.sort()
		for i in listetuples:
			self.listecle.append(i[0])
			self.listevaleur.append(i[1])
		dico24 = dict(zip(self.listecle, self.listevaleur))
		self._dictionnaire = dico24

	def reverse(self):
		listetuples = list(zip(self.listecle, self.listevaleur))
		del self.listecle[:]
		del self.listevaleur[:]
		listetuples.reverse()
		for i in listetuples:
			self.listecle.append(i[0])
			self.listevaleur.append(i[1])
		dico24 = dict(zip(self.listecle, self.listevaleur))
		self._dictionnaire = dico24

	def __next__(self):
		maxi=int(len(self.listecle))
		self.index = self.index + 1
		try:
			self.listecle[self.index]
		except IndexError:
			self.index=-1
			raise StopIteration
		return self.listecle[self.index]

	def __iter__(self):
		return self

	def keys(self):
		return(self._dictionnaire.keys())
	def values(self):
		return(self._dictionnaire.values())
	def items(self):
		return(self._dictionnaire.items())

	def __add__(self, objadd):
		dicoadd=objadd._dictionnaire
		self._dictionnaire.update(dicoadd)

