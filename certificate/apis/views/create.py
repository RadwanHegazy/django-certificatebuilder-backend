from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from ..serializers import CertificateSerializer

class create_cer_view (APIView) : 
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, requset, **kwargs) : 
        serializer = self.serializer_class(data=requset.data)
        if  serializer.is_valid() : 
            serializer.save()
            return Response(
                data={
                    'output' : serializer.certificate_path,
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)