
from rest_framework import serializers
from api.models import CodeExplainer
from api.utils import send_code_to_api

class CodeExplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeExplainer
        fields = ("id","_input","_output")
        extra_kwargs = {
            "_output":{"read_only":True}    
        }

    def create(self, validated_data):
        # # Assuming chat_with_chatbot returns the response directly
        # _input = validated_data.get("_input", "")  # Get the input from validated_data
        # agent_executor = main(_input)

        # # Adjust this line based on the actual structure of the response in AgentExecutor
        # _output = getattr(agent_executor, 'response', "Default value")

        # ce = CodeExplainer(_output=_output, **validated_data)
        # ce.save()
        # return ce
        ce = CodeExplainer(**validated_data)
        _output = send_code_to_api(validated_data["_input"])
        ce._output = _output
        ce.save()
        return ce
    



