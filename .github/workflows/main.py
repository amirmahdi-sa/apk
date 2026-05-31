import requests
import flet as ft
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main(page: ft.Page):
    # تنظیمات صفحه برای پشتیبانی بهتر از راست‌به‌چین (فارسی)
    page.title = "هواشناسی هوشمند فارسی"
    page.bgcolor = "#1e1e2e"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_weather(e):
        shahr = input_shahr.value
        if not shahr:
            matn_natije.value = "لطفاً ابتدا اسم شهر را بنویسید!"
            page.update()
            return

        api_key = "60738a9d12a1498b3fc8fcf52cc6073c"

        # با اضافه کردن &lang=fa کاری کردیم که سرور زبان فارسی را بفهمد
        url = f"https://api.openweathermap.org/data/2.5/weather?q={shahr}&appid={api_key}&units=metric&lang=fa"

        try:
            pasokh = requests.get(url)

            if pasokh.status_code != 200:
                matn_natije.value = "خطا! یا فیلترشکن مسدود است یا اسم شهر را اشتباه نوشتید."
                icon_hava.src = ""  # حذف آیکون قبلی در صورت خطا
                page.update()
                return

            data = pasokh.json()

            # استخراج اطلاعات از کشوهای جی‌سان
            dama = data["main"]["temp"]
            rutoobat = data["main"]["humidity"]
            # وضعیت هوا به فارسی (مثلا: آسمان صاف)
            وضعیت = data["weather"][0]["description"]
            کد_آیکون = data["weather"][0]["icon"]  # گرفتن کد تصویر هوا از سرور

            # نمایش اطلاعات به فارسی
            matn_natije.value = f"🏙 شهر: {shahr}\n🌡 دما: {dama} درجه سانتی‌گراد\n💧 رطوبت: {rutoobat}%\n☁️ وضعیت: {وضعیت}"

            # تغییر عکس آیکون متناسب با آب و هوای فعلی آن شهر
            icon_hava.src = f"https://openweathermap.org/img/wn/{کد_آیکون}@2x.png"

        except Exception as error:
            matn_natije.value = "خطا در اتصال! اینترنت یا فیلترشکن را بررسی کنید."
            print(error)

        page.update()

    # --- ظاهر فارسی برنامه ---
    input_shahr = ft.TextField(
        label="نام شهر (فارسی یا انگلیسی)",
        hint_text="مثلاً: تهران یا اصفهان",
        width=280,
        text_align=ft.TextAlign.RIGHT  # راست‌چین کردن متن ورودی
    )

    dokme = ft.ElevatedButton(
        content="دریافت وضعیت آب و هوا", on_click=get_weather)

    # ابزاری برای نمایش عکس آیکون هوا
    icon_hava = ft.Image(src="", width=100, height=100)

    matn_natije = ft.Text(value="", size=18, color="white",
                          text_align=ft.TextAlign.RIGHT)

    page.add(
        ft.Divider(height=10, color="transparent"),
        ft.Text("سامانه هواشناسی هوشمند فارسی", size=22,
                color="cyan", weight=ft.FontWeight.BOLD),
        ft.Divider(height=10, color="transparent"),
        input_shahr,
        dokme,
        icon_hava,  # اضافه شدن آیکون به صفحه
        matn_natije
    )


ft.app(target=main)
