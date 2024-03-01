from django.contrib import admin
from .models import Product
from .models import Category
from .models import Cart
from .models import Booking
from .models import Feedback
from .models import UserProfile

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(UserProfile)
