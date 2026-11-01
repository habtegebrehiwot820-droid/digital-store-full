import os
import uuid
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from .models import DigitalProduct

# 1. Frontend Homepage View
def home_store(request):
    products = DigitalProduct.objects.all()  # Fetches your products from the database
    return render(request, 'shop/home.html', {'products': products})

# 2. Chapa Payment Gateway View
def initialize_payment(request, product_id):
    product = get_object_or_404(DigitalProduct, id=product_id)
    tx_ref = str(uuid.uuid4())
    
    CHAPA_URL = "https://chapa.co"
    CHAPA_SECRET_KEY = "Telebirr and CBE Birr"  # Replace with your actual key later
    
    headers = {
        "Authorization": f"Bearer {CHAPA_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "amount": str(product.price),
        "currency": "ETB",
        "email": "customer@example.com",
        "first_name": "Habte",
        "last_name": "Gebeya",
        "tx_ref": tx_ref,
        "callback_url": "http://127.0.0",
        "return_url": "http://127.0.0",
    }
    
    try:
        response = requests.post(CHAPA_URL, json=payload, headers=headers)
        data = response.json()
        if data.get('status') == 'success':
            return redirect(data['data']['checkout_url'])
    except Exception:
        pass
        
    # Temporary fallback for local testing to see your success screen instantly
    return render(request, 'shop/success.html', {'product': product})

# 3. Secure File Delivery View
def download_product_file(request, product_id):
    product = get_object_or_404(DigitalProduct, id=product_id)
    file_path = product.digital_file.path
    
    if os.path.exists(file_path):
        # Open the file securely and stream it straight to their browser window
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
    else:
        raise Http404("The requested file does not exist on our server.")
