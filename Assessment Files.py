#1)Write a program to demonstrate the Fruit Store Console application
stock={}  #Declare blank dictionary

print("------------Fruit Market--------------")

menu="""
            1)Fruit Manager
            2)Customer
            
"""
    
print(menu)

choice=int(input("Enter Your Choice:"))
    
status=True


while status:
    
    
    if choice==1:
                
                fruit_manager_status=True
                menu1="""
                    1) Press 1 For Add Fruit Stock
                    2) Press 2 For View Fruit Stock
                    3) Press 3 For Update Fruit Stock
                """
        
                print(menu1)

                user_choice1=int(input("Select Your Task:"))


                if user_choice1==1:
                    user_status=True
                    while user_status:

                        spec={}   
                        print("ADD FRUIT STOCK")

        
                        fruit_name=input("Enter The Fruit Name:")
                        fruit_qty=int(input('Enter The Fruit Quantity(in kg):'))
                        fruit_price=int(input('Enter The Fruit Price(per kg):'))

    
                        spec['qty']=fruit_qty
                        spec['price']=fruit_price

        
                        stock[fruit_name]=spec   
                        print(stock)


                        manager_choice=input("Do you Want to add more fruit?:")
                        if manager_choice=='y' or manager_choice=='Y':
                            user_status=True
                        else:
                            user_status=False
                elif user_choice1==2:
                    print(stock)
                    print("CUSTOMER")
                    
                elif user_choice1==3:
                    spec={}   
                    print("UPDATE FRUIT STOCK")

                    
                    fruit_name=input("Enter The Fruit Name:")
                    fruit_qty=int(input('Enter The Fruit Quantity(in kg):'))
                    fruit_price=int(input('Enter The Fruit Price(per kg):'))

    
                    spec['qty']=fruit_qty
                    spec['price']=fruit_price

        
                    stock[fruit_name]=spec   
                    print(stock)


                    manager_choice=input("Do you Want to add more fruit?:")
                    if manager_choice=='y' or manager_choice=='Y':
                            user_status=True
                    else:
                            fruit_manager_status=False
                
            
                else:
                        print("Thank You For Visiting Our Shop..")
                        status=False                    
    else:
        print("Error! Please try again later....\n Enter First Manager Department")
        status=False
    
    