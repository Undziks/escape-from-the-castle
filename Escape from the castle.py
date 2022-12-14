import random

def showInstructions():
  #print a main menu and the commands
  print('''RPG GAME
--------------------------------------------------------------
Instruction: Your mision is to escape from a deserted castle.
But before this you must find keys and avoid strange monsters.
You can go north, south, east and west.
--------------------------------------------------------------
''')   
                    
  print('''========
Commands:
  go [direction]
  get [item]
  quit or exit - to leave the game
''')

def showStatus():
  #print the player's current status
  global end_game 
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  directions = list(rooms[currentRoom].keys())
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
    directions.remove('item')
  print("You can go to:", directions)
  print("---------------------------")
  if 'Meeting Place' in currentRoom:
      x, y = random.randrange(1,12), random.randrange(1,12)
      print("Mathematic challenge!", x, "*", y)
      multi = input(">")
      if int(multi) != int(x * y):
          end_game = True
      else:
          print("Good answer, keep playing!")


#an inventory, which is initially empty
inventory = []

end_game = False

#a dictionary linking a room to other rooms
rooms = {

            'Gate' : { 
                  'south' : 'Empty Room',
                  'east' : 'Meeting Place'
                },

            'Empty Room' : {
                  'north' : 'Gate',
                  'east' : 'Living Room',
                  'south' : 'Kings Chamber'
                },
            
            'Meeting Place' : {
                'west' : 'Gate',
                'south' : 'Living Room',
                'east' : 'Knight Room',
                'item' : 'cat'
                },
            
            'Living Room' : {
                'west' : 'Empty Room',
                'north' : 'Meeting Place',
                'item' : 'knife',
                'east' : 'Square',
                'south' : 'Queens Chamber'
                },
            
            'Knight Room' : {
                'west' : 'Meeting Place',
                'south' : 'Square',
                'item' : 'key',
                'east' : 'Toilet'
                },
            
            'Square' : {
                'west' : 'Living Room',
                'north' : 'Knight Room',
                'item' : 'monster',
                'south' : 'Magicjan Room'
                #'item' : 'Axolotl in Russian tank'
                },
            
            'Kings Chamber' : {
                'north' : 'Empty Room',
                'south' : 'Trazury',
                'east' : 'Queens Chamber',
                'item' : 'monster'
                },
            
            'Queens Chamber' : {
                'north' : 'Living Room',
                'west' : 'Kings Chamber',
                'east' : 'Magicjan Room',
                'south' : 'Stable',
                'item' : 'key'
                },
            'Magicjan Room' : {
                'north' : 'Sqare',
                'east' : 'Dining Room',
                'south' : 'Stable',
                'west' : 'Queens Chamber',
                'item' : 'monster'
                }
         }

#start the player in the Gate
currentRoom = 'Gate'

showInstructions()

#loop forever
while True:

  showStatus()
  
  if end_game:
    print("Wrong answer! GAME OVER!")
    break

  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  
  if move[0] in ['exit', 'quit']:
      print("You left the game. GAME OVER!")
      break

  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful messagees
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  if set(['cat', 'gun']).issubset(set(inventory)):
      print("---------------------------")
      print('Great you have a Cat Soldier!')
      i = inventory.index('cat')
      inventory = inventory[:i]+['cat soldier']+inventory[i+1:]
      inventory.remove('gun')
      
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      if 'cat' in inventory:
          print("A monster has been defeated, thanks to your cat!")
          rooms[currentRoom]['item'] = 'defeated monster'
      else:
          print("A monster has got you... GAME OVER!")
          break