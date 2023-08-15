from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Item, Action
from django.shortcuts import get_object_or_404, redirect,render
from django.utils import timezone  # 追加: タイムゾーンを利用するために必要
from django.contrib.auth.models import User


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
    # 'avaliable'なアイテムのみをフィルタリング
    available_items = Item.objects.filter(status='available')
    return render(request, 'borrow_items.html', {'items': available_items})


@login_required
def borrow_item(request, item_id):
    # 'available' なステータスを持つ指定されたIDのアイテムを取得
    item = get_object_or_404(Item, pk=item_id, status='available')

    # アクションを作成する前に現在のタイムスタンプを取得
    current_timestamp = timezone.now()

    # Actionオブジェクトを作成
    Action.objects.create(user=request.user, item=item, action_type='borrowed',
                          timestamp=current_timestamp)  # タイムスタンプを記録

    # アイテムのステータスを 'rented' に変更
    item.status = 'rented'
    item.save()

    return redirect('borrow_items')  # 修正: 正しいリダイレクト先へ

@login_required
def return_items(request):
    # 正しいUserモデルのインスタンスを取得
    target_user = User.objects.get(username=request.user.username)

    # target_userを使って 'borrowed' としているアイテムをフィルタリング
    borrowed_items = Action.objects.filter(user=target_user, action_type='borrowed')
    return render(request, 'return_items.html', {'items': borrowed_items})

@login_required
def return_item(request, action_id):
    action = get_object_or_404(Action, pk=action_id, user=request.user, action_type='borrowed')

    # アクションのステータスを 'returned' に変更
    action.action_type = 'returned'
    action.timestamp = timezone.now()
    action.save()

    # アイテムのステータスを 'available' に変更
    item = action.item
    item.status = 'available'
    item.save()

    return redirect('return_items')  # 返却後、再度借りているアイテムのリストにリダイレクト
