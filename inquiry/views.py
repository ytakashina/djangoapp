from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from inquiry.models import Inquiry
from inquiry.forms import InquiryForm


# Create your views here.
def index(request):
    inquiry_list = Inquiry.objects.all().order_by('id')  # 値を取得
    return render(request, 'inquiry/index.html', {'inquiry_list': inquiry_list})


def add(request):
    inquiry = Inquiry()
    form = InquiryForm(instance=inquiry)
    return render(request, 'inquiry/add.html', {'form': form})
    # return render(request, 'inquiry/add.html', {'form': form, 'id': id})  # 更新を同じフォームで行う場合


def save(request):
    inquiry = Inquiry()
    form = InquiryForm(request.POST, instance=inquiry)
    if form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.save()
    else:
        raise ValueError("入力エラー{}".format(inquiry))
    return redirect('index')


def detail(request, id=None):
    inquiry = get_object_or_404(Inquiry, id=id)
    fields = ('user_name', 'email', 'sex', 'job', 'inquiry_text')
    inquiry_dict = {k: getattr(inquiry, k) for k in fields}
    return render(request, 'inquiry/detail.html', {'inquiry_items': inquiry_dict.items()})


def delete(request, id=None):
    inquiry = get_object_or_404(Inquiry, id=id)
    inquiry.delete()
    return redirect('index')
