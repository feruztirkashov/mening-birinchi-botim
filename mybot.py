import telebot
from telebot import types
import sqlite3
from telebot import apihelper # Proxy uchun kerak

# 1. PythonAnywhere uchun Proxy sozlamasi
# 2. Ma'lumotlar bazasini sozlash
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, first_name TEXT, username TEXT)')
conn.commit()

# 3. Bot sozlamalari
TOKEN = '8741548508:AAG6Z0QZgZPSn9ASu6Qklbl9yY0oiGz_5ec'
bot = telebot.TeleBot(TOKEN)
ADMIN_USERNAME = "FTU0927" # @ belgisiz yozgan ma'qul

# 1. DARSLAR RO'YXATI
KOMPYUTER_DARSLARI = {
    'comp_dars_1': {'id': 'BAACAgIAAxkBAAMJaftyA7hCqnAsobZ-otxnrnFH0pEAAhQNAAIEYvlJDhh-zVpQJ9Q7BA', 'nomi': '1-dars'},
    'comp_dars_2': {'id': 'BAACAgIAAxkBAAMLaftyKatD96nJfzV2ZmA497o_hG0AAjIJAAJyrUFIhtqIwGHzTeo7BA', 'nomi': '2-dars'},
    'comp_dars_3': {'id': 'BAACAgIAAxkBAAMNaftyR6XtcAQ3ia6LIfcjd1NRgFwAAuAKAAKfBFhIoaxGSmz8OBo7BA', 'nomi': '3-dars'},
    'comp_dars_4': {'id': 'BAACAgIAAxkBAAMPaftyZIeVd8JKCCdfYPn7Hgx5tOEAAuEKAAKfBFhIKYY2K9FUg0s7BA', 'nomi': '4-dars'},
    'comp_dars_5': {'id': 'BAACAgIAAxkBAAMLaftyKatD96nJfzV2ZmA497o_hG0AAjIJAAJyrUFIhtqIwGHzTeo7BA', 'nomi': '5-dars'},
    'comp_dars_6': {'id': 'BAACAgIAAxkBAAMTaftyn0JaPxfGcTMl9Q4gtiOTqOQAAuIKAAKfBFhIbda7qcEr2Ek7BA', 'nomi': '6-dars'},
    'comp_dars_7': {'id': 'BAACAgIAAxkBAAMVaftyuCXJ1HNmpZ6grHYjprbmu6wAAuQKAAKfBFhIO2crHWKmgsY7BA', 'nomi': '7-dars'},
    'comp_dars_8': {'id': 'BAACAgIAAxkBAAMXaftyz9xfA0vtk_DyL53snME-RR8AAqQLAAJzUKBJzgnbQPwaybs7BA', 'nomi': '8-dars'},
    'comp_dars_9': {'id': 'BAACAgIAAxkBAAMZafty7UJUZRHMyGACnZ5BKwuUPF8AAowMAAL_3GlI1YrOnpdLCR47BA', 'nomi': '9-dars'},
    'comp_dars_10': {'id': 'BAACAgIAAxkBAAMJaftyA7hCqnAsobZ-otxnrnFH0pEAAhQNAAIEYvlJDhh-zVpQJ9Q7BA', 'nomi': '10-dars'},
    'comp_dars_11': {'id': 'BAACAgIAAxkBAAMdaftzHBsUPMgtvWRPInsnRdjTkikAAqYLAAJzUKBJ8TOHvAABYVsrOwQ', 'nomi': '11-dars'},
    'comp_dars_12': {'id': 'BAACAgIAAxkBAAMfaftzMxWotdT4D_gzDJfLCAR3yAgAAo8NAALM6JFLtR9r_XCh20w7BA', 'nomi': '12-dars'}
}

# Diqqat: Bu yerda kalit so'zlarni comp_dars emas, off_dars deb o'zgartirdim (adashmaslik uchun)
MICROSOFT_OFFICE = {
    'off_dars_1': {'id': 'BAACAgIAAxkBAAMuaft3iFCz8JQUT7aIFox_5Yqr2XYAAgwJAALD8qFLASuiX7NyG_o7BA', 'nomi': '1-dars'},
    'off_dars_2': {'id': 'BAACAgIAAxkBAAMwaft3oHskDl4yA0O4hcuxg67QVwwAAh0IAALUYfBLrNpdBsIbEXI7BA', 'nomi': '2-dars'},
    'off_dars_3': {'id': 'BAACAgIAAxkBAAMyaft3ucU0foUhsMguurBRR7_E7QUAAh8IAAIeg3BI1Bjvx0Menys7BA', 'nomi': '3-dars'},
    'off_dars_4': {'id': 'BAACAgIAAxkBAAM0aft3zt9cjfuEcbB3zLEBo3WX3-QAAggKAAJgHoFIkxV0ctZcYto7BA', 'nomi': '4-dars'},
    'off_dars_5': {'id': 'BAACAgIAAxkBAAM2aft38H2sL_fPVmqU9D8CEYGcPFQAAi8KAAJgHoFIajIWsU6Rqro7BA', 'nomi': '5-dars'},
    'off_dars_6': {'id': 'BAACAgIAAxkBAAM4aft4B_dkR_8UQCEFOE3bPSFI64oAAisJAAJO-phIu_hc32thhek7BA', 'nomi': '6-dars'},
    'off_dars_7': {'id': 'BAACAgIAAxkBAAM6aft4IrIDA4cU_y43tkr6hYy1VMcAAtQKAAJcY6lI6BXEuwk99O07BA', 'nomi': '7-dars'},
    'off_dars_8': {'id': 'BAACAgIAAxkBAAM8aft4OkwbM01E6A62R8ntFsSMPWQAAocLAAJcY7lI4CLFxxMdYRU7BA', 'nomi': '8-dars'}
}
GRAFIK_DIZAYN = {
    'graf_dars_1': {'id': 'BAACAgIAAxkBAANSaft7Lq12GD_PSkBxkRV2n8GsPb8AAvMPAAJdCoFJZTkr05gSeAQ7BA', 'nomi': '1-dars:'},
    'graf_dars_2': {'id': 'BAACAgIAAxkBAANYaft7ft_3jKwKSZbk-jszFClVNjYAAvQPAAJdCoFJI4_zN6ReSX87BA', 'nomi': '2-dars'},
    'graf_dars_3': {'id': 'BAACAgIAAxkBAANaaft7mHuj9U3MaFW_Y3dj3rR4nvIAAvUPAAJdCoFJKg660HOSYGQ7BA', 'nomi': '3-dars'},
    'graf_dars_4': {'id': 'BAACAgIAAxkBAANfaft8IGQPiTfbI6mEgYW_zImkvbYAAvcPAAJdCoFJxPGwwTu63AQ7BA', 'nomi': '4-dars'},
    'graf_dars_5': {'id': 'BAACAgIAAxkBAANhaft8PJRiy5EPhhNgGDt8lc47e8IAAvgPAAJdCoFJk5x6M_9b_Fs7BA', 'nomi': '5-dars'},
    'graf_dars_6': {'id': 'BAACAgIAAxkBAANjaft8XU_C5prM6LvxOOZs6fSIhtEAAvkPAAJdCoFJEFyE1SCU3mg7BA', 'nomi': '6-dars'},
    'graf_dars_7': {'id': 'BAACAgIAAxkBAANoaft8xehJ8JV3Z5KellgXI643TMUAAvoPAAJdCoFJ4mf43l9tZ0o7BA', 'nomi': '7-dars'},
    'graf_dars_8': {'id': 'BAACAgIAAxkBAANqaft82hg1IHUBCJxGhdHgDtOFB8UAAvwPAAJdCoFJwQSd8g1-zXE7BA', 'nomi': '8-dars'}
}
DASTURLASH_DARSLARI = {
    'prog_dars_1': {'id': 'BAACAgIAAxkBAAOUafwhx7VIpD191sBTYsjTIKhQC-wAAvIPAAItYHFJwvDA0lCTxdM7BA', 'nomi': '1-dars'},
    'prog_dars_2': {'id': 'BAACAgIAAxkBAAOaafwiymHsowQTl7du1Zl-d6EpnbYAAvMPAAItYHFJ2TKPfG2lsYo7BA', 'nomi': '2-dars'},
    'prog_dars_3': {'id': 'BAACAgIAAxkBAAOcafwi-RkXQs-PzrUIgZv6_xF4PgAD9A8AAi1gcUluyir_RbV_CTsE', 'nomi': '3-dars'},
    'prog_dars_4': {'id': 'BAACAgIAAxkBAAOeafwjDnwfMNgpy_akVWq40Ta7bF4AAvUPAAItYHFJaCEb1oDHUL07BA', 'nomi': '4-dars'},
    'prog_dars_5': {'id': 'BAACAgIAAxkBAAOgafwjKJ2A9MaOvgZQNwjlaGcyR_IAAvYPAAItYHFJ9LqkrEn5WgU7BA', 'nomi': '5-dars'},
    'prog_dars_6': {'id': 'BAACAgIAAxkBAAOiafwjRiYlQP_V50jler5p0YikuyoAAvcPAAItYHFJeJIrnKBPLdc7BA', 'nomi': '6-dars'},
    'prog_dars_7': {'id': 'BAACAgIAAxkBAAOkafwjZlaIxzoD-gPOGAAB2B-gKSeSAAL5DwACLWBxSYi1Dxv4ReqWOwQ', 'nomi': '7-dars'},
    'prog_dars_8': {'id': 'BAACAgIAAxkBAAOmafwjfqhs9wOsgK7vRWdS8y8miDsAAvsPAAItYHFJ1hwMw8RSXWU7BA', 'nomi': '8-dars'}
}
MODELING_3D = {
    '3d_dars_1': {'id': 'BAACAgIAAxkBAAO2afwlpGlj9rlWFEf7x0nn49osRiYAAqMTAAKEc-lJpRBzlciwTrQ7BA', 'nomi': '3D 1-dars'},
    '3d_dars_2': {'id': 'BAACAgIAAxkBAAO4afwlukUicEPn-2A-aHBz2y-XfgsAAqQTAAKEc-lJuPo3h5-tRy87BA', 'nomi': '3D 2-dars'},
    '3d_dars_3': {'id': 'BAACAgIAAxkBAAO6afwl0Ln5sl3hNA-NWzwbXVbym_wAAqUTAAKEc-lJ8OeYmKWTY7M7BA', 'nomi': '3D 3-dars'},
    '3d_dars_4': {'id': 'BAACAgIAAxkBAAO8afwl5ue3_noBk0nW6MsLYGZFZ-4AAqYTAAKEc-lJ__kfEp_lf6U7BA', 'nomi': '3D 4-dars'},
    '3d_dars_5': {'id': 'BAACAgIAAxkBAAO-afwmBRCGbLAPuXQ-5r10VSppzXQAAqcTAAKEc-lJST6rpSxLmaI7BA', 'nomi': '3D 5-dars'},
    '3d_dars_6': {'id': 'BAACAgIAAxkBAAPAafwmH89kiz64DNqJcpSB1XZbYg0AAqgTAAKEc-lJYycBn2XHq0A7BA', 'nomi': '3D 6-dars'},
    '3d_dars_7': {'id': 'BAACAgIAAxkBAAPCafwmMrlX7uVdMnTvcSPKkM8jmGQAAqkTAAKEc-lJsjxHdkDWUnA7BA', 'nomi': '3D 7-dars'},
    '3d_dars_8': {'id': 'BAACAgIAAxkBAAPEafwmSAPkxXcIv95ma71MMKVtOg4AAqoTAAKEc-lJn0BC5Oq5gko7BA', 'nomi': '3D 8-dars'},
    '3d_dars_9': {'id': 'BAACAgIAAxkBAAPGafwmZqRnX-uFNGNqeVpCMsisVyUAAqsTAAKEc-lJWSHOyBvpaXA7BA', 'nomi': '3D 9-dars'},
    '3d_dars_10': {'id': 'BAACAgIAAxkBAAPIafwmkR8PA5Zv5Vvm-qpzhhDttvUAAq0TAAKEc-lJvF4Ih3moaXM7BA', 'nomi': '3D 10-dars'},
    '3d_dars_11': {'id': 'BAACAgIAAxkBAAPKafwmpi13rVmQqM2oN4qlrjSdqXMAAq8TAAKEc-lJiz6X8tSWMXc7BA', 'nomi': '3D 11-dars'},
    '3d_dars_12': {'id': 'BAACAgIAAxkBAAPMafwmuZzR2uI0-5SwA5mh9TltoXcAArETAAKEc-lJWB64aiigmcI7BA', 'nomi': '3D 12-dars'}
}
SMM_MARKETING = {
    'smm_dars_1': {'id': 'BAACAgIAAxkBAAPgafwrsg6IAAH9pp8mvapgKRYEfNNSAAIJEgAC7sfoSqJXO0XK8HxeOwQ', 'nomi': 'SMM 1-dars'},
    'smm_dars_2': {'id': 'BAACAgIAAxkBAAPiafwrzPFlD5RBAdavwA_F3O3NqAgAAgoSAALux-hKRS8MwM25-7A7BA', 'nomi': 'SMM 2-dars'},
    'smm_dars_3': {'id': 'BAACAgIAAxkBAAPkafwr4MSCRqNpUJP0j6ThpuYKwwsAAgsSAALux-hK6TOu9v60KT47BA', 'nomi': 'SMM 3-dars'},
    'smm_dars_4': {'id': 'BAACAgIAAxkBAAPmafwr_BfFBxgFPkMU-BJNPpirAWkAAhESAALux-hK0l9RZzCYLvM7BA', 'nomi': 'SMM 4-dars'},
    'smm_dars_5': {'id': 'BAACAgIAAxkBAAPoafwsGPvURzdaUEHPAtMZtyMVfJoAAhQSAALux-hKUMbx5IRKXN87BA', 'nomi': 'SMM 5-dars'},
    'smm_dars_6': {'id': 'BAACAgIAAxkBAAPqafwsOkouhY4xmYWpi2E0YQ8KCGQAAhISAALux-hKP0CXjm-vwmk7BA', 'nomi': 'SMM 6-dars'},
    'smm_dars_7': {'id': 'BAACAgIAAxkBAAPsafwsTbA9_jdm-_sdyN4N6QXQAAEgAAIWEgAC7sfoSkoKIY3nz27qOwQ', 'nomi': 'SMM 7-dars'},
    'smm_dars_8': {'id': 'BAACAgIAAxkBAAPuafwsYlC5UB99JpU3vBR3KB1o9VEAAhcSAALux-hKugnYJqUffZM7BA', 'nomi': 'SMM 8-dars'},
    'smm_dars_9': {'id': 'BAACAgIAAxkBAAPwafwscxDnMxIJWalnXFus2QpgwLYAAhgSAALux-hKPxZuQulLu207BA', 'nomi': 'SMM 9-dars'},
    'smm_dars_10': {'id': 'BAACAgIAAxkBAAPyafwsiM84LyDt2XszSAlm7mGK19QAAhkSAALux-hKn8e5wEqTKk07BA', 'nomi': 'SMM 10-dars'},
    'smm_dars_11': {'id': 'BAACAgIAAxkBAAP0afwsmrx80JZTjF1Zhsx-RtW7Gv0AAhkVAAJ0R5hKMS5eUuo5Tx07BA', 'nomi': 'SMM 11-dars'},
    'smm_dars_12': {'id': 'BAACAgIAAxkBAAP2afwsrT-wOX6uEA93IlIG5iT7VgEAAhoVAAJ0R5hKlkk328WF9HY7BA', 'nomi': 'SMM 12-dars'}
}
VIDEO_MONTAJ = {
    'montaj_dars_1': {'id': 'BAACAgIAAxkBAAIBAWn8MQb_6ISyxtBpSjKUQUV7qapHAALdCgACqfHYSOSSQLEMtVFCOwQ', 'nomi': 'Montaj 1-dars'},
    'montaj_dars_2': {'id': 'BAACAgIAAxkBAAIBA2n8MU4QfVrScagT23Bt4iCsW8GYAAI_CwACzjL4SJObY27NgKUMOwQ', 'nomi': 'Montaj 2-dars'},
    'montaj_dars_3': {'id': 'BAACAgIAAxkBAAIBBWn8MWPgGkf0cX92QwPyKxXBuqelAAK5CwACjXDgSNbfut5xbCuqOwQ', 'nomi': 'Montaj 3-dars'},
    'montaj_dars_4': {'id': 'BAACAgIAAxkBAAIBCGn8MXyHqy2iUOVMTugteRoORhq5AAK7CwACjXDgSNE-ZgrjsENaOwQ', 'nomi': 'Montaj 4-dars'},
    'montaj_dars_5': {'id': 'BAACAgIAAxkBAAIBC2n8MZGHU3G3ud9f8cMewqlk0VIlAAK6CwACjXDgSDD79PgIOAqrOwQ', 'nomi': 'Montaj 5-dars'},
    'montaj_dars_6': {'id': 'BAACAgIAAxkBAAIBDWn8MaasHnb3oTp9VikqhRKwfdZPAAJbCQAC3pgQSChLOz0U4-DXOwQ', 'nomi': 'Montaj 6-dars'},
    'montaj_dars_7': {'id': 'BAACAgIAAxkBAAIBD2n8MbtBSILSkmRF9up7c8MfmdzQAAK8CwACjXDgSO1KJ7-Z6c2WOwQ', 'nomi': 'Montaj 7-dars'},
    'montaj_dars_8': {'id': 'BAACAgIAAxkBAAIBEWn8Mc7E3tZx6LkNW_OWN6pjNr93AAK9CwACjXDgSGYWIh7sET-oOwQ', 'nomi': 'Montaj 8-dars'},
    'montaj_dars_9': {'id': 'BAACAgIAAxkBAAIBE2n8MeKZPqMeHB0k-facK5oKHrhBAAKvCAADgnFIlREjf1WElDI7BA', 'nomi': 'Montaj 9-dars'},
    'montaj_dars_10': {'id': 'BAACAgIAAxkBAAIBFWn8MfejYZlnI27UnIfOkJe6OljtAAKJCQACb97wSHEeywIxKhnQOwQ', 'nomi': 'Montaj 10-dars'}
}
CHET_TILLARI = {
    'lang_dars_1': {'id': 'BAACAgIAAxkBAAIBJmn8NMfhiXkUZzTbiuJe80qRJOxRAALkBgACzEH4SbZF8srlNtVZOwQ', 'nomi': 'turk tili 1-dars'},
    'lang_dars_2': {'id': 'BAACAgIAAxkBAAIBKGn8NN_kQcIBxFPdYE7IeW5i1YDKAAK4BQACmxKxSQ8LKUMFxal9OwQ', 'nomi': 'turk  tili 2-dars'},
    'lang_dars_3': {'id': 'BAACAgIAAxkBAAIBK2n8NRSKNQABkaNC74QEHGAvx8yOaQACoQQAAmpy-ElO1pLRI_IrDzsE', 'nomi': 'turk  tili 3-dars'},
    'lang_dars_4': {'id': 'BAACAgIAAxkBAAIBLWn8NSh32-vkiIlGj2qd3SkRETDNAALCBAACanL4SSg4T36NrjJAOwQ', 'nomi': 'turk  tili 4-dars'},
    'lang_dars_5': {'id': 'BAACAgIAAxkBAAIBL2n8NTrRMje-E1jLyTA33ypi_gk-AALoBgACzEH4SYl-qh4FrDeSOwQ', 'nomi': 'turk  tili 5-dars'},
    'lang_dars_6': {'id': 'BAACAgIAAxkBAAIBMWn8NU79W_TtWIrTG01htYzdDXpiAAJoBAACCKg4SzzDk6al2c48OwQ', 'nomi': 'turk  tili 6-dars'}
}



def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Kompyuter savodxonligi')
    btn2 = types.KeyboardButton('Microsoft Office darslari')
    btn3 = types.KeyboardButton('Grafik dizayn')
    btn4 = types.KeyboardButton('Dasturlash')
    btn5 = types.KeyboardButton('3D modeling')
    btn6 = types.KeyboardButton('SMM va marketing')
    btn7 = types.KeyboardButton('Video montaj')
    btn8 = types.KeyboardButton('Chet tillari')
    btn9 = types.KeyboardButton('☎️ Biz bilan bog\'lanish')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    return markup

def darslar_inline_menu(darslar_lugati):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for key, dars in darslar_lugati.items():
        markup.add(types.InlineKeyboardButton(dars['nomi'], callback_data=key))
    markup.add(types.InlineKeyboardButton('🏠 Bosh sahifa', callback_data='back_to_main'))
    return markup
def register_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    data = cursor.fetchone()
    if data is None:
        cursor.execute('INSERT INTO users (user_id, first_name, username) VALUES (?, ?, ?)', (user_id, first_name, username))
        conn.commit()
        print(f"Yangi foydalanuvchi qo'shildi: {first_name}")

@bot.message_handler(commands=['start'])
def start(message):
    register_user(message) # Ro'yxatga olish shu yerda chaqiriladi
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}! Bo'limni tanlang:", reply_markup=main_menu())


# --- MATNLI XABARLARNI TEKSHIRISH ---
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Kompyuter savodxonligi':
        bot.send_message(message.chat.id, "Kompyuter savodxonligi darslari:", 
                         reply_markup=darslar_inline_menu(KOMPYUTER_DARSLARI))
    
    elif message.text == 'Microsoft Office darslari': # MANA BU QISMNI QO'SHTIK
        bot.send_message(message.chat.id, "Microsoft Office darslari:", 
                         reply_markup=darslar_inline_menu(MICROSOFT_OFFICE))

    elif message.text == 'Grafik dizayn':
        bot.send_message(message.chat.id, "Grafik dizayn darslari:", 
                         reply_markup=darslar_inline_menu(GRAFIK_DIZAYN))

    elif message.text == 'Dasturlash':
        bot.send_message(message.chat.id, "Dasturlash darslari:", 
                         reply_markup=darslar_inline_menu(DASTURLASH_DARSLARI))

    elif message.text == '3D modeling':
        bot.send_message(message.chat.id, "3D modeling darslari:", 
                         reply_markup=darslar_inline_menu(MODELING_3D))
    elif message.text == 'SMM va marketing':
        bot.send_message(message.chat.id, "SMM va marketing darslari:", 
                         reply_markup=darslar_inline_menu(SMM_MARKETING))

    elif message.text == 'Video montaj':
        bot.send_message(message.chat.id, "Video montaj darslari:", 
                         reply_markup=darslar_inline_menu(VIDEO_MONTAJ))

    elif message.text == 'Chet tillari':
        bot.send_message(message.chat.id, "Chet tillari darslari:", 
                         reply_markup=darslar_inline_menu(CHET_TILLARI))

 
    elif message.text == '☎️ Biz bilan bog\'lanish':
        bot.send_message(message.chat.id, "Murojaat uchun admin:👨‍💻  @FTU0927")
    else:
        bot.send_message(message.chat.id, "Bu bo'limda darslar hozircha yo'q.")

# --- TUGMALAR BOSILGANDA ---
# --- TUGMALAR BOSILGANDA ---

@bot.message_handler(commands=['start'])
def start(message):
    register_user(message) # Ro'yxatga olish shu yerda chaqiriladi
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}! Bo'limni tanlang:", reply_markup=main_menu())

@bot.message_handler(commands=['statistika'])
def show_stat(message):
    if message.from_user.username == "@FTU0927": # O'z username'ingizni yozing
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        bot.send_message(message.chat.id, f"Botdagi umumiy foydalanuvchilar soni: {count} ta")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    # Bu yerda hamma lug'atlarni bitta joyga yig'ib olamiz (agar sizda shunday bo'lsa)
    all_d = {**KOMPYUTER_DARSLARI, **MICROSOFT_OFFICE, **GRAFIK_DIZAYN, **DASTURLASH_DARSLARI, **MODELING_3D, **SMM_MARKETING, **VIDEO_MONTAJ, **CHET_TILLARI}
    
    # Hamma videolar tagida chiqadigan bir xil matn
    caption_text = "🎓 Bilim olish botiga xush kelibsiz!\n\n👨‍💻 Muallif: @FTU0927\n🚀 Do'stlaringizga ham ulashing! https://t.me/bepuldars2026_bot "

    if call.data in all_d:
        dars = all_d[call.data]
        bot.send_video(
            call.message.chat.id, 
            dars['id'], 
            caption=caption_text # Mana shu joyi matnni qo'shib beradi
        )
    
    elif call.data == 'back_to_main':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Asosiy menyuga qaytdingiz:", reply_markup=main_menu())


    elif call.data in MODELING_3D:
        dars = MODELING_3D[call.data]
        bot.send_video(call.message.chat.id, dars['id'], caption=dars['nomi'])
        
    elif call.data in SMM_MARKETING:
        dars = SMM_MARKETING[call.data]
        bot.send_video(call.message.chat.id, dars['id'], caption=dars['nomi'])

    elif call.data in VIDEO_MONTAJ:
        dars = VIDEO_MONTAJ[call.data]
        bot.send_video(call.message.chat.id, dars['id'], caption=dars['nomi'])

    elif call.data in CHET_TILLARI:
        dars = CHET_TILLARI[call.data]
        bot.send_video(call.message.chat.id, dars['id'], caption=dars['nomi'])

@bot.message_handler(content_types=['video'])
def get_id(message):
    bot.reply_to(message, f"Video ID: `{message.video.file_id}`")

print("Bot ishga tushdi...")
bot.polling(none_stop=True)
