from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
from IPython.display import display, HTML
import openpyxl
import time

capabilities={
    "platformName": "Android",
     "platformVersion": "9.0",
     "deviceName": "BlueStack",
     "automationName" : "Appium"
}

#trucashAccounts=pd.read_excel("balance pay8.xlsx",  encoding='utf8')
trucashAccounts=pd.read_csv("trucashAccount.csv", encoding='utf8')

# display(trucashAccounts)

#Structurizing DATA
cvv=trucashAccounts["CVV"]
expiery=trucashAccounts["Expiery"]
cardNumber=trucashAccounts["Card_Number"]

#Defining Months Keys
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

#Generating Driver
driver=webdriver.Remote("http://127.0.0.1:9900/wd/hub",capabilities)
count=0
status=""
#Infinity Loop
while(True):
    #Swipe for find app
    
    for i in range(1,26):
        print(i)
        try:
            #driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[22]").click()
            appName=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView["+str(i)+"]").text
            print(appName)
            if str(appName)=="TruCash Balance Checker":
                status="found"
                driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView["+str(i)+"]").click()
                break
        except:pass
    if count==9:break
    if status=="found":break
    count+=1
    driver.swipe(600, 300, 100, 500)
time.sleep(3)


#Login
data=[]
accountNumber=""
for i in range(len(cvv)):
    expDate=""
    if expiery[i][-3:] in months:
        expDate=str(int(months.index(expiery[i][-3:]))+1)+str(expiery[i][0:2])     
    print(expDate)
    cn=cardNumber[i][-9:-1]
    print(cn)
    accountNumber=cn
    try:
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText").set_text(cn);
    except:pass
    try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").set_text(str(cvv[i]))
    except:pass
    try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").set_text(expDate)
    except:pass
    try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button").click()
    except:pass
    try:
        driver.find_element(By.ID,"com.trucash.balance_tracker_prepaid:id/tvOK").click()
        try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText").set_text(cn);
        except:pass
        try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").set_text(str(cvv[i]))
        except:pass
        try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").set_text(expDate)
        except:pass
        try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button").click()
        except:pass
    except:pass
    try:driver.find_element(By.ID,"com.trucash.balance_tracker_prepaid:id/buttonSkip").click()
    except:time.sleep(5)
    try:driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
    except:pass
    try:driver.find_element(By.ID,"com.trucash.balance_tracker_prepaid:id/action_activity").click()
    except:pass
    try:driver.find_element(By.XPATH,'//androidx.appcompat.app.ActionBar.Tab[@content-desc="All"]/android.widget.TextView').click()
    except:
        try:
            driver.find_element(By.ID,"com.trucash.balance_tracker_prepaid:id/action_activity").click()
            driver.find_element(By.XPATH,'//androidx.appcompat.app.ActionBar.Tab[@content-desc="All"]/android.widget.TextView').click()
        except:
            pass
    try:
        transactions=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout").text
        print(transactions)
    except:pass
    time.sleep(10)
    allDates=[]
    allTransactionName=[]
    allTransactionAmount=[]
    previousState=[]
    while(True):
        currentState=[]
        temp=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
        for t in temp:
            print(t.text)
            currentState.append(t.text)
        if currentState==previousState:break
        else:
            data.append([i for i in currentState])
            previousState=currentState
        driver.swipe(300, 700, 300, 300)
    print(data)
    
    currentBalance=""
    for i in data[0][4:6]:
        currentBalance=currentBalance+i
        
    print("\n\n\nCurremt Balance:",currentBalance,"\n\n\n")
        
    count=0
    transactions=[]
    for j in data:
        tempCount=0
        temp=[]
        if count==0:
            for k in range(11,len(data[count])-3):
                temp.append(data[count][k])
            transactions.append(temp)
        else:
            for k in range(3,len(data[count])-3):
                temp.append(data[count][k])
            transactions.append(temp)
        count+=1
    
    individualTransactions=[]
    globalCount=0
    for i in transactions:
        temp=[]
        count=1
        for j in i:
            temp.append(j) 
            if count%4==0:
                if str(temp[-1]).find("$") == -1:
                    temp2=[]
                    try:temp2.append(individualTransactions[globalCount-1][0])
                    except:temp2.append("")
                    temp2.append(temp[0])
                    temp2.append(temp[1])
                    temp2.append(temp[2])
                    individualTransactions.append(temp2)
                else:individualTransactions.append(temp)
                temp=[]
                count=0
            count+=1
        globalCount+=1
            
    transactionsAll=[]
    for i in individualTransactions:
        if i in transactionsAll:pass
        else:
            transactionsAll.append(i)
            
    dataFormatizing={"Date":[],"Title":[],"Detail":[],"Price":[]}
    for i in transactionsAll:
        dataFormatizing["Date"].append(i[0])
        dataFormatizing["Title"].append(i[1])
        dataFormatizing["Detail"].append(i[2])
        dataFormatizing["Price"].append(i[3])
        
    df=pd.DataFrame(dataFormatizing)
    df.to_csv(accountNumber+".csv")
    try:
        #Logout
        driver.find_element(By.ID,"com.trucash.balance_tracker_prepaid:id/action_more").click()
        driver.swipe(300, 700, 300, 100)
        driver.swipe(300, 700, 300, 100)
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[7]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()
    except:pass