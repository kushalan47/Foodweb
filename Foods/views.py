from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import Food
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signin.html'
    success_url = reverse_lazy('food_list')

def food_list(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successful!')
            return redirect('food_list')
        else:
            messages.success(request, 'Login Failed')
    else:
        if request.user.is_authenticated:
            food = Food.objects.filter(author=request.user)
        else:
            food = Food.objects.all()
        return render(request,'index.html',{'food':food})

def food_detail(request,id):
    food = Food.objects.get(pk=id)
    return render(request,'detail.html',{'food':food})


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Food
    template_name = 'create.html'
    fields = ['title', 'image','desc']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        messages.success(
            self.request, 'Your Food has been successfully created!')
        print('saved')
        return redirect('food_list')

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = 'update.html'
    fields = ['title', 'image','desc']

    def form_valid(self, form):
        instance = form.save()
        messages.success(   
            self.request, 'Your Food has been successfully updated!')
        return redirect('food_list')

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your Food has been successfully deleted!')
        return super().delete(self, request, *args, **kwargs)

# def search(request):
#     if request.POST:
#         search_term = request.POST['search_term']
#         search_results = Food.objects.filter(
#             Q(title__icontains=search_term) |
#             Q(desc__icontains=search_term)
#         )
#         context = {
#             'search_term': search_term,
#             'foods': search_results.filter(author=request.user)
#         }
#         return render(request, 'search.html', context)
#     else:
#         return redirect('food_list')