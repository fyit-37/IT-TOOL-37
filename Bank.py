class Bank:
     u_name = str(input("Enter name  : "))
     u_acc = str(input("Enter account number :"))
     u_curr_bal = 0

     def user_details(self):
          u_name = str(input("Enter your name : "))
          if u_name == Bank.u_name:
               print(f'The account number of the {u_name} is : {Bank.u_acc}')
               print(f'The current balance of the  {u_name} is : {Bank.u_curr_bal}')

     def deposit(self):
          u_name = str(input("Enter your name : "))
          if u_name == Bank.u_name:
               d_amt = int(input("Enter the amount you want to deposit :"))
               Bank.u_curr_bal += d_amt
               print(f"The current balance is {Bank.u_curr_bal}")

     def withdraw(self):
          u_name = str(input("Enter your name : "))
          if u_name == Bank.u_name:
               w_amt = int(input("Enter the amount you want to deposit :"))
               Bank.u_curr_bal -= w_amt
               print(f"The current balance is {Bank.u_curr_bal}")

a = Bank()
while True:
     print("------Menu------")
     print("1. View user details")
     print("2. Deposit amount")
     print("3. Withdraw amount")
     print("4. Quit")
     u_opt = int(input("Enter option :"))
     if u_opt == 1:
          a.user_details()
     elif u_opt == 2:
          a.deposit()
     elif u_opt == 3:
          a.withdraw()
     elif u_opt == 4:
          break
               
          
