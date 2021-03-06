from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
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


class UsersCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("admin:users")
    # fields = "__all__"
    form_class = ShopUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/создание"
        return context


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("admin:user_update")
    form_class = ShopUserAdminEditForm

    def get_context_data(self, **kwargs):
        context = super(UsersUpdateView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/редактирование"
        return context


class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete.html"
    success_url = reverse_lazy("admin:users")

    def get_context_data(self, **kwargs):
        context = super(UsersDeleteView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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
    form_class = ProductCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context["title"] = "категории/редактирование"
        return context

    def form_valid(self, form):
        if "discount" in form.cleaned_data:
            discount = form.cleaned_data["discount"]
            if discount:
                # print(f"применяется скидка {discount}% к товарам категории {self.object.name}")
                self.object.services_set.update(price=F("price") * (1 - discount / 100))
                db_profile_by_type(self.__class__, "UPDATE", connection.queries)

        return super().form_valid(form)


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
    form_class = ProductEditForm

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
    form_class = ProductEditForm

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


from django.db import connection
from django.db.models.signals import pre_save
from django.dispatch import receiver


def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x["sql"], queries))
    print(f"db_profile {type} for {prefix}:")
    [print(query["sql"]) for query in update_queries]


@receiver(pre_save, sender=ServicesCategory)
def service_is_active_update_servicecategory_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.services_set.update(is_active=True)
        else:
            instance.services_set.update(is_active=False)

        # db_profile_by_type(sender, 'UPDATE', connection.queries)
