from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('welcome')

	else:
		form = UserRegistrationForm()
	return render(request, 'account/signup.html', {'form' : form})
