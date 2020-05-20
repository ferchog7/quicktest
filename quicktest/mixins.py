from rest_framework import views, permissions

class MixinAuth(views.APIView):
    permission_classes = [permissions.IsAuthenticated]