from django.contrib import admin
from .models import Profile
from .models import Engineers
from .models import Entrepreneur
from .models import Researchers
from .models import Academician
from .models import Doctors
from .models import Category
admin.site.register(Profile)
admin.site.register(Engineers)
admin.site.register(Entrepreneur)
admin.site.register(Researchers)
admin.site.register(Academician)
admin.site.register(Doctors)
admin.site.register(Category)
