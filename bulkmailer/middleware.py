from django.http import HttpResponseForbidden

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the User-Agent header
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # Get the Referrer header
        referrer = request.META.get('HTTP_REFERER', '')

        # Determine if the request is likely direct access
        is_direct_access = not referrer or user_agent.lower() == 'python-requests/2.26.0'

        # Log request details
        print("Request from:", request.META.get('REMOTE_ADDR'))
        print("Request method:", request.method)
        print("Request path:", request.path)
        print("Direct access:", is_direct_access)
        
        if is_direct_access:
            return HttpResponseForbidden("Direct access is not allowed.")
        
        # Call the next middleware or view
        response = self.get_response(request)

        return response
