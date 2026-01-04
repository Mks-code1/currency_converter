import time
import os 
dollar =  print("""
--------------------------------------------------------------------.
| .--                   MKS REVERSE NOTE                    .--      |
| |_       ......    THE UNTIED STATES OF AMERICA                |_  |
| __)    ``````````             ______            B93810455B     __) |
|      2        ___            /      \                     2        |
|              /|~\\          /  _-\\  \           __ _ _ _  __      |
|             | |-< |        |  //   \  |         |_  | | | |_       |
|              \|_//         | |-  o o| |         |   | `.' |__      |
|               ~~~          | |\   b.' |                            |
|       B83910455B           |  \ '~~|  |                            |
| .--  2                      \_/ ```__/    ....            2    .-- |
| |_        ///// ///// ////   \__\'`\/      ``  //// / ////     |_  |
| __)                   F I V E  D O L L A R S                   __) |
`--------------------------------------------------------------------'

          

          
____________________________________________________________________________________________________________________________________________________________

""")
exchange_rates = {
        ""    : dollar, # الرسمة 
        "USD" : 1.0,  # صرف الواحد دولار 
        "ERU" : 0.85, # سعر صرف الواحد دولار مقابل اليورو
        "SAR" : 3.75, # سعر صرف الواحد دولار مقابل الريال سعودي
        "SYP" : 11750,  # سعر صرف الواحد دولار ماقبل ليرة سورية
    }

def clean ():
    os.system('cls' if os.name =='nt' else 'clear')

def Display_rates():
    clean()
    print("Welcom to 'currency converter':\n")
    for currency in exchange_rates:
        print(f"{currency} : {exchange_rates[currency]}")
    
   


def currency_converter():
    clean()

    Display_rates()
# ياخذ الدولة يلي بده يحول لها 
    from_currency = input("\nChoose a currnecy to convert from: ").upper()
        

    while True :
        # الكمية 
        amount = float(input("Enter the amount: ")) 
        
        # cnfirm for contniu
        confirmation = input(f"\nyou entered {amount} {from_currency }. Confirm? (Y/N):").upper() 

        # if choos n again (ياخذ مرة ثانية الكمية ويتاكد منه)
        if confirmation == "Y":
            break
    clean()
    Display_rates()

    to_currency = input("\nChoose a currency to convert to: ").upper()
    
    print("Analyzing your reqest....please wait.")                            # سوينا تاخير في الوقت 
    time.sleep(2)
    print(
        f"Checking for {to_currency}'s best rates available .....please wait"

    )
    time.sleep(3)
    print(
        f"Getting a discount price for {from_currency}.... Please wite"
    )
    time.sleep(2)


# التحقق من اخيتار العملات بشكل صحيح  
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency. Conversion canceld.")
        time.sleep(2)
        currency_converter()    


# Find the exchange rate  
    new_rate = exchange_rates[to_currency] / exchange_rates[from_currency]

    converted_amount = amount *  new_rate 

    clean()
    print(
        f"Prepraring the deal from {from_currency} to {to_currency}.....please wite\n"
    )
    time.sleep(2)
    print(
        f"Exchange rate: 1 {from_currency} = {new_rate} {to_currency}\n\n "
    )
    time.sleep(2)
    print(
        f"{amount} {from_currency} is equal to {round(converted_amount ,2 )} {to_currency}"
    )
    time.sleep(1)
    accept_transaction = input('\nDo you accept this transaction? (Y/N)').upper()
    if accept_transaction == "Y":
        print("Transaction Successful!")
    else:
        print("transaction Canseled")
    
    another_transaction = input ("\nDo you want to perform another conversion? (Y/N): ").upper()

    if another_transaction == "Y":
        currency_converter()
    else:
        print("Thanks for you using the currency converter!")

# Start the currency converter
currency_converter()


                
           







        


     



