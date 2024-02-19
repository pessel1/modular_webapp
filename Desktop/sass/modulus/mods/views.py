from django.shortcuts import render
from .models import Header, Sidebar, MainContent, Footer

# Create your views here.
def homepage(request):
    header = Header.objects.first()
    sidebar = Sidebar.objects.first()
    main_content = MainContent.objects.first()
    footer = Footer.objects.first()

    # Pass data to template
    context = {
      'header': header,
      'sidebar': sidebar,
      'main_content': main_content,
      'footer': footer,
    }

    # Render the template with data
    return render(request, 'homepage.html', context)