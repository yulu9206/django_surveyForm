from django.shortcuts import render, redirect
def index(request):
	return render(request, 'survey_form/index.html')
def submit(request):
	if request.session.get('count') == None:
		request.session['count'] = 1
	else:
		request.session['count'] += 1
	
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')
def result(request):
	return render(request, 'survey_form/result.html')