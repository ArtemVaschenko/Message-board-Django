from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from app1.forms import AddPostForm, RegisterUserForm
from app1.models import Item


class HomePageView(ListView):
    items = Item.objects.all()
    model = Item
    template_name = 'home_page.html'
    context_object_name = 'items'


class AddItemPageView(CreateView):
    form_class = AddPostForm
    template_name = 'add_item.html'
    success_url = reverse_lazy('home')


class ShowItemPage(DetailView):
    model = Item
    template_name = 'item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'item'


class RegisterUser(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    model = User
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class MyPage(DetailView):
    model = User
    template_name = 'my_page.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'
    k = Item.objects.filter(owner=User.username)
    # user_items = Item.objects.get(owner=User.id)
    # id = User.pk
    # def get(self, request, user_id):
    #     user = get_object_or_404(User, pk=user_id)
    #     context = {
    #         'user': user,
    #     }
    #     return render(request, 'my_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
