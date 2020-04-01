import django
from .models import Post, Requirements
# x = Post.objects.all()
# for y in x:
# 	print(y)
def check():
	return "Summa\nis\nan\nemotion"

def get_req():
	x = Requirements.objects.all()
	retur = ""
	for y in x:
		retur = retur + str(y) + "\n"
	return retur


