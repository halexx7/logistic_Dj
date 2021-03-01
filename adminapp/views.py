from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from adminapp.forms import ProductCategoryEditForm, ProductEditForm, ShopUserAdminEditForm
from authnapp.forms import ShopUserRegisterForm
from authnapp.models import ShopUser
from mainapp.models import Services, ServicesCategory


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    response = redirect("admin:users")
    return response


class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = "adminapp/users.html"


def user_create(request):
    title = "пользователи/создание"

    if request.method == "POST":
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("admin:users"))
    else:
        user_form = ShopUserRegisterForm()

    content = {"title": title, "update_form": user_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


def user_update(request, pk):
    title = "пользователи/редактирование"

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:user_update", args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {"title": title, "update_form": edit_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


def user_delete(request, pk):
    title = "пользователи/удаление"

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == "POST":
        # user.delete()
        # Instead delete we will set users inactive
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("admin:users"))

    content = {"title": title, "user_to_delete": user, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_delete.html", content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = "админка/категории"
    categories_list = ServicesCategory.objects.all()
    content = {"title": title, "objects": categories_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/categories.html", content)


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ServicesCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ServicesCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context["title"] = "категории/редактирование"
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class ProductCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ServicesCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("admin:categories")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = "админка/продукт"
    category = get_object_or_404(ServicesCategory, pk=pk)
    products_list = Services.objects.filter(category__pk=pk).order_by("name")
    content = {"title": title, "category": category, "objects": products_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/products.html", content)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Services
    template_name = "adminapp/product_update.html"
    success_url = reverse_lazy("admin:products")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context["title"] = "продукт/создание"
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Services
    template_name = "adminapp/product_read.html"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    template_name = "adminapp/product_update.html"
    success_url = reverse_lazy("admin:product_update")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context["title"] = "продукт/редактирование"
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = "adminapp/product_delete.html"
    success_url = reverse_lazy("admin:products")

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context["title"] = "продукт/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
