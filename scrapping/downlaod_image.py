import requests
r=requests.get("http://www.cusrinagar.edu.in/Content/ThemePublic/Libraries/images/cus-logo-green.png")
with open("cusrinagar.png","wb") as  f:
	f.write(r.content)
f.close()
