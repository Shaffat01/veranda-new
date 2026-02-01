import os
from pathlib import Path
from django.templatetags.static import static
import dj_database_url

# root-directory
BASE_DIR = Path(__file__).resolve().parent.parent

# security
SECRET_KEY = 'django-insecure-your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost']

# applications
INSTALLED_APPS = [
    'jazzmin',   
    # "unfold", 
    # "unfold.contrib.filters", 
    # "unfold.contrib.forms",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'veranda_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # আপনার templates ফোল্ডার
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'veranda_project.wsgi.application'

# ডাটাবেজ (ডিফল্ট SQLite ব্যবহার করা হয়েছে)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}
# পাসওয়ার্ড ভ্যালিডেশন
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ভাষা ও সময়
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- স্ট্যাটিক ও মিডিয়া ফাইল কনফিগারেশন ---

# CSS, JS, এবং থিম ইমেজের জন্য
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# এই লাইনটি WhiteNoise কে ফাইল কমপ্রেস করতে সাহায্য করবে
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# অ্যাডমিন প্যানেল থেকে আপলোড করা ছবির জন্য
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ডিফল্ট অটো ফিল্ড
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'admin_dashboard'
LOGOUT_REDIRECT_URL = 'login'


# UNFOLD = {
#     "SITE_TITLE": "Veranda Admin",
#     "SITE_SYMBOL": "speed", # Material Symbols থেকে আইকন
#     "site_title": "Veranda Admin",
#     "site_header": "Veranda",
#     "site_brand": "Veranda Administration", 
    
#     "COLORS": {
#         "primary": {
#             "50": "250 245 239",
#             "100": "241 230 216",
#             "200": "225 201 172",
#             "300": "202 165 120",
#             "400": "184 135 83",
#             "500": "166 110 58", 
#             "600": "141 87 47",
#             "700": "114 67 40",
#             "800": "94 56 36",
#             "900": "79 48 32",
#             "950": "44 25 16",
#         },
#     },
#     "SIDEBAR": {
#         "show_search": True,
#         "show_all_applications": True,
#     },

#     "TABS": [
#     {
#         "models": ["core.homecontent", "core.inquiry", "core.testimonial"],
#         "items": [
#             {"title": "Overview", "link": "admin:index", "icon": "dashboard"},
#             {"title": "Booking Request", "link": "admin:core_inquiry_changelist", "icon": "mail"},
#         ],
#     },
# ],
# }




JAZZMIN_SETTINGS = {
    # ড্যাশবোর্ডের টাইটেল
    "site_header": "Veranda",
    
    # আপনার লোগো (static ফোল্ডারে যে পাথে আছে)
    "site_logo": "images/Veranda Logo/Logo.jpg", 
    
    # ওয়েবসাইটের কপিরাইট টেক্সট
    "copyright": "Veranda Event Venue",
    
    # লগইন স্ক্রিনের ওয়েলকাম মেসেজ
    "welcome_sign": "Welcome to Veranda Dashboard",
    
    # টপ মেনুতে 'View Site' বাটন যোগ করা
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Visit Website", "url": "/", "new_window": True},
    ],
    
    # ইউজার প্রোফাইল মেনু
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    
    # সাইডবার সেটিংস
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # আইকন কাস্টমাইজেশন (অপশনাল)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
}

# কালার থিম (আপনার ব্র্যান্ডের সাথে মিলিয়ে গোল্ডেন/ডার্ক থিম)
JAZZMIN_UI_TWEAKS = {
    "theme": "solar",  # অথবা 'cyborg', 'slate', 'superhero' ট্রাই করতে পারেন
    "dark_mode_theme": "darkly",
    
    # নেভিগেশন বারের কালার
    "navbar": "navbar-dark",
    "brand_colour": "navbar-primary",
    
    # সাইডবার
    "sidebar": "sidebar-dark-warning", # এখানে গোল্ডেন/ওয়ার্নিং কালার দিলে Veranda-এর সাথে মিলবে
    "no_navbar_border": True,
    
    # বাটন স্টাইল
    "button_classes": {
        "primary": "btn-outline-primary", # আউটলাইন বাটন বেশি মডার্ন লাগে
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }

}
