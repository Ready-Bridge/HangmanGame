import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


        
    
    

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        
        
        if parse[0] == 'add':
            try :                               #add 예외처리
              if len(parse) > 4 :
                print('add (Name) (Age) (Score)') 
              
              elif '' in parse :
                print('add (Name) (Age) (Score)')

              else : 
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                scdb += [record]
            
            except IndexError :
              print('add (Name) (Age) (Score)')
            
            except ValueError :
              print('add (Name) (Age) (Score)')
            
               
        #del 기능 수정
        elif parse[0] == 'del':
            try :                           # del 예외처리
              if len(parse) > 2 :
                print("del (Name)")
              
              else :
                for p in scdb[:]:
                    if p['Name'] == parse[1]:                                  
                        scdb.remove(p)    
              
            except IndexError :
              print('del (Name)')
                        
        elif parse[0] == 'show':      
            try :                                   #show 예외처리
              if len(parse) > 2 :
                print('show (Name or Age or Score)')
              
              else :    
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            
            except KeyError :
              print('show (Name or Age or Score)')
          
        #find 기능 추가
        elif parse[0] == 'find':
            try :
              if len(parse) > 2 :
                print('find (Name)')
              
              else :  
                name = parse[1]
                findScoreDB(scdb, name)
            
            except IndexError :
              print('find (Name)')
          
        #inc 기능 추가
        elif parse[0] == 'inc':
            try :                                   #inc 예외처리
              if len(parse) > 3 :
                print('inc (Name) (Amount of Score)')
              
              else :  
                name = parse[1]
                amount = int(parse[2])
                incScoreDB(scdb, name, amount)
            
            except IndexError :
              print('inc (Name) (Amount of Score)')
            
        elif parse[0] == 'quit':
          
          if len(parse) > 1 :         #quit 예외처리(?)
            print('Enter \'quit\' ')
          else :  
            break
        
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]) , end=' ')
        print()

#find 기능에서 사용할 함수
def findScoreDB(scdb, name) :
      for i in scdb:
          if i['Name'] == name:    
              for k in i:              
                  print(k + "=" + str(i[k]) , end=' ')
              print()
              
#inc 기능에서 사용할 함수
def incScoreDB(scdb, name, amount) :
    for i in scdb:
        if i['Name'] == name :
          i['Score'] += amount


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)