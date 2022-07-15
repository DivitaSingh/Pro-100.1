class ATM(object):
     def __init__(self,ATMCard, PinNumber):
        self.ATMCard=ATMCard
        self.PinNumber=PinNumber

     def CashWidrawl():
        print ("Cash Widrawed")

     def BalanceEnquiry():
        print("Balance = ₹ 10,000 ")

     def CashTransfer():
        print("Cash has been Transfered")

cash = ATM(1259,2010)
cash.BalanceEnquiry()
cash.CashTransfer()
cash.CashWidrawl()
cash.PinNumber()
