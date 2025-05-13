from flask import Flask, render_template, send_from_directory
from datetime import datetime
import os

app = Flask(__name__, static_folder='D:\\anniversary_surprise\\static')

# ====== PERSONALIZATION ======
ANNIVERSARY_DATE = datetime(2024, 4, 1)
HER_NAME = "GIRL"
YOUR_NAME = "BOY"

# Reasons you love her
REASONS = [
    "The way your eyes light up when you talk about something you love",
    "The comfort of your hand in mine, like everything is going to be okay",
    "How your voice instantly calms me, no matter how bad my day has been",
    "The way you challenge me to grow while still loving me exactly as I am",
    "The way you look at me like I’m the only person in the world",
    "How being with you feels like coming home - even when we’re miles apart",
]

# Love letter
LOVE_LETTER = f"""
To My Love,

From the moment we first met, something just felt like our souls already knew each other. I still remember that first time we sat together over a simple cup of tea, talking for hours like the rest of the world had disappeared. Since then, every moment with you has felt like both a heartbeat and a lifetime.

I often find myself thinking about the laughter we’ve shared, the quiet moments in between, and the way you held my hand like it was the only thing that mattered. In those little moments, I realized I was falling in love with you completely, effortlessly, and deeply.

I want you to know that I’m here for you, always. I promise to:
 1. Make you smile, even when the days are heavy.
 2. Hold you close when you feel the weight of the world.
 3. Choose you, over and over, every day—with my whole heart.

Life won’t always be easy, but no matter what it brings, you’ll never face it alone. I’ll be by your side—today, tomorrow, and for all the days to come.

With all my love,  
Your's (ABC) 🧸
"""

# Route for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.static_folder),
        'us.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# Home route
@app.route('/')
def home():
    days_together = (datetime.now() - ANNIVERSARY_DATE).days
    return render_template(
        'responsive_home.html',
        days=days_together,
        her_name=HER_NAME,
        your_name=YOUR_NAME
    )

# Surprise route
@app.route('/surprise')
def surprise():
    return render_template(
        'responsive_surprise.html',
        reasons=REASONS,
        letter=LOVE_LETTER,
        anniversary=ANNIVERSARY_DATE.strftime("%B %d, %Y"),
        her_name=HER_NAME,
        your_name=YOUR_NAME
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
