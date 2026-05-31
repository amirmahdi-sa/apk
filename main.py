import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import flet as ft
import requests

def main(page: ft.Page):
    page.title = "اپلیکیشن آب و هوای هوشمند"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title_text = ft.Text("سامانه هواشناسی", size=28, weight=ft.FontWeight.BOLD, color="blueaccent")
    
    city_input = ft.TextField(label="نام شهر را بنویسید ", width=300, text_align=ft.TextAlign.CENTER)
    
    result_temp = ft.Text("", size=40, weight=ft.FontWeight.BOLD, color="amber")
    result_desc = ft.Text("", size=20, color="white")

    # تابعی که وقتی روی دکمه کلیک شد اجرا می‌شود
    def get_weather(e):
        city = city_input.value
        if not city:
            result_desc.value = "لطفاً نام شهر را وارد کنید!"
            page.update()
            return
        
        # آدرس API رایگان و بدون فیلتر (OpenWeatherMap) همراه با یک کلید عمومی تست
        api_key = "b1b15e88fa797225412429c1c50c122a1" # این یک کلید موقت برای تست توئه
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            # درخواست فرستادن به سایت خارجی
            response = requests.get(url).json()
            
            # استخراج دما و وضعیت هوا از داخل پاسخ سایت
            temp = response["main"]["temp"]
            desc = response["weather"][0]["main"]
            
            # آپدیت کردن متن‌های روی صفحه
            result_temp.value = f"{temp}°C"
            result_desc.value = f"وضعیت هوا: {desc}"
            
        except:
            result_desc.value = "خطا! نام شهر را درست وارد کرده‌اید؟ یا اینترنت وصل است؟"
            result_temp.value = ""
            
        # بروزرسانی صفحه برای نمایش تغییرات
        page.update()

    # دکمه بررسی وضعیت هوا
    check_button = ft.ElevatedButton("بررسی وضعیت آب و هوا", on_click=get_weather, bgcolor="blue", color="white")

    # اضافه کردن همه المان‌ها به صفحه به ترتیب
    page.add(
        title_text,
        ft.Divider(height=20, color="transparent"), # یک فاصله خالی
        city_input,
        check_button,
        ft.Divider(height=30, color="transparent"),
        result_temp,
        result_desc
    )

if __name__ == "__main__":
    ft.app(target=main)
