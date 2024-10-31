from django.contrib import admin
from databasePI.models import User, ChatbotSession, UserTips, ChatbotOption, UserResponse

# Registrar cada modelo no admin
admin.site.register(User)
admin.site.register(ChatbotSession)
admin.site.register(UserTips)
admin.site.register(ChatbotOption)
admin.site.register(UserResponse)
