# Fun Intelligence Calculator

print("Welcome to the Intelligence Calculator!\n")
name = input("Enter your name: ")

print("\nAnswer the following questions:")

score = 0

# Question 1
ans = input("Q1: What is 5 + 7? ")
if ans.strip() == "12":
    score += 1

# Question 2
ans = input("Q2: Which planet is known as the Red Planet? ")
if ans.lower().strip() == "mars":
    score += 1

# Question 3
ans = input("Q3: If you have 3 apples and take away 2, how many do you have? ")
if ans.strip() == "2":
    score += 1

# Question 4
ans = input("Q4: What is the capital of France? ")
if ans.lower().strip() == "paris":
    score += 1

# Question 5
ans = input("Q5: What comes next in the sequence: 2, 4, 8, 16, ? ")
if ans.strip() == "32":
    score += 1

print("\n--- Intelligence Report ---")
print(f"Name: {name}")
print(f"Score: {score}/5")

if score == 5:
    print("Genius Level! Super Intelligent 🚀")
elif 3 <= score < 5:
    print("Smart! You have good intelligence.")
elif 1 <= score < 3:
    print("Average, but you can improve!")
else:
    print("Keep learning, intelligence grows with practice.")

print("An Intelligence Calculator can’t really measure true IQ (that needs scientific testing), but we have made a fun program in Python that asks the user some questions, gives them a score, and then shows a playful intelligence level.")    
