from flask import Flask, jsonify, request
import os

app = Flask(__name__)

iphones_for_rent = [
    {"id": 1, "model": "iPhone 13 Pro", "color": "Graphite", "storage": "256GB", "price_per_day": 100000, "is_available": True},
    {"id": 2, "model": "iPhone 14", "color": "Midnight", "storage": "128GB", "price_per_day": 85000, "is_available": True},
    {"id": 3, "model": "iPhone 15 Pro Max", "color": "Natural Titanium", "storage": "512GB", "price_per_day": 150000, "is_available": True},
    {"id": 4, "model": "iPhone SE (2022)", "color": "Starlight", "storage": "64GB", "price_per_day": 60000, "is_available": False} # Contoh tidak tersedia
]

@app.route('/')
def home():
    return "Selamat datang di API Sewa iPhone! Kunjungi /api/iphones untuk daftar iPhone."

@app.route('/api/iphones', methods=['GET'])
def get_iphones():
    available_only = request.args.get('available', 'false').lower() == 'true'
    
    if available_only:
        filtered_iphones = [iphone for iphone in iphones_for_rent if iphone['is_available']]
        return jsonify({
            "status": "success",
            "message": "Daftar iPhone yang tersedia untuk disewa",
            "iphones": filtered_iphones,
            "count": len(filtered_iphones)
        })
    else:
        return jsonify({
            "status": "success",
            "message": "Daftar semua iPhone",
            "iphones": iphones_for_rent,
            "count": len(iphones_for_rent)
        })

@app.route('/api/rent/<int:iphone_id>', methods=['POST'])
def rent_iphone(iphone_id):
    for iphone in iphones_for_rent:
        if iphone['id'] == iphone_id:
            if iphone['is_available']:
                iphone['is_available'] = False # Ubah status menjadi tidak tersedia
                return jsonify({
                    "status": "success",
                    "message": f"iPhone {iphone['model']} (ID: {iphone_id}) berhasil disewa.",
                    "rented_iphone": iphone
                }), 200 # HTTP 200 OK
            else:
                return jsonify({
                    "status": "error",
                    "message": f"iPhone {iphone['model']} (ID: {iphone_id}) saat ini tidak tersedia untuk disewa."
                }), 400 # HTTP 400 Bad Request (sudah disewa)
    
    return jsonify({
        "status": "error",
        "message": f"iPhone dengan ID {iphone_id} tidak ditemukan."
    }), 404 # HTTP 404 Not Found

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5000))
    app.run(debug=True, host='0.0.0.0', port=port)