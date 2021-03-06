from django.shortcuts import render


# Pearl views

def handler404(request, exception):
    """
        Error Handler 404 - Page Not Found
    """
    return render(request, 'error_404.html', status=404)


def handler500(request):
    """
        Error Handler 500 - Internal Server Error
    """
    return render(request, 'error_500.html', status=500)
