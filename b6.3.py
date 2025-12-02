print('Nguyen Ngoc Chi MSSV 245752021610164')
#Class co so
class Nguoi(object):
      def getGender( self ):
          return "Unknown"
#Class Nam ke thua tu Nguoi        
class Nam( Nguoi ):
      def getGender( self ):
          return "Nam"
#Class Nu ke thua tu Nguoi
class Nu( Nguoi ):
      def getGender( self ):
        return "Nu"
#Tao doi tuong tu cac lop con
aNam = Nam()
aNu= Nu()
#In ket qua tu phuong thuc getGender cua cac doi tuong
print (aNam.getGender())     #In ra "Nam"
print (aNu.getGender())      #In ra "Nu"
