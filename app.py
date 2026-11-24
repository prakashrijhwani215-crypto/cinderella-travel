import urllib.parse
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Cinderella Voyage WhatsApp
WHATSAPP_NUMBER = "221781840000"


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/submit-booking", methods=["POST"])
def submit_booking():
  full_name = request.form.get("full_name", "Client")
  service = request.form.get("service_type", "Flight Ticket")
  trip_type = request.form.get("trip_type", "One Way")
  dep = request.form.get("departure", "-")
  des = request.form.get("destination", "-")
  dep_date = request.form.get("departure_date", "-")
  ret_date = request.form.get("return_date", "N/A")
  pax = request.form.get("passengers", "1")

  # Return date sirf Round Trip ke case mein include karein
  if trip_type == "Round Trip" and ret_date:
    dates_info = f"Departure: {dep_date}\nReturn: {ret_date}"
  else:
    dates_info = f"Date: {dep_date}"

  msg = (
      f"✈️ *Cinderella Voyage Inquiry*\n"
      f"---------------------------\n"
      f"👤 *Name:* {full_name}\n"
      f"🛎️ *Service:* {service}\n"
      f"🔄 *Trip Type:* {trip_type}\n"
      f"🛫 *From:* {dep}\n"
      f"🛬 *To:* {des}\n"
      f"📅 *{dates_info}*\n"
      f"👥 *Passengers:* {pax}\n"
      f"---------------------------"
  )

  encoded = urllib.parse.quote(msg)
  return redirect(f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded}")


if __name__ == "__main__":
  # 0.0.0.0 se ye local network / mobile par accessible ho jata hai
  app.run(host="0.0.0.0", port=5000, debug=True)