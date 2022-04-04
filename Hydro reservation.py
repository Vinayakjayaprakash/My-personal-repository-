#Vinayak Jayaprakash IST 140
#hydro reservation
common_list= []
vip_list = []
def fourthmessage ():
    print("Currently the ride operates by having 3 people in it that being 1 vip rider and 2 general riders")
    print("Here are the current riders ")
    print(vip_list[0] +",  " +common_list[0] +",  "+ common_list[1])
def errormessage():
    print("That was not a correct input please try again: ")
def thirdmessage():
    print("The current list of VIP's are: ")
    print(vip_list)
    print("The current list of common riders are: ")
    print(common_list)
def vipmessage():
    print("Thank you for becoming a VIP!")
def novipmessage():
        print("Ok that's fine that you don't want to be a VIP! Since you still registered you will be put down as a common rider you can always come back to this menu and say yes to being a VIP to be added to the VIP line")
def vipinfo():
    print("The VIP pass is $60 it includes free drink refills and the benefit of being first in line for select rides")
def intro():
    print("Hello user welcome to the hydro reservation system, please click on menu option 1-4 to begin")
intro()
menu_items = ["Enter name to reserve place in common line  ", "Sign up/ learn more about being a VIP", "Check list of common riders and VIP riders","search name to check place in line", "Dispatch ride"]
for count, items in enumerate(menu_items, start=1):
 output = "Menu Option" + str(count) + ":  " + str(items)
 print(output)
user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
user_input=user_input.upper()
while user_input != "EXIT":
  if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input!= "5"and user_input != "EXIT":
    errormessage()
    user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
    user_input = user_input.upper()
  if user_input == "1":
      entername = input("Please enter your name:  ")
      formathexample = entername.title()
      print("Your entered your name as: ", formathexample)
      common_list.append(entername)
      print("The current list of common riders are: ")
      print(common_list)
      print("You have now reserved your spot in line for the hydro coster if you would like to skip the common line consider becoming a VIP!")
      user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
      user_input = user_input.upper()
  if user_input == "2":
      entername = input("Please enter your name:  ")
      formathexample = entername.title()
      print("Your entered your name as: ", formathexample)
      VIPstatus = (input("Would you like to be a VIP?(Y/N) Enter in 'VIP' to hear about VIP costs"))
      VIPstatus = VIPstatus.upper()
      if VIPstatus != "Y" and VIPstatus != "N" and VIPstatus != "VIP":
        errormessage()
        VIPstatus = (input("Would you like to be a VIP?(Y/N) Enter in 'VIP' to hear about VIP costs"))
        VIPstatus = VIPstatus.upper()
      if VIPstatus == "Y":
          vipmessage()
          vip_list.append(entername)
          print("The current list of VIP's are: ")
          print(vip_list)
          user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
          user_input = user_input.upper()
      if VIPstatus == "N":
          novipmessage()
          common_list.append(entername)
          print("The current list of common riders are: ")
          print(common_list)
          user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
          user_input=user_input.upper()
      if VIPstatus == "VIP":
          vipinfo()
          VIPstatus = (input("Would you like to be a VIP?(Y/N) Enter in 'VIP' to hear about VIP costs"))
  if user_input == "3":
      thirdmessage()
      user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
  if user_input == "4":
    print("please enter your name to check your place in the line")
    entername = input("Please enter your name:  ")
    formathexample = entername.title()
    print("Your entered your name as: ", formathexample)
    conter = 0
    for name in common_list:
       conter = conter + 1
       if name==entername:
           print("your place in the common line is " + str(conter))
    conter = 0
    for name in vip_list:
       conter = conter + 1
       if name == entername:
         print("your place in the vip line is " + str(conter))

    user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))

  if user_input == "5":
      fourthmessage()
      removelist = (input("For ride operators only please choose if you wish to remove the 3 people from the list(Y/N) "))
      removelist = removelist.upper()
      if removelist == "Y":
          del vip_list[0]
          del common_list[0]
          del common_list[0]
      user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
      user_input = user_input.upper()
      print(common_list)
      if removelist== "N":
          print("got it nothing will be deleated")
          user_input = str(input("Please enter in a menu option or type 'EXIT' in order to terminate the program "))
          user_input = user_input.upper()
