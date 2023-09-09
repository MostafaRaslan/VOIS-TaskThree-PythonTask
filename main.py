import pandas as pd
EmployeesSheet = "Employees.csv"
EmployeesSheetUpdated="EmployeesUpdate.csv"
dataframe = pd.read_csv(EmployeesSheet)
print("CSVFile ")
print(dataframe)
#DeleteDuplicates
New_dataframe = dataframe.drop_duplicates()
print("RemoveDropDuplicates ")
print(New_dataframe)
#ChangeTheTypeOfAgeInteger
New_dataframe['Age'] = New_dataframe['Age'].astype(int)
print("RemoveDecimalsFromAge ")
print(New_dataframe)
#ChangeValuesFROMUSDTOEGP
New_dataframe['Salary(USD)'] = New_dataframe['Salary(USD)'].multiply(35)
print("ChangeCurrencyDataFromUSDTOEGP ")
print(New_dataframe)
#ChangeTheColoumnHeaderFromUSDTOEGP
New_dataframe = New_dataframe.rename(columns={'Salary(USD)':'Salary(EGP)'})
print("ChangeTheColoumnHeaderFromUSDTOEGP ")
print(New_dataframe)
#PrintingTheMeanOfAge
AverageAge = New_dataframe['Age'].mean()
print("TheAverageAgeIs: "+str(AverageAge))
#PrintingTheMedian of Salaries
MedianSalary = New_dataframe['Salary(EGP)'].median()
print("PrintTheMedianSalary: "+str(MedianSalary))
#RatioBetweenMales&Females
NumberOFMale = len(New_dataframe[New_dataframe['Gender'] == 'M'])
print("NumberOfMale: "+str(NumberOFMale))
NumberOFFemale = len(New_dataframe[New_dataframe['Gender'] == 'F'])
print("NumberOfFemale :"+str(NumberOFFemale))
RatioValue = NumberOFMale/NumberOFFemale
print("RatioValue "+str(RatioValue))
#GETCSVFILE
New_dataframe.to_csv(EmployeesSheetUpdated)

