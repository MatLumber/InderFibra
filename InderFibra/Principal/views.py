from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView
from Principal.models import Usuario
from datetime import date
from Administracion.models import Productos,Ventas
from django.contrib.auth import authenticate, login,logout
from Principal.forms import RegisterForm,LoginForm,ChangeDataUser
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Register.html'
    success_url = '/Inicio/'
    def form_valid(self, form):
        request = self.request
        login(request, form.save())
        return redirect('/Inicio/')
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'Login.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/Inicio/')
        return super().get(request, *args, **kwargs)
    def form_valid(self, form):
        request = self.request
        Usuario = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        remember_me = form.cleaned_data.get('remember_me')
        user = authenticate(request, username=Usuario, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                            request.session.set_expiry(0)
            if request.GET.get("next") == None or request.GET.get("next") == "":
                return redirect('/Inicio/')
            return redirect(request.GET.get("next"))
        return super(LoginView, self).form_invalid(form)


def index(request):
    return render(request,"index.html")

    
def productos(request):
    allproductos = Productos.objects.all()
    if request.method == "POST":
        now = date.today()
        producto = request.POST["producto"]
        getProducte = Productos.objects.get(id=producto)
        generarVenta = Ventas(Fecha=now,Cantidad=1,Producto=getProducte)
        generarVenta.save()
        getProducte.Stock = int(getProducte.Stock) - 1
        getProducte.Ventas = int(getProducte.Ventas) + 1
        getProducte.save()

    return render(request,"productos.html",{'productos':allproductos})
@login_required()
def Inicio(request):
    return render(request,"inicio.html",)
@login_required()
def LogoutView(request):
    logout(request)
    return render(request, "logout.html")
@login_required()
def perfil(request):
    instUser = Usuario.objects.get(id=request.user.id)
    form = ChangeDataUser(instance=instUser)
    if request.method == "POST":
        form = ChangeDataUser(request.POST,instance= instUser)
        if form.is_valid():
            form.save(commit=True)
    return render(request,"perfil.html",{'form':form})
