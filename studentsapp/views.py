from django.shortcuts import render, redirect
from studentsapp.models import student
from studentsapp.forms import PostForm

def listone(request): 
	try: 
		unit = student.objects.get(cName="李采茜") #讀取一筆資料
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def listall(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())
	
def index(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "index.html", locals())		

def post(request):
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
	else:
		mess="表單資料尚未送出!"	
	return render(request, "post.html", locals())
	
def post1(request):  #新增資料，資料不作驗證
	if request.method == "POST":	  #如果是以POST方式才處理
		cName = request.POST['cName'] #取得表單輸入資料
		cSex =  request.POST['cSex']
		cBirthday =  request.POST['cBirthday']
		cEmail = request.POST['cEmail']
		cPhone =  request.POST['cPhone']
		cAddr =  request.POST['cAddr']
		#新增一筆記錄
		unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
		unit.save()  #寫入資料庫
		return redirect('/index/')	
	else:
		message = '請輸入資料(資料不作驗證)'
	return render(request, "post1.html", locals())	
	
def post2(request):  #新增資料，資料必須驗證
	if request.method == "POST":  #如果是以POST方式才處理
		postform = PostForm(request.POST)  #建立forms物件
		if postform.is_valid():			#通過forms驗證
			cName = postform.cleaned_data['cName'] #取得表單輸入資料
			cSex =  postform.cleaned_data['cSex']
			cBirthday =  postform.cleaned_data['cBirthday']
			cEmail = postform.cleaned_data['cEmail']
			cPhone =  postform.cleaned_data['cPhone']
			cAddr =  postform.cleaned_data['cAddr']
			#新增一筆記錄
			unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
			unit.save()  #寫入資料庫
			message = '已儲存...'
			return redirect('/index/')	
		else:
			message = '驗證碼錯誤！'	
	else:
		message = '姓名、性別、生日必須輸入！'
		postform = PostForm()
	return render(request, "post2.html", locals())		
		
def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			unit = student.objects.get(id=id)  
			unit.delete()
			return redirect('/index/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	
	
def edit(request,id=None,mode=None):  
	if mode == "edit":  # 由 edit.html 按 submit
		unit = student.objects.get(id=id)  #取得要修改的資料記錄	
		unit.cName=request.GET['cName']
		unit.cSex=request.GET['cSex']
		unit.cBirthday=request.GET['cBirthday']
		unit.cEmail=request.GET['cEmail']
		unit.cPhone=request.GET['cPhone']
		unit.cAddr=request.GET['cAddr']		
		unit.save()  #寫入資料庫
		message = '已修改...'
		return redirect('/index/')	
	else: # 由網址列
		try:
			unit = student.objects.get(id=id)  #取得要修改的資料記錄
			strdate=str(unit.cBirthday)
			strdate2=strdate.replace("年","-")
			strdate2=strdate.replace("月","-")
			strdate2=strdate.replace("日","-")
			unit.cBirthday = strdate2
		except:
			message = "此 id不存在！"	
		return render(request, "edit.html", locals())	
		
def edit2(request,id=None,mode=None):
    if mode == "load":  # 由 index.html 按 編輯二 鈕
      unit = student.objects.get(id=id)  #取得要修改的資料記
      strdate=str(unit.cBirthday)
      strdate2=strdate.replace("年","-")
      strdate2=strdate.replace("月","-")
      strdate2=strdate.replace("日","-")
      unit.cBirthday = strdate2		
      return render(request, "edit2.html", locals())
    elif mode == "save": # 由 edit2.html 按 submit		
      unit = student.objects.get(id=id)  #取得要修改的資料記錄	
      unit.cName=request.POST['cName']
      unit.cSex=request.POST['cSex']
      unit.cBirthday=request.POST['cBirthday']
      unit.cEmail=request.POST['cEmail']
      unit.cPhone=request.POST['cPhone']
      unit.cAddr=request.POST['cAddr']		
      unit.save()  #寫入資料庫
      message = '已修改...'
      return redirect('/index/')
	  
def postform(request):  #新增資料，資料必須驗證
	postform = PostForm()  #建立PostForm物件
	return render(request, "postform.html", locals())		  
