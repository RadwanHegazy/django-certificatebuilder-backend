from rest_framework import serializers
from certificate.factory import CertificateBuilder

class CertificateSerializer (serializers.Serializer) :
    bg_img = serializers.ChoiceField(choices=(
        ('cer_green','cer_green'),
        ('cer_blue','cer_blue'),
        ('cer_purple','cer_purple'),
    ))
    client = serializers.CharField()
    description = serializers.CharField()
    head = serializers.CharField()
    signer = serializers.CharField()

    def save (self) :
        certificate = CertificateBuilder(**self.validated_data)
        certificate.build()
        self.certificate_path = certificate.output
        return certificate