class Bil:

   #constructor körs först
   def __init__(self, fabrikat, color, lager): 
        self.fabrikat = fabrikat 
        self.color = color
        self.lager = lager

   def getfabrikat(self):
      return self.fabrikat


   def setfabrikat(self, fabrikat):
      self.fabrikat = fabrikat 

   def setColor(self,color):
      self.Color =color   


   def getcolor(self):  
      return self.color



   def setlager(self, lager):
       self.lager =lager

   def getlager(self):
      return self.lager
