import random
import operator
file = open(r"C:\Users\Alon\Desktop\project.txt","r+")
#function that tells the length of the chracters in the page
def sum_all(file):
    file.readlines()
    sum = file.tell()
    file.seek(0)
    return sum
#check if the player win
def check(file):
    file.seek(count)
    if "TREASURE".find(file.readline(1)) != -1:
        print("you win!")
        file.seek(count)
        print(f"you have landed on {file.readline(1)}!")
        return True
    else:
        charcter = file.readline(1)
        print(f"you didn`t find the tearsure but you landed on {charcter}")
        file.seek(count)
#from line 23 we are creating the map of the game
def map(file):
 for number in range(1,10):
    random_times = random.randint(1,20)
    for i in range(1,random_times + 1):
        file.write(f"{number}")
        if file.tell() % 40 == 0:
            file.write("\n")
 file.write("TREASURE")
 for number in range(9,0,-1):
    random_times = random.randint(1,20)
    for i in range(1,random_times + 1):
        file.write(f"{number}")
        if file.tell() % 40 == 0:
            file.write("\n")
map(file)
#start palying
print("you`re playing find the treasure!")
print("in order to move towards the treasure you need to specify how many steps you want to make and"
      " forward or backward")
list_of_players = []
while True:
  win = ""
  name = input("enter your name")
  user_input = input("write the number of steps and forward/backword")
  allCharcters = sum_all(file)
  count = 0
  track = 0
  number_of_turns = 0
  error = 0
  while win != True:
    number_of_turns += 1
    if track == 0:
      try:
       user_input_list = user_input.split()
      except:
       print("you didnt enter the moves correctly!")
       error += 1
       break
    if user_input_list[1] == "forward":
        if allCharcters < int(user_input_list[0]) + file.tell():
            print("you can`t go there because it`s out of the map!")
        else:
            count += file.seek(int(user_input_list[0]))
            win = check(file)
    elif user_input_list[1] == "backward":
        if file.tell() - int(user_input_list[0]) < 0:
            print("you can`t go there because it`s out of the map!")
        else:
            count -= int(user_input_list[0])
            win = check(file)
    else:
        print("please enter proper values")
    if win != True:
      new_input = input("enter your new move!")
      try:
        user_input_list = new_input.split()
      except:
          print("you didnt enter the moves correctly!")
          error += 1
          break
      track +=1
  if error > 0:
      continue
  str1 = "name"
  str2 = "score"
  if len(list_of_players) <10:
    this_player = {"name":name,"score":number_of_turns}
    list_of_players.append(this_player)
    file = open(r"C:\Users\Alon\Desktop\project.txt", "w+")
    map(file)
    list_of_players.sort(key=operator.itemgetter("score"))
    for i in range(0,len(list_of_players)):
      file.write("\n")
      file.write(f"{list_of_players[i][str1]} : {str(list_of_players[i][str2])}")
    i = 0
  else:
    this_player = {"name": name, "score": number_of_turns}
    if list_of_players[9]["score"] > this_player["score"]:
        list_of_players[9] = this_player
        file = open(r"C:\Users\Alon\Desktop\project.txt", "w+")
        map(file)
        list_of_players.sort(key=operator.itemgetter("score"))
        for i in range(0, len(list_of_players)):
            file.write("\n")
            file.write(f"{list_of_players[i][str1]} : {str(list_of_players[i][str2])}")
        i = 0
  answer = input("do you want to keep playing?")
  if answer == "no":
    break
file.close()
