import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema, OpenApiResponse


class ProxyView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def proxy_request(self, request, service_name, path):
        # Verify the service name
        service_url = settings.SERVICE_URLS.get(service_name)
        if not service_url:
            return Response({'error': 'Service not found'}, status=404)

        # Construct the full URL
        url = f"{service_url}/{path}"
        headers = {
            'Authorization': request.headers.get('Authorization')
        }

        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            params=request.GET,
            json=request.data
        )
        return Response(response.json(), status=response.status_code)

    @extend_schema(responses={200: OpenApiResponse(response=dict, description='Successful response')})
    def get(self, request, service_name, path):
        return self.proxy_request(request, service_name, path)

    @extend_schema(responses={200: OpenApiResponse(response=dict, description='Successful response')})
    def post(self, request, service_name, path):
        return self.proxy_request(request, service_name, path)

    @extend_schema(responses={200: OpenApiResponse(response=dict, description='Successful response')})
    def put(self, request, service_name, path):
        return self.proxy_request(request, service_name, path)

    @extend_schema(responses={200: OpenApiResponse(response=dict, description='Successful response')})
    def delete(self, request, service_name, path):
        return self.proxy_request(request, service_name, path)
