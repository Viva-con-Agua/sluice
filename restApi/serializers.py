from rest_framework import serializers
from register.models import Microservice

class MicroserviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Microservice
        fields = ('name', 'url', 'publicKey', 'created_date', 'modifyed_date') 

   # iid = serializers.IntegerField(read_only=True)
   # name = serializers.CharField(max_length=200)
   # url = serializers.CharField(max_length=200)
   # publicKey = serializers.TextField()
   # modifyed_date = serializers.DateTimeField(blank=True, null=True)

   # def create(self, validated_data):

   #     return Microservice.objects.create(**validated_data)

   # def update(self, instance, validated_data):

   #     instance.name = validated_data.get('name', instance.name)
