from django.contrib.auth.forms import UserCreationForm

# UserCreationForm을 상속받아서 update.html의 Form 내부를 재구성
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Username의 칸을 비활성화 하도록 재구성하는 코드
        self.fields['username'].disabled = True