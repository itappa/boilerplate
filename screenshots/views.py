from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import MultipleImageForm
from .models import Screenshot, Tag


class ItemListView(LoginRequiredMixin, ListView):
    template_name = "recipes/index.html"
    model = Screenshot
    context_object_name = "images"
    paginate_by = 30


def upload(request):
    if request.method == "POST":
        form = MultipleImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist("image")
            category = form.cleaned_data.get("category")
            tags = form.cleaned_data.get("tags")

            images = sorted(images, key=lambda f: f.name.lower())
            for index, image in enumerate(images):
                photo = Screenshot(image=image, category=category, order=index)
                photo.save()

                if tags:
                    if not hasattr(tags, "__iter__") or isinstance(tags, Tag):
                        tags = [tags]
                    photo.tags.set(tags)

            return redirect("recipes:index")
    else:
        form = MultipleImageForm()

    return render(request, "recipes/upload.html", {"form": form})
