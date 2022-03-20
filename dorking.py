import time


website = input("Enter Website: ")

print("======GITHUB DORKS STARTING======")
time.sleep(2)

with open('githubdorks.txt') as githubWordlist:
     for line in githubWordlist:
        githubURL = "https://github.com/search?q=" + website + line + "&s=indexed&type=Code",
        print(githubURL, "\n")
print("======GITHUB DORKS ENDED======", "\n")
print("\n")
time.sleep(2)


print("======GOOGLE DORKS STARTING======")
time.sleep(2)
with open('googledorks.txt', encoding = 'cp850') as googleWordlist:
        for line in googleWordlist:
                googleWebsite = website.replace('"','')
                url = "https://www.google.com/search?q=" + "site:" + googleWebsite
                print(url, line)
print("======GOOGLE DORKS ENDED======") 


