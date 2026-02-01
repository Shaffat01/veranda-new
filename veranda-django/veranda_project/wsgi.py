import os

from django.core.wsgi import get_wsgi_application

# এখানে 'veranda_project' আপনার সেটিংস ফোল্ডারের নামের সাথে মিল থাকতে হবে
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veranda_project.settings')

app = application # Vercel এটি খুঁজে পাওয়ার জন্য প্রয়োজন

application = get_wsgi_application()
