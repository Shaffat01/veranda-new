import os
from django.core.wsgi import get_wsgi_application

# আপনার প্রজেক্টের নাম নিশ্চিত করুন
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veranda_project.settings')

# এই লাইনটি 'application' ডিফাইন করে
application = get_wsgi_application()

# Vercel এই 'app' ভেরিয়েবলটি খোঁজে
app = application