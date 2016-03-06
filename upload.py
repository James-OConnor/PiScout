import os
import requests

n = 1
print("Attemting to upload matches...")
if os.path.isfile('queue.txt'):
	with open("queue.txt", "r") as file:
		try:
			for line in file:
				requests.post("http://52.2.17.191/submit", data={'data': line})
				print("Uploaded entry number " + str(n))			
				n += 1
		except:
			print("Failed miserably. Are you connected to the internet?")
	os.remove('queue.txt')
else:
	print("The match queue doesn't exist.")
print("Finished.")
input("Press Enter to exit")
