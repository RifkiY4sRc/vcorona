import requests,re
reqlist = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()
R = '\033[31m'
G = '\033[32m'
W = "\033[0m"
ask = """
            Author : Rifki Y4sRc
               {Corona  Tools}
         """
print (G+ask+W)
print ("[!]Get data. Please waitt... ")
print
for x in reqlist: print("______________________________________\n"+x['attributes']['Provinsi']+"\nterdeteksi \t: "+str(x['attributes']['Kasus_Posi'])+"\nmati \t\t: "+str(x['attributes']['Kasus_Meni'])+"\nsembuh \t\t: "+str(x['attributes']['Kasus_Semb'])+"\nsakit \t\t: "+str(x['attributes']['Kasus_Posi']-x['attributes']['Kasus_Meni']-x['attributes']['Kasus_Semb']))
