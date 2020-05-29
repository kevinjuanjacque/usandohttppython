import requests
import json
import webbrowser

response = requests.get('https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.pjson/?auth_key=0a0a91095dada6205777584c105b677c66abc415')
response_json=json.loads(response.text)
#print(response_json)
menor=0
comuna=input("ingrese comuna, para buscar bencinera mas economica: ")
la=0
lo=0
for x in response_json["bencinaEnLinea"]:
	
	if (x['comuna'].lower().replace(" ","")==comuna.lower().replace(" ","") and x['gasolina95']!=0 ):
		if(menor==0 or menor>x['gasolina95']):
			la=x["latitud"]
			lo=x["longitud"]
			calle=x["calle"]+" "+str(x["numero"])
			precio=x["gasolina95"]
		pass
if la==0 and lo==0 :
	print("no se encontro la comuna que buscabas")
	pass
else:
	print("la bencinera mas economica esta en "+calle+" el precio 95 octanos es de "+str(precio))
	dim=str(la)+","+str(lo)
	url="https://maps.google.com/?q="	
	url=url+str(dim)	
	webbrowser.open(url, new=1, autoraise=True)