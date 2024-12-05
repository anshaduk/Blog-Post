import requests

def fetch_data(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def get_client_ip(request):
    return request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0] or request.META.get('REMOTE_ADDR')

def get_public_ip():
    data = fetch_data('https://api64.ipify.org?format=json')
    return data.get('ip') if data else None

def get_user_country(request):
    ip = get_client_ip(request)
    if ip in {'127.0.0.1', '::1'}:  
        ip = get_public_ip()

    if not ip:
        return 'Unknown'

    data = fetch_data(f'http://ip-api.com/json/{ip}')
    return data.get('country', 'Unknown') if data else 'Unknown'
