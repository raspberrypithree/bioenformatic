class DNA:
		
	def __init__(self, name,ds,seq,df,type_mod,description):
		self.NAME	=name
		self.DS		=ds
		self.SEQ	=seq
		self.DF		=df
		self.TYPE_MOD	=type_mod
		self.DESCRIPTION=description
		
		
	def olustur(self):
		length=len(self.SEQ)
		Name  		= self.NAME
		DS		= self.DS
		Seg		= self.SEQ
		DF		= self.DF
		Len		= length
		Type		= self.TYPE_MOD
		Description	= self.DESCRIPTION
		dna=[Name, DS,Seg,DF,Len,Type,Description]
		"""
		dna={
		  'name'        : self.NAME,
		   'DS'         : self.DS,
		   'seq'        : self.SEQ,
		   'DF'         : self.DF,			Not useful
		    'len'       : length,
		   'type'       : self.TYPE_MOD,
		   'description': self.DESCRIPTION
		}
		"""
		return dna	
	


	def duzenle(self):
		self.NAME		=input("Enter the name:")
		self.SEQ		=input("Enter the seq:")	
		length			=len(self.SEQ)
		self.DESCRIPTION	=input("Enter the description:")
		
		Name  		= self.NAME
		DS		= self.DS
		Seg		= self.SEQ
		DF		= self.DF
		Len		= length
		Type		= self.TYPE_MOD
		Description	= self.DESCRIPTION
		dna=[Name, DS,Seg,DF,Len,Type,Description]
		"""
		dna=[]
		dna={
		   'name'       : self.NAME,
		   'DS'         : self.DS,
		   'seq'        : self.SEQ,
		   'DF'         : self.DF,
		   'len'        : length,
		   'type'       : self.TYPE_MOD,
		   'description': self.DESCRIPTION
		}
		dna['name']=name
		dna['seq']=seq
		dna['len']=length
		dna['description']=description
		"""
		return dna
		
		

#d.olustur()

#d=DNA("DNA",5,"atgatgat",3,"DNA","First DNA")


	 
       
	
