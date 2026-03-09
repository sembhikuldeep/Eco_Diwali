from flask import Flask, render_template
import random

app = Flask(__name__)

tips = {
    "Diyas": "Clean and reuse diyas as home decor or plant holders. You can paint them to look new for next Diwali!",
    "Fireworks": "Do not burn leftover fireworks. Collect paper and metal parts separately and send them for recycling.",
    "Candles": "Melt leftover wax and pour into molds with new wicks to make fresh candles.",
    "Decorations": "Reuse lights and flowers for festive home decor. Compost natural flowers instead of throwing them away.",
    "Plastics": "Avoid single-use plastic decorations. Clean and donate reusable ones to local NGOs.",
    "Clothes": "Donate old festive clothes to charity or use them for DIY crafts like cushion covers or gift wraps.",
    "Gift wrapping": "Reuse gift bags, boxes, and ribbons. Choose paper or cloth wrapping instead of plastic.",
    "Sweets boxes": "Clean and reuse sweet boxes for storage or organize stationery and jewelry.",
    "Oil": "After using oil for diyas, do not pour it down the drain. Collect and reuse it for household cleaning.",
    "Electronics": "Recycle old decorative lights or damaged electronics at e-waste collection centers.",
    "Flowers": "Dry used flowers and make natural potpourri or organic colors for future festivals.",
    "Cards": "Cut and reuse old greeting cards for making bookmarks or DIY gift tags.",
    "Food waste": "Avoid excess cooking. Share leftover food with neighbors or donate to local food banks.",
    "Paper": "Recycle old newspapers and cardboard used for decorations or gift wrapping.",
    "Metal items": "Collect broken metal diyas or decorative items and give them to metal scrap recyclers."
}

@app.route("/")
def home():
    item = random.choice(list(tips.keys()))
    advice = tips[item]
    return render_template("index.html", item=item, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)