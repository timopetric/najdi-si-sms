from najdisi_sms import SMSSender

sms = SMSSender("NAJDISI_USER", "NAJDISI_PASS")
sms.send("SLO_PHONE_NUMBER","MSG_TEXT")