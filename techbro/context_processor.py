from cart.models import Shopcart
from techbro.models import *


def cartcount(request,):
    count = Shopcart.objects.filter(user__username = request.user.username, paid = False)
    user1 = user__username = 1
    

    itemcount = 0

    for item in count:
        # itemcount += user1
        itemcount += item.c_item

    context = {
        'itemcount' : itemcount
    }

    return context