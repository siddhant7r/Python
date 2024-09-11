records={}

n=int(input("How many records"))

for i in range(n):
    aadhaar=int(input("Enter Aadhar Number"))
    name=(input("Enter Name"))
    mob=int(input("Enter Mobile Number"))
    d={"name":name,
       "mobile":mob}
    
    records[aadhaar]=d
print(records)

records[0]["address"]="Bhopal"

print(records)