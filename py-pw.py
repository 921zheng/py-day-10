user=input("what is your name")
password=input("what is your pw")


length_pw=len(password)
secret=length_pw * '*'
print(f"{user}'s password is {secret} and it is {length_pw} digit")