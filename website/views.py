from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):  # get context dataという関数を定義 
        ctxt = super().get_context_data()
        ctxt["username"] = "" 
        return ctxt
    
class AboutView(TemplateView):
    template_name = "about.html"