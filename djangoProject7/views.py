from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 주소 요청하나당 함수를 하나 호출하는 방식
# 호출되는 함수는 반드시 입력값으로 request객체를 가져야 함.
# request객체는 클라이언트가 입력한 데이터를 서버에서 받아주는 역할의 부품
def start(request):
    print('SHOP01 주소로 요청했을 때 START호출됨.')
    return HttpResponse("START함수 호출됨.!!!!")  # alt+enter

def index(request):
    return HttpResponse("<body bgcolor=yellow>장고 첫 페이지입니다.</body><br>" +
                        "<a href=http://www.naver.com>네이버로 이동</a><br>" +
                        "<a href=http://www.daum.net>다음으로 이동</a><br>" +
                        "<a href=admin>관리자모드로 이동</a><br>" +
                        "<a href=shop01>shop01시작 페이지로</a><br>" +
                        "<a href=shop01/index1>shop01/index1페이지로</a><br>" +
                        "<a href=shop01/index2>shop01/index2페이지로</a><br>" +
                        "<a href=shop01/index0>shop01/index0페이지로</a><br>" +
                        "<a href=shop01/index3>shop01/index3(css)페이지로</a><br>" +
                        "<a href=shop01/index4>shop01/index4(js)페이지로</a><br>" +
                        "<a href=shop01/index5>shop01/index5(js2)페이지로</a><br>" +
                        "<a href=shop01/index6>shop01/index6(js3)페이지로</a><br>" +
                        "<a href=shop01/index7>shop01/index7(js4-함수)페이지로</a><br>" +
                        "<a href=shop01/index8>shop01/index8(js4-함수2)페이지로</a><br>" +
                        "<a href=shop01/index9>shop01/index9(js4-함수3)페이지로</a><br>" +
                        "<a href=shop01/index10>shop01/index10(js4-함수4)페이지로</a><br>" +
                        "<a href=shop01/index11>shop11/index11(jquery1)페이지로</a><br>" +
                        "<a href=shop01/index12>shop11/index12(jquery2)페이지로</a><br>" +
                        "<a href=shop01/index13>shop11/index13(결제)페이지로</a><br>" +
                        "<a href=shop01/index14>shop11/index14(map)페이지로</a><br>" +
                        "<a href=shop01/index15>shop11/index15(구글차트)페이지로</a><br>"
                        )

def index1(request):
    return HttpResponse("<body bgcolor=pink>장고 index1 페이지입니다.</body>")

def index2(request):
    return HttpResponse("<font color=red>장고</font> index2 페이지입니다.")

def index0(request):
    return render(request, 'shop01/index.html')

def index3(request):
    return render(request, 'shop01/index3.html')

def index4(request):
    return render(request, 'shop01/index4.html')

def index5(request):
    return render(request, 'shop01/index5.html')

# views.py는 클라이언트의 요청과 서버의 응답을 컨트롤러 역할!!
def index6(request):
    return render(request, 'shop01/index6.html')

def index7(request):
    return render(request, 'shop01/index7.html')

def index8(request):
    return render(request, 'shop01/index8.html')

def index9(request):
    return render(request, 'shop01/index9.html')

def index10(request):
    return render(request, 'shop01/index10.html')

def index11(request):
    return render(request, 'shop01/index11.html')

def index12(request):
    return render(request, 'shop01/index12.html')

def index13(request):
    return render(request, 'shop01/index13.html')

def index14(request):
    return render(request, 'shop01/index14.html')


def index15(request):
    return render(request, 'shop01/index15.html')