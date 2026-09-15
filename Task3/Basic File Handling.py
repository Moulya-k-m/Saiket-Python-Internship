try:
    with open("sample.txt","r") as file:
     data=file.read()
     old=input("Enter the string to be replaced: ")
     new=input("Enter the new string: ")
     rep=data.replace(old,new)
     if old in data:
        print("---------------------------")
        count=data.count(old)
        print(f"No.of replacements: {count}")
        with open("sample.txt","w") as file:
                file.write(rep)
        print("Word found and replaced")
        print("---------------------------")
        print(rep)
        print("---------------------------")
     else:
        print("Word not found")
except FileNotFoundError:
    print("File not found")