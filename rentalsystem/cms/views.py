from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Action,User



def user_login(request):
    if request.method == 'POST':
        # POST メソッドの場合、LoginView を呼び出してログイン処理を行う
        login_view = LoginView.as_view(
            template_name='login.html',
            authentication_form=CustomAuthenticationForm
        )
        return login_view(request)
    else:
        # GET メソッドの場合、ログインフォームを表示
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def borrow_items(request):
    # 'yes'なアイテムのみをフィルタリング
    available_items = Item.objects.filter(status='yes')
    return render(request, 'borrow_items.html', {'items': available_items})

def borrow_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    # 商品を借りる処理を実行...
    # 例：Action.objects.create(user=request.user, item=item, action_type='borrowed')
    return redirect('borrow')

@login_required
def return_items(request):
    # 正しいUserモデルのインスタンスを取得
    target_user = User.objects.get(username=request.user.username)

    # target_userを使って 'borrowed' としているアイテムをフィルタリング
    borrowed_items = Action.objects.filter(user=target_user, action_type='borrowed')
    return render(request, 'return_items.html', {'items': borrowed_items})
