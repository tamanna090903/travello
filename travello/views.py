from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
	dest1 = Destination()
	dest1.name = 'Mumbai'
	dest1.desc = 'the city that never sleeps'
	dest1.price = 700
	

	dest2 = Destination()
	dest2.name = 'Thailand'
	dest2.desc = 'the city that never sleeps'
	dest2.price = 600
	


	dest3 = Destination()
	dest3.name = 'Francisco'
	dest3.desc = 'the city that never sleeps'
	dest3.price = 600
	

	dests = [dest1, dest2, dest3]
	return render(request ,"index.html", {'dests': dests})
