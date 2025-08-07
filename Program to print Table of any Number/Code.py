while True:
    
    n = int(input("Enter a Number: "))    
    
    file = open(f"Tables/table_of_{n}.txt", "w")
    
    for i in range(1, 11):
        line = (f"{n} X {i} = {n*i}\n")
    
        file.write(line)
    
    file.close()    
    
    
    print("Done!") 