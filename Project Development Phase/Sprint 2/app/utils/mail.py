from trycourier import Courier
from keys import COURIER_AUTH_KEY

client = Courier(auth_token=COURIER_AUTH_KEY)

def send_mail(to_email, vlink):
  try:
    client.send_message(
      message={
        "to": {
          "email": to_email,
        },
        "template": "M9429AAXCA4ASHQ7QM52J1ACPWW5",
        "data": {
          "vlink": vlink,
        },
      }
    )
  except:
    pass
  finally:
    print(vlink)