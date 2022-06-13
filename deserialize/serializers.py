from rest_framework import serializers
from .models import Country, PetroleumProduct, Detail

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        
    def create(self, validated_data):
        # create stages
        data = validated_data
        print(data)
        import pdb; pdb.set_trace()
        country = create_country(**validated_data)
        return country
     
        

class PetroleumProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetroleumProduct
        fields = "__all__"
        
    def create(self, validated_data):
        # create stages
        petroleum_product = create_petroleum_product(**validated_data)
        return petroleum_product


class DetailSerializer(serializers.ModelSerializer):
    # petroleum_product = serializers.StringRelatedField(many=False)
    # country = serializers.StringRelatedField(many=False)

    class Meta:
        model = Detail
        fields = "__all__"
        

class DetailListSerializer(serializers.Serializer):
    petroleum_product__name  = serializers.CharField(max_length=50)
    sale__sum = serializers.IntegerField()
    
    
