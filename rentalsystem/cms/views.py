from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.shortcuts import render

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
